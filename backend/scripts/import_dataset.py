import sys
import os
import pandas as pd
from datetime import datetime
import numpy as np

# Add app to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from database.session import SessionLocal
from database.repositories.station_repository import station_repository
from database.models.groundwater_reading import GroundwaterReading
from core.logger import logger

def import_dataset(file_path: str):
    logger.info(f"Starting dataset import from {file_path}")
    
    try:
        df = pd.read_excel(file_path)
    except Exception as e:
        logger.error(f"Failed to read dataset: {e}")
        return

    required_cols = ['Station', 'Data Acquisition Time', 'Groundwater Level Telemetry 6 Hourly _meter_']
    for col in required_cols:
        if col not in df.columns:
            logger.error(f"Missing required column: {col}")
            return

    db = SessionLocal()
    try:
        stations = station_repository.get_stations(db)
        station_map = {s.name: s.id for s in stations}

        inserted = 0
        skipped = 0
        failed = 0
        readings_to_insert = []

        for index, row in df.iterrows():
            try:
                raw_name = str(row['Station']).strip()
                if pd.isna(row['Station']) or not raw_name:
                    skipped += 1
                    continue
                    
                # Dynamically match Excel names to DB/Artifact names (e.g., 'Amberpet_1' -> 'AMBERPET_1')
                station_name = raw_name.upper().replace(" ", "_")

                if station_name not in station_map:
                    skipped += 1
                    continue

                station_id = station_map[station_name]
                
                ts_str = str(row['Data Acquisition Time'])
                if pd.isna(row['Data Acquisition Time']) or ts_str.lower() == 'nan':
                    skipped += 1
                    continue
                    
                timestamp = pd.to_datetime(ts_str)

                wl_val = row['Groundwater Level Telemetry 6 Hourly _meter_']
                if pd.isna(wl_val):
                    skipped += 1
                    continue
                    
                water_level = float(wl_val)

                reading = GroundwaterReading(
                    station_id=station_id,
                    timestamp=timestamp,
                    groundwater_level=water_level
                )
                readings_to_insert.append(reading)
                
                if len(readings_to_insert) >= 1000:
                    db.bulk_save_objects(readings_to_insert)
                    db.commit()
                    inserted += len(readings_to_insert)
                    readings_to_insert = []

            except Exception as e:
                failed += 1
                logger.error(f"Failed to process row {index}: {e}")
                
        if readings_to_insert:
            db.bulk_save_objects(readings_to_insert)
            db.commit()
            inserted += len(readings_to_insert)

        logger.info(f"Import Summary: {inserted} inserted, {skipped} skipped, {failed} failed.")

    finally:
        db.close()

if __name__ == "__main__":
    dataset_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../data/raw/dwlr_hyderabad.xlsx'))
    if not os.path.exists(dataset_path):
        logger.error(f"Dataset not found at {dataset_path}")
    else:
        import_dataset(dataset_path)
