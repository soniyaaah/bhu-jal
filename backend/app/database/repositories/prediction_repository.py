from sqlalchemy.orm import Session
from database.models.prediction import Prediction
from datetime import datetime

class PredictionRepository:
    def create_prediction(self, db: Session, station_id: int, predicted_value: float, model_name: str, model_version: str, processing_time_ms: float):
        prediction = Prediction(
            station_id=station_id,
            predicted_value=predicted_value,
            model_name=model_name,
            model_version=model_version,
            processing_time_ms=processing_time_ms
        )
        db.add(prediction)
        db.commit()
        db.refresh(prediction)
        return prediction

    def get_predictions_by_station(self, db: Session, station_id: int, limit: int = 100):
        return db.query(Prediction).filter(Prediction.station_id == station_id).order_by(Prediction.prediction_time.desc()).limit(limit).all()

prediction_repository = PredictionRepository()
