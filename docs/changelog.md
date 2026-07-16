# Changelog

All notable changes to the Groundwater Intelligence Platform will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - Initial Setup & ML Artifacts

### Added
- Comprehensive project documentation generated in the `docs/` directory, acting as the single source of truth for future implementation.
- Repository structure blueprint defined (Backend, Frontend, ML, Scripts).
- Raw DWLR dataset files placed in `data/raw/` (`dwlr_hyderabad.xlsx`, `big_telegana.xlsx`).
- Initial requirements file (`requirements.txt`) containing necessary data science and backend dependencies.
- Machine learning artifacts (models, input scalers, output scalers) saved in `ml/artifacts/` for 6 monitoring stations:
  - AMBERPET_1
  - BAGH_LINGAMPALLY-PZ_1
  - BEGAMPET_(BALKAMPET)
  - BEGAMPET_(IMD)
  - BOWENPALLY_1
  - ERRAGADDA-PZ_1
- Placeholder scripts for feature engineering, model training, and data loading under `ml/`.
- Jupyter notebook placeholders for EDA and model experimentation in `notebooks/`.
