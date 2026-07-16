# Project State

## Overall Project Status
The **Groundwater Intelligence Platform for Hyderabad** is currently in its initial phase, focusing on data preparation and machine learning model training. The fundamental machine learning artifacts have been generated, while the application layers (backend, database, frontend, deployment) remain pending.

## Completed Phases
- ✔ **Dataset Preprocessing**: Handling missing values, cleaning raw Excel files.
- ✔ **Feature Engineering**: Creating relevant time-series features.
- ✔ **Station-wise Model Training**: Individual models trained for different geographical stations.
- ✔ **Model Artifacts Generation**: Scalers and models saved in `ml/artifacts/`.

## Pending Phases
- ⬜ **Backend (FastAPI)**: Setting up API endpoints and service layers.
- ⬜ **Database**: Schema implementation and database deployment.
- ⬜ **Dashboard**: Frontend development for visualization.
- ⬜ **GIS Visualization**: Interactive map integration.
- ⬜ **Real-time Updates**: Streaming pipeline for real-time inference.
- ⬜ **Deployment**: Dockerization and cloud deployment.

## Current Repository Structure
```
groundwater-intelligence-platform/
├── README.md
├── requirements.txt
├── backend/          # Pending implementation
├── data/             # Contains raw dataset (dwlr_hyderabad.xlsx)
├── docs/             # Project documentation
├── frontend/         # Pending implementation
├── ml/               # Machine learning scripts and artifacts
│   ├── artifacts/    # Saved .pkl models and scalers
│   ├── data/         # Data processing scripts (placeholders)
│   └── forecasting/  # Training and prediction scripts (placeholders)
└── notebooks/        # Jupyter notebooks for EDA (placeholders)
```

## Existing Artifacts
Located in `ml/artifacts/`, the repository currently contains models and scalers for the following stations:
- `AMBERPET_1`
- `BAGH_LINGAMPALLY-PZ_1`
- `BEGAMPET_(BALKAMPET)`
- `BEGAMPET_(IMD)`
- `BOWENPALLY_1`
- `ERRAGADDA-PZ_1`

## Important Observations
- The repository relies on `scikit-learn`, `pandas`, `xgboost`, `lightgbm`, and `tensorflow` as indicated by `requirements.txt`.
- Data is primarily ingested from Excel (`dwlr_hyderabad.xlsx`).
- Models are highly station-specific to account for local geographical and hydrological variations.

## Technical Debt
- **Assumption**: The ML scripts (in `ml/forecasting/` and `ml/data/`) are currently placeholders and the actual logic that produced the artifacts is not fully committed to the repository.
- Lack of database integration for storing predictions and history.
- API endpoints for serving these models are not yet implemented.

## Known Assumptions
- **Assumption**: Input data contains time-series measurements of groundwater levels for specific stations.
- **Assumption**: Scalers (`_scaler_X.pkl` and `_scaler_y.pkl`) indicate that the features and target variables are normalized/standardized before training.
- **Assumption**: The target variable is likely a future groundwater level.
