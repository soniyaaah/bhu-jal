from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from schemas.station import IngestionPayload
from database.session import get_db
from database.repositories.station_repository import station_repository
from database.repositories.reading_repository import reading_repository
from services.websocket_manager import manager
from services.forecasting import forecasting_service
from schemas.forecast import ForecastRequest, CurrentFeatures
from core.logger import logger

router = APIRouter()

@router.post("")
async def ingest_reading(payload: IngestionPayload, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    """
    Ingest a new real-time groundwater reading.
    Validates payload, stores reading, triggers prediction, and broadcasts WebSocket event.
    """
    logger.info(f"Ingestion started for station: {payload.station_id}")
    
    # 1. Validate and fetch station
    station = station_repository.get_station_by_name(db, payload.station_id)
    if not station:
        raise HTTPException(status_code=404, detail="Station not found")
        
    # 2. Store reading
    try:
        new_reading = reading_repository.create_reading(
            db=db,
            station_id=station.id,
            timestamp=payload.timestamp,
            groundwater_level=payload.water_level
        )
    except Exception as e:
        logger.error(f"Failed to store reading for {payload.station_id}: {e}")
        raise HTTPException(status_code=500, detail="Failed to store reading")

    logger.info(f"Reading stored successfully for {payload.station_id}")

    # 3. Generate Prediction
    try:
        forecast_req = ForecastRequest(
            horizon_days=7,
            current_features=CurrentFeatures(
                water_level=payload.water_level,
                temperature=25.0, # Placeholder
                precipitation=0.0 # Placeholder
            )
        )
        prediction = forecasting_service.generate_forecast(payload.station_id, forecast_req, db)
        logger.info(f"Prediction generated for {payload.station_id}")
        has_prediction = True
    except Exception as e:
        logger.warning(f"Could not generate prediction for {payload.station_id}: {e}")
        has_prediction = False

    # 4. Broadcast WebSocket Event (in background so we don't block response)
    async def broadcast_updates():
        # Broadcast new reading
        await manager.broadcast(
            event_type="NEW_READING",
            payload={
                "station_id": payload.station_id,
                "timestamp": payload.timestamp.isoformat(),
                "water_level": payload.water_level
            }
        )
        # Broadcast new prediction if generated
        if has_prediction:
            await manager.broadcast(
                event_type="NEW_PREDICTION",
                payload={
                    "station_id": payload.station_id,
                    "timestamp": payload.timestamp.isoformat()
                }
            )
            
    background_tasks.add_task(broadcast_updates)
    
    return {"status": "success", "message": "Data ingested successfully"}
