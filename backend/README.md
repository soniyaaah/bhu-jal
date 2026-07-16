# Backend Application

This is the FastAPI backend for the Groundwater Intelligence Platform.

## Architecture
The backend follows a service-oriented architecture:
- `api/`: Contains FastAPI route definitions grouped by domain (Stations, Forecast, Anomaly).
- `core/`: Application-wide settings, configuration, and exception handlers.
- `schemas/`: Pydantic models defining input and output validation structures.
- `services/`: Business logic, particularly the `ModelRegistry` which auto-discovers and loads ML artifacts from `../../ml/artifacts`.

## Running the Application

### Development
1. Ensure all dependencies are installed:
   ```bash
   pip install -r ../requirements.txt
   ```
2. Start the Uvicorn development server:
   ```bash
   cd backend/app
   uvicorn main:app --reload
   ```
3. Access the API documentation:
   - Swagger UI: `http://127.0.0.1:8000/docs`
   - ReDoc: `http://127.0.0.1:8000/redoc`

## Future Phases
- Database Integration (SQLAlchemy setup under `database/`)
- Real-time updates via WebSockets (`websocket/`)
