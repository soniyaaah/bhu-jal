from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from database.base import Base
from sqlalchemy.orm import relationship

class Station(Base):
    __tablename__ = "stations"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    district = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
