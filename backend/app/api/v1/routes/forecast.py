from fastapi import APIRouter
from schemas.forecast import ForecastRequest, ForecastResponse
from services.forecasting import forecasting_service

router = APIRouter()

@router.post("/{station_id}", response_model=ForecastResponse)
def generate_forecast(station_id: str, request: ForecastRequest):
    """
    Generate future groundwater level predictions using the station's trained model.
    """
    return forecasting_service.generate_forecast(station_id, request)
