from pydantic import BaseModel, Field
from typing import List
from datetime import datetime

class CurrentFeatures(BaseModel):
    water_level: float = Field(..., description="Current water level reading")
    temperature: float = Field(0.0, description="Current temperature (default 0.0 if unknown)")
    precipitation: float = Field(0.0, description="Current precipitation (default 0.0 if unknown)")

class ForecastRequest(BaseModel):
    horizon_days: int = Field(..., ge=1, le=30, description="Number of days to forecast")
    current_features: CurrentFeatures

class ForecastData(BaseModel):
    target_date: datetime
    predicted_water_level: float

class ForecastResponse(BaseModel):
    station_id: str
    forecast: List[ForecastData]
