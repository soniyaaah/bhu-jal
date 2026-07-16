from sqlalchemy.orm import Session
from database.models.station import Station

class StationRepository:
    def get_stations(self, db: Session):
        return db.query(Station).all()
        
    def get_station_by_id(self, db: Session, station_id: int):
        return db.query(Station).filter(Station.id == station_id).first()
        
    def get_station_by_name(self, db: Session, name: str):
        return db.query(Station).filter(Station.name == name).first()
        
    def create_station(self, db: Session, name: str, latitude: float, longitude: float, district: str = None):
        station = Station(name=name, latitude=latitude, longitude=longitude, district=district)
        db.add(station)
        db.commit()
        db.refresh(station)
        return station

station_repository = StationRepository()
