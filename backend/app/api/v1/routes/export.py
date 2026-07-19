from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from database.session import get_db
from database.repositories.reading_repository import reading_repository
from database.repositories.station_repository import station_repository
import csv
from io import StringIO
from datetime import datetime
from typing import Optional

router = APIRouter()

@router.get("/readings")
def export_readings(
    station_id: Optional[str] = None,
    format: str = "csv",
    db: Session = Depends(get_db)
):
    """
    Export groundwater readings in CSV or JSON format.
    """
    station = None
    if station_id:
        station = station_repository.get_station_by_name(db, station_id)
        if not station:
            raise HTTPException(status_code=404, detail="Station not found")
        readings = reading_repository.get_readings_by_station(db, station.id)
    else:
        # Get all readings - this might be large in production, but okay for this phase
        from database.models.groundwater_reading import GroundwaterReading
        readings = db.query(GroundwaterReading).order_by(GroundwaterReading.timestamp.asc()).all()
        
    if format.lower() == "json":
        return [
            {
                "station_id": r.station.name if r.station else r.station_id,
                "timestamp": r.timestamp.isoformat(),
                "water_level": r.groundwater_level
            }
            for r in readings
        ]
        
    elif format.lower() == "csv":
        output = StringIO()
        writer = csv.writer(output)
        writer.writerow(["Station ID", "Timestamp", "Water Level"])
        
        for r in readings:
            writer.writerow([
                r.station.name if r.station else r.station_id,
                r.timestamp.isoformat(),
                r.groundwater_level
            ])
            
        return Response(
            content=output.getvalue(),
            media_type="text/csv",
            headers={"Content-Disposition": f"attachment; filename=readings_export.csv"}
        )
    
    else:
        raise HTTPException(status_code=400, detail="Invalid format. Use 'csv' or 'json'.")
