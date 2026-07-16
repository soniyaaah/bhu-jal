from fastapi import APIRouter
from schemas.analytics import AnomalyRequest, AnomalyResponse
from services.analytics import analytics_service

router = APIRouter()

@router.post("/detect", response_model=AnomalyResponse)
def detect_anomaly(request: AnomalyRequest):
    """
    Check if a recent reading is an anomaly based on historical patterns.
    """
    return analytics_service.detect_anomaly(request)
