from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime
from schemas.station import StationResponse, StationDataResponse
from database.session import get_db
from database.repositories.station_repository import station_repository
from database.repositories.reading_repository import reading_repository

router = APIRouter()

@router.get("", response_model=List[StationResponse])
def get_stations(db: Session = Depends(get_db)):
    """
    Retrieve a list of all available monitoring stations from the database.
    """
    stations = station_repository.get_stations(db)
    return [
        StationResponse(
            id=s.name, # Use name as ID for ML registry compatibility
            name=s.name,
            latitude=s.latitude,
            longitude=s.longitude,
            district=s.district or "Unknown",
            created_at=s.created_at
        ) for s in stations
    ]

@router.get("/{station_id}/data", response_model=List[StationDataResponse])
def get_station_data(
    station_id: str, 
    start_date: Optional[datetime] = None, 
    end_date: Optional[datetime] = None,
    db: Session = Depends(get_db)
):
    """
    Retrieve historical groundwater readings for a specific station from the database.
    """
    station = station_repository.get_station_by_name(db, station_id)
    if not station:
        raise HTTPException(status_code=404, detail="Station not found")
        
    readings = reading_repository.get_readings_by_station(db, station.id, start_date, end_date)
    
    return [
        StationDataResponse(
            timestamp=r.timestamp,
            water_level=r.groundwater_level
        ) for r in readings
    ]
