from sqlalchemy.orm import Session
from database.models.groundwater_reading import GroundwaterReading
from datetime import datetime
from typing import Optional

class ReadingRepository:
    def get_readings_by_station(self, db: Session, station_id: int, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None):
        query = db.query(GroundwaterReading).filter(GroundwaterReading.station_id == station_id)
        if start_date:
            query = query.filter(GroundwaterReading.timestamp >= start_date)
        if end_date:
            query = query.filter(GroundwaterReading.timestamp <= end_date)
        return query.order_by(GroundwaterReading.timestamp.asc()).all()
        
    def create_reading(self, db: Session, station_id: int, timestamp: datetime, groundwater_level: float):
        reading = GroundwaterReading(station_id=station_id, timestamp=timestamp, groundwater_level=groundwater_level)
        db.add(reading)
        db.commit()
        db.refresh(reading)
        return reading

reading_repository = ReadingRepository()
