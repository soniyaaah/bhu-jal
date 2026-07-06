# bhu-

### repo structure
groundwater-intelligence-platform/
│
├── README.md
├── LICENSE
├── .gitignore
├── .env.example
├── requirements.txt
├── pyproject.toml              # Optional, recommended later
├── docker-compose.yml          # Later
├── Dockerfile                  # Later
│
├── docs/
│   ├── architecture.md
│   ├── api.md
│   ├── dataset.md
│   ├── model.md
│   ├── dashboard.md
│   └── deployment.md
│
├── data/
│   ├── raw/
│   │   └── dwlr_hyderabad.xlsx
│   │
│   ├── interim/
│   │
│   ├── processed/
│   │
│   └── external/
│
├── notebooks/
│   ├── 01_dataset_overview.ipynb
│   ├── 02_eda.ipynb
│   └── 03_model_experiments.ipynb
│
├── backend/
│   │
│   ├── app/
│   │   ├── main.py
│   │   │
│   │   ├── api/
│   │   │   ├── forecast.py
│   │   │   ├── anomaly.py
│   │   │   ├── analytics.py
│   │   │   └── stations.py
│   │   │
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── logger.py
│   │   │   └── constants.py
│   │   │
│   │   ├── database/
│   │   │   ├── session.py
│   │   │   ├── models.py
│   │   │   └── schema.py
│   │   │
│   │   ├── services/
│   │   │   ├── forecasting.py
│   │   │   ├── anomaly.py
│   │   │   ├── analytics.py
│   │   │   └── preprocessing.py
│   │   │
│   │   ├── utils/
│   │   │
│   │   └── websocket/
│   │
│   └── tests/
│
├── ml/
│   │
│   ├── data/
│   │   ├── load_data.py
│   │   ├── clean_data.py
│   │   ├── validate.py
│   │   └── feature_engineering.py
│   │
│   ├── forecasting/
│   │   ├── train.py
│   │   ├── predict.py
│   │   ├── evaluate.py
│   │   ├── random_forest.py
│   │   ├── lstm.py
│   │   └── prophet.py
│   │
│   ├── anomaly/
│   │   ├── isolation_forest.py
│   │   ├── lof.py
│   │   └── autoencoder.py
│   │
│   ├── pipelines/
│   │
│   ├── artifacts/
│   │
│   └── reports/
│
├── frontend/
│   ├── public/
│   ├── src/
│   │
│   ├── package.json
│   └── vite.config.ts
│
├── scripts/
│   ├── ingest.py
│   ├── retrain.py
│   ├── simulate_stream.py
│   └── seed_database.py
│
└── assets/
    ├── screenshots/
    └── icons/