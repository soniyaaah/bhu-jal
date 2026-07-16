from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.forecast import ForecastRequest, ForecastResponse
from services.forecasting import forecasting_service
from database.session import get_db

router = APIRouter()

@router.post("/{station_id}", response_model=ForecastResponse)
def generate_forecast(station_id: str, request: ForecastRequest, db: Session = Depends(get_db)):
    """
    Generate future groundwater level predictions using the station's trained model.
    """
    return forecasting_service.generate_forecast(station_id, request, db)
