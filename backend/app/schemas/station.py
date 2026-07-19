from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class StationBase(BaseModel):
    id: str
    name: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    district: Optional[str] = None
    created_at: Optional[datetime] = None

class StationResponse(StationBase):
    pass

class StationDataResponse(BaseModel):
    timestamp: datetime
    water_level: float

class IngestionPayload(BaseModel):
    station_id: str
    timestamp: datetime
    water_level: float
