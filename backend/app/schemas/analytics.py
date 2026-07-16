from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class AnomalyRequest(BaseModel):
    station_id: str
    timestamp: datetime
    water_level: float

class AnomalyResponse(BaseModel):
    is_anomaly: bool
    anomaly_score: float
    threshold: float
