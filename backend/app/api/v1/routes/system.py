from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from database.session import get_db
from services.model_registry import model_registry
from services.websocket_manager import manager
from services.scheduler import scheduler_service
from database.models.groundwater_reading import GroundwaterReading
from database.models.prediction import Prediction
from database.models.station import Station
import datetime

router = APIRouter()

# Simple uptime tracker
START_TIME = datetime.datetime.now(datetime.timezone.utc)

@router.get("/health")
def health_check(db: Session = Depends(get_db)):
    """
    Health check endpoint for the backend services.
    """
    # Check DB
    try:
        db.execute(text("SELECT 1"))
        db_status = "connected"
    except Exception:
        db_status = "disconnected"

    uptime = datetime.datetime.now(datetime.timezone.utc) - START_TIME
    
    return {
        "status": "healthy" if db_status == "connected" else "unhealthy",
        "database": db_status,
        "models_loaded": len(model_registry.get_all_stations()),
        "scheduler": scheduler_service.get_status(),
        "websocket_clients": len(manager.active_connections),
        "uptime": str(uptime)
    }

@router.get("/metrics")
def get_metrics(db: Session = Depends(get_db)):
    """
    Returns system metrics.
    """
    total_readings = db.query(GroundwaterReading).count()
    total_predictions = db.query(Prediction).count()
    active_stations = db.query(Station).count()

    return {
        "total_readings": total_readings,
        "total_predictions": total_predictions,
        "active_stations": active_stations,
        "connected_clients": len(manager.active_connections)
    }
