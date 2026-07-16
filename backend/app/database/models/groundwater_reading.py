from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey, Index
from sqlalchemy.sql import func
from database.base import Base
from sqlalchemy.orm import relationship

class GroundwaterReading(Base):
    __tablename__ = "groundwater_readings"
    id = Column(Integer, primary_key=True, index=True)
    station_id = Column(Integer, ForeignKey("stations.id", ondelete="CASCADE"), nullable=False)
    timestamp = Column(DateTime(timezone=True), nullable=False)
    groundwater_level = Column(Float, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    station = relationship("Station")

    __table_args__ = (
        Index("idx_readings_station_time", "station_id", "timestamp"),
    )
