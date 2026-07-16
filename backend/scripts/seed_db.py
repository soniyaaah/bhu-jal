import sys
import os

# Add app to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from database.session import SessionLocal
from database.repositories import station_repository
from core.logger import logger

import pandas as pd

def seed_stations():
    logger.info("Starting dynamic station seeding from dataset...")
    db = SessionLocal()
    dataset_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../data/raw/dwlr_hyderabad.xlsx'))
    
    if not os.path.exists(dataset_path):
        logger.error(f"Dataset not found at {dataset_path}")
        return
        
    try:
        df = pd.read_excel(dataset_path)
        
        # Extract unique stations and their metadata (taking the first occurrence for metadata)
        unique_stations = df.drop_duplicates(subset=['Station']).dropna(subset=['Station'])
        
        for index, row in unique_stations.iterrows():
            raw_name = str(row['Station']).strip()
            # Normalize name to match ML Artifacts
            normalized_name = raw_name.upper().replace(" ", "_")
            
            lat = float(row['Latitude']) if not pd.isna(row['Latitude']) else 0.0
            lon = float(row['Longitude']) if not pd.isna(row['Longitude']) else 0.0
            dist = str(row['District']).strip() if not pd.isna(row['District']) else "Unknown"
            
            existing = station_repository.get_station_by_name(db, normalized_name)
            if not existing:
                station_repository.create_station(
                    db=db,
                    name=normalized_name,
                    latitude=lat,
                    longitude=lon,
                    district=dist
                )
                logger.info(f"Seeded station: {normalized_name}")
            else:
                logger.info(f"Station already exists: {normalized_name}")
                
    except Exception as e:
        logger.error(f"Failed to seed stations dynamically: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    logger.info("Starting seed script...")
    seed_stations()
    logger.info("Seed script finished.")
