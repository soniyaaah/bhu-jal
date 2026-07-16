# Architectural Decisions

This document records the architectural decisions discovered or established during the development of the Groundwater Intelligence Platform.

## 1. Station-wise Models
**Decision**: Train individual models for each monitoring station rather than a single global model.
- **Why**: Groundwater dynamics are highly localized, depending on specific geological features, extraction rates, and proximity to water bodies. A global model would struggle to capture these micro-variations.
- **Trade-off**: Increases the number of artifacts to manage and load, but significantly improves prediction accuracy.

## 2. Saved Artifacts via Pickle
**Decision**: Models and scalers are saved as `.pkl` files using `joblib` or `pickle`.
- **Why**: Scikit-learn and related libraries natively support pickle serialization, making it the fastest and easiest way to persist the pipeline state (both the algorithm and the data scaling parameters).
- **Assumption**: Security of the deployment environment is controlled, as unpickling untrusted data is a security risk.

## 3. Separation of Preprocessing Pipelines
**Decision**: Scaling is saved as separate `_scaler_X.pkl` and `_scaler_y.pkl` artifacts rather than bundled within the model object.
- **Why**: Allows flexibility. Features can be scaled for analysis without loading the entire prediction model, and targets can be inverse-transformed easily after inference.

## 4. Choice of FastAPI (Backend)
**Decision**: Use FastAPI instead of Flask or Django.
- **Why**: FastAPI provides built-in Pydantic validation, automatic Swagger documentation, and high performance due to its asynchronous capabilities. It is highly suitable for building ML inference APIs.

## 5. Modular Services (Architecture)
**Decision**: Separate routing, business logic (services), and data access.
- **Why**: Promotes testability and maintainability. The prediction logic can be tested independently of the HTTP routing layer.

## 6. Assumptions Made During Documentation Phase
- **Assumption**: The target variable is future groundwater level.
- **Assumption**: The large size of `AMBERPET_1_model.pkl` (17MB) indicates an ensemble model (like Random Forest), whereas smaller models (~1KB) indicate simple linear models or unresolved training configurations.
- **Assumption**: Data frequency in the raw dataset is consistent enough to support time-series forecasting.
- **Assumption**: A relational database (PostgreSQL/MySQL) will be used to store historical readings, as time-series variations and anomalies need to be related back to specific stations.
