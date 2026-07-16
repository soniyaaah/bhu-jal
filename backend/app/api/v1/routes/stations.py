from fastapi import APIRouter
from typing import List, Optional
from datetime import datetime
from schemas.station import StationResponse, StationDataResponse
from services.model_registry import model_registry
import random
from datetime import timedelta

router = APIRouter()

@router.get("", response_model=List[StationResponse])
def get_stations():
    """
    Retrieve a list of all available monitoring stations.
    """
    return model_registry.get_all_stations()

@router.get("/{station_id}/data", response_model=List[StationDataResponse])
def get_station_data(station_id: str, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None):
    """
    Retrieve historical groundwater readings for a specific station.
    """
    model_registry.validate_station(station_id)
    
    # Mock data generation since database is not connected
    mock_data = []
    base_date = start_date or (datetime.now() - timedelta(days=30))
    limit_date = end_date or datetime.now()
    
    curr = base_date
    while curr <= limit_date:
        mock_data.append(
            StationDataResponse(
                timestamp=curr,
                water_level=random.uniform(5.0, 30.0)
            )
        )
        curr += timedelta(days=1)
        
    return mock_data
