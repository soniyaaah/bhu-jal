from fastapi import APIRouter
from api.v1.routes import stations, forecast, analytics, system

api_router = APIRouter()

api_router.include_router(system.router, tags=["System"])
api_router.include_router(stations.router, prefix="/stations", tags=["Stations"])
api_router.include_router(forecast.router, prefix="/forecast", tags=["Forecast"])
api_router.include_router(analytics.router, prefix="/anomaly", tags=["Anomaly"])
