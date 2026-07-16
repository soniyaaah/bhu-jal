from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class StationBase(BaseModel):
    station_id: str
    name: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None

class StationResponse(StationBase):
    pass

class StationDataResponse(BaseModel):
    timestamp: datetime
    water_level: float
