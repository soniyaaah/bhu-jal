import os
import joblib
from functools import lru_cache
from typing import List, Dict, Any, Tuple
from core.logger import logger
from core.exceptions import ModelNotFoundError
from schemas.station import StationResponse

# Path to the ml artifacts directory relative to this file
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
ARTIFACTS_DIR = os.path.join(PROJECT_ROOT, "ml", "artifacts")

class ModelRegistry:
    def __init__(self):
        self.artifacts_dir = ARTIFACTS_DIR
        self._available_stations: Dict[str, StationResponse] = {}
        self._discover_models()

    def _discover_models(self):
        """Scans the artifacts directory to find available models and scalers."""
        if not os.path.exists(self.artifacts_dir):
            logger.warning(f"Artifacts directory not found at {self.artifacts_dir}")
            return

        for filename in os.listdir(self.artifacts_dir):
            if filename.endswith("_model.pkl"):
                # Extract station name from filename (e.g., AMBERPET_1_model.pkl -> AMBERPET_1)
                station_id = filename.replace("_model.pkl", "")
                
                # Check if scalers exist
                scaler_x_path = os.path.join(self.artifacts_dir, f"{station_id}_scaler_X.pkl")
                scaler_y_path = os.path.join(self.artifacts_dir, f"{station_id}_scaler_y.pkl")
                
                if os.path.exists(scaler_x_path) and os.path.exists(scaler_y_path):
                    logger.info(f"Discovered complete model artifacts for station: {station_id}")
                    # In a real app, lat/long might come from a DB or metadata file
                    self._available_stations[station_id] = StationResponse(
                        id=station_id,
                        name=station_id.replace("_", " ").title(),
                        latitude=17.0, # Placeholder
                        longitude=78.0, # Placeholder
                        district="Unknown",
                        created_at=None
                    )
                else:
                    logger.warning(f"Incomplete artifacts for station: {station_id}. Missing scalers.")

    def get_all_stations(self) -> List[StationResponse]:
        """Returns a list of all stations with valid models."""
        return list(self._available_stations.values())

    def validate_station(self, station_id: str):
        """Validates if a station is supported."""
        if station_id not in self._available_stations:
            raise ModelNotFoundError(station_id)

    @lru_cache(maxsize=10)
    def load_artifacts(self, station_id: str) -> Tuple[Any, Any, Any]:
        """
        Loads the model, scaler_X, and scaler_y for a given station.
        Cached in memory to prevent repeated disk reads.
        """
        self.validate_station(station_id)
        
        logger.info(f"Loading artifacts into memory for station: {station_id}")
        
        model_path = os.path.join(self.artifacts_dir, f"{station_id}_model.pkl")
        scaler_x_path = os.path.join(self.artifacts_dir, f"{station_id}_scaler_X.pkl")
        scaler_y_path = os.path.join(self.artifacts_dir, f"{station_id}_scaler_y.pkl")
        
        try:
            model = joblib.load(model_path)
            scaler_x = joblib.load(scaler_x_path)
            scaler_y = joblib.load(scaler_y_path)
            return model, scaler_x, scaler_y
        except Exception as e:
            logger.error(f"Failed to load artifacts for {station_id}: {e}")
            raise ModelNotFoundError(station_id)

# Singleton instance
model_registry = ModelRegistry()
