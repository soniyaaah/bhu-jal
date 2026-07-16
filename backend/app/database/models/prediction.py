from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Index
from sqlalchemy.sql import func
from database.base import Base
from sqlalchemy.orm import relationship

class Prediction(Base):
    __tablename__ = "predictions"
    id = Column(Integer, primary_key=True, index=True)
    station_id = Column(Integer, ForeignKey("stations.id", ondelete="CASCADE"), nullable=False)
    prediction_time = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    predicted_value = Column(Float, nullable=False)
    model_name = Column(String, nullable=False)
    model_version = Column(String, nullable=False)
    processing_time_ms = Column(Float, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    station = relationship("Station")
    
    __table_args__ = (
        Index("idx_predictions_station_time", "station_id", "prediction_time"),
    )
