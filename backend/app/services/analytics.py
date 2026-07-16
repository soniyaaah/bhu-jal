from schemas.analytics import AnomalyRequest, AnomalyResponse
from core.logger import logger
from services.model_registry import model_registry

class AnalyticsService:
    @staticmethod
    def detect_anomaly(request: AnomalyRequest) -> AnomalyResponse:
        """
        Detects if a given reading is anomalous.
        """
        # Validate station exists
        model_registry.validate_station(request.station_id)
        
        logger.debug(f"Checking anomaly for {request.station_id} at {request.timestamp}")
        
        # Mock logic since anomaly models are not in artifacts
        # We assume any water level above 50 or below 5 is anomalous
        is_anomaly = False
        score = 0.0
        
        if request.water_level > 50.0:
            is_anomaly = True
            score = 0.95
        elif request.water_level < 5.0:
            is_anomaly = True
            score = 0.85
        else:
            score = 0.1
            
        return AnomalyResponse(
            is_anomaly=is_anomaly,
            anomaly_score=score,
            threshold=0.75
        )

analytics_service = AnalyticsService()
