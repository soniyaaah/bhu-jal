# API Contract

This document outlines the planned REST API contract for the Groundwater Intelligence Platform backend.

## General
- **Base URL**: `/api/v1`
- **Content-Type**: `application/json`
- **Authentication**: Placeholder (Future implementation using JWT tokens, expected in `Authorization: Bearer <token>` header).

---

## Endpoints

### 1. Get Stations
- **Endpoint**: `/stations`
- **Method**: `GET`
- **Purpose**: Retrieve a list of all available monitoring stations.
- **Request Schema**: None
- **Response Schema**:
  ```json
  [
    {
      "station_id": "string",
      "name": "string",
      "latitude": "float",
      "longitude": "float"
    }
  ]
  ```
- **Status Codes**: 
  - `200 OK`: Successful retrieval.

### 2. Get Station Data
- **Endpoint**: `/stations/{station_id}/data`
- **Method**: `GET`
- **Purpose**: Retrieve historical groundwater readings for a specific station.
- **Request Schema** (Query Parameters):
  - `start_date` (optional): ISO 8601 string
  - `end_date` (optional): ISO 8601 string
- **Response Schema**:
  ```json
  [
    {
      "timestamp": "string (ISO 8601)",
      "water_level": "float"
    }
  ]
  ```
- **Status Codes**: 
  - `200 OK`: Successful retrieval.
  - `404 Not Found`: Station ID does not exist.

### 3. Generate Forecast
- **Endpoint**: `/forecast/{station_id}`
- **Method**: `POST`
- **Purpose**: Generate future groundwater level predictions using the station's trained model.
- **Request Schema**:
  ```json
  {
    "horizon_days": "integer (1-30)",
    "current_features": {
      "water_level": "float",
      "temperature": "float",
      "precipitation": "float"
    }
  }
  ```
- **Response Schema**:
  ```json
  {
    "station_id": "string",
    "forecast": [
      {
        "target_date": "string (ISO 8601)",
        "predicted_water_level": "float"
      }
    ]
  }
  ```
- **Status Codes**: 
  - `200 OK`: Forecast generated successfully.
  - `400 Bad Request`: Invalid input features.
  - `404 Not Found`: Model for station not found.

### 4. Detect Anomalies
- **Endpoint**: `/anomaly/detect`
- **Method**: `POST`
- **Purpose**: Check if a recent reading is an anomaly based on historical patterns.
- **Request Schema**:
  ```json
  {
    "station_id": "string",
    "timestamp": "string (ISO 8601)",
    "water_level": "float"
  }
  ```
- **Response Schema**:
  ```json
  {
    "is_anomaly": "boolean",
    "anomaly_score": "float",
    "threshold": "float"
  }
  ```
- **Status Codes**: 
  - `200 OK`: Success.

---

## Validation
- All payloads will be strictly validated using Pydantic models in FastAPI. 
- Validation errors will return a `422 Unprocessable Entity` status code with details on the invalid fields.

## Swagger Notes
FastAPI will automatically generate Swagger UI at `/docs` and ReDoc at `/redoc`. All endpoints should have descriptive docstrings for automatic documentation generation.
