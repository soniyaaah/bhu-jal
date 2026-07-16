from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health_check():
    """
    Health check endpoint for the backend services.
    """
    return {
        "status": "ok",
        "service": "Groundwater Intelligence Platform Backend"
    }
