from fastapi import Request
from fastapi.responses import JSONResponse
from core.logger import logger

class AppBaseException(Exception):
    """Base custom exception for the application."""
    def __init__(self, message: str, status_code: int = 500):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

class ModelNotFoundError(AppBaseException):
    def __init__(self, station_id: str):
        super().__init__(f"Model or artifacts not found for station: {station_id}", status_code=404)

class StationNotFoundError(AppBaseException):
    def __init__(self, station_id: str):
        super().__init__(f"Station not found: {station_id}", status_code=404)

class InvalidInputDataError(AppBaseException):
    def __init__(self, details: str):
        super().__init__(f"Invalid input data: {details}", status_code=400)

async def app_exception_handler(request: Request, exc: AppBaseException):
    logger.error(f"Application error: {exc.message} (status: {exc.status_code}) on {request.url}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message},
    )

async def generic_exception_handler(request: Request, exc: Exception):
    logger.exception(f"Unhandled exception on {request.url}: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"},
    )
