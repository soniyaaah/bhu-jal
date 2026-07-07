# Groundwater Dataset Audit Report

Generated on: 2026-07-06 17:48:58.318089

---

## Dataset Overview

| Metric | Value |
|--------|-------|
| Rows | 25000 |
| Columns | 22 |
| Duplicate Rows | 0 |
| Memory Usage (MB) | 17.99 |

---

## Column Names

- _id
- SlNo
- Station
- Agency
- State LGD Code
- State
- District LGD Code
- District
- Tehsil
- Block
- Village
- River
- Basin
- Tributary
- Subtributary
- SubSubtributary
- Local River
- Latitude
- Longitude
- RL_MSL
- Data Acquisition Time
- Groundwater Level Telemetry 6 Hourly _meter_

---

## Missing Values

| Column                                       |   Missing Count |   Missing Percentage |
|:---------------------------------------------|----------------:|---------------------:|
| _id                                          |               0 |                    0 |
| SlNo                                         |               0 |                    0 |
| Station                                      |               0 |                    0 |
| Agency                                       |               0 |                    0 |
| State LGD Code                               |               0 |                    0 |
| State                                        |               0 |                    0 |
| District LGD Code                            |               0 |                    0 |
| District                                     |               0 |                    0 |
| Tehsil                                       |               0 |                    0 |
| Block                                        |               0 |                    0 |
| Village                                      |               0 |                    0 |
| River                                        |               0 |                    0 |
| Basin                                        |               0 |                    0 |
| Tributary                                    |               0 |                    0 |
| Subtributary                                 |               0 |                    0 |
| SubSubtributary                              |               0 |                    0 |
| Local River                                  |               0 |                    0 |
| Latitude                                     |               0 |                    0 |
| Longitude                                    |               0 |                    0 |
| RL_MSL                                       |           25000 |                  100 |
| Data Acquisition Time                        |               0 |                    0 |
| Groundwater Level Telemetry 6 Hourly _meter_ |               0 |                    0 |

---

## Data Types

| Column                                       | Data Type      |
|:---------------------------------------------|:---------------|
| _id                                          | int64          |
| SlNo                                         | int64          |
| Station                                      | str            |
| Agency                                       | str            |
| State LGD Code                               | int64          |
| State                                        | str            |
| District LGD Code                            | int64          |
| District                                     | str            |
| Tehsil                                       | str            |
| Block                                        | str            |
| Village                                      | str            |
| River                                        | str            |
| Basin                                        | str            |
| Tributary                                    | str            |
| Subtributary                                 | str            |
| SubSubtributary                              | str            |
| Local River                                  | str            |
| Latitude                                     | float64        |
| Longitude                                    | float64        |
| RL_MSL                                       | float64        |
| Data Acquisition Time                        | datetime64[us] |
| Groundwater Level Telemetry 6 Hourly _meter_ | float64        |

---

## Numeric Statistics

|        |      _id |     SlNo | Station      | Agency   |   State LGD Code | State     |   District LGD Code | District   | Tehsil   | Block   | Village   | River   | Basin   | Tributary   | Subtributary   | SubSubtributary   | Local River   |      Latitude |     Longitude |   RL_MSL | Data Acquisition Time      |   Groundwater Level Telemetry 6 Hourly _meter_ |
|:-------|---------:|---------:|:-------------|:---------|-----------------:|:----------|--------------------:|:-----------|:---------|:--------|:----------|:--------|:--------|:------------|:---------------|:------------------|:--------------|--------------:|--------------:|---------:|:---------------------------|-----------------------------------------------:|
| count  |  25000   |  25000   | 25000        | 25000    |            25000 | 25000     |               25000 | 25000      | 25000    | 25000   | 25000     | 25000   | 25000   | 25000       | 25000          | 25000             | 25000         | 25000         | 25000         |        0 | 25000                      |                                     25000      |
| unique |    nan   |    nan   | 6            | 1        |              nan | 1         |                 nan | 1          | 1        | 1       | 1         | 1       | 1       | 1           | 1              | 1                 | 1             |   nan         |   nan         |      nan | nan                        |                                       nan      |
| top    |    nan   |    nan   | Bowenpally_1 | CGWB     |              nan | Telangana |                 nan | HYDERABAD  | -        | -       | -         | -       | -       | -           | -              | -                 | -             |   nan         |   nan         |      nan | nan                        |                                       nan      |
| freq   |    nan   |    nan   | 9410         | 25000    |              nan | 25000     |                 nan | 25000      | 25000    | 25000   | 25000     | 25000   | 25000   | 25000       | 25000          | 25000             | 25000         |   nan         |   nan         |      nan | nan                        |                                       nan      |
| mean   | 183212   | 183212   | nan          | nan      |               36 | nan       |                 507 | nan        | nan      | nan     | nan       | nan     | nan     | nan         | nan            | nan               | nan           |    17.4406    |    78.4801    |      nan | 2024-08-04 01:42:06.043200 |                                       -11.6731 |
| min    |  54304   |  54304   | nan          | nan      |               36 | nan       |                 507 | nan        | nan      | nan     | nan       | nan     | nan     | nan         | nan            | nan               | nan           |    17.3888    |    78.4361    |      nan | 2023-03-01 00:00:00        |                                       -55.34   |
| 25%    | 127453   | 127453   | nan          | nan      |               36 | nan       |                 507 | nan        | nan      | nan     | nan       | nan     | nan     | nan         | nan            | nan               | nan           |    17.4005    |    78.4742    |      nan | 2023-12-21 06:00:00        |                                       -11.85   |
| 50%    | 174136   | 174136   | nan          | nan      |               36 | nan       |                 507 | nan        | nan      | nan     | nan       | nan     | nan     | nan         | nan            | nan               | nan           |    17.4463    |    78.4761    |      nan | 2024-11-04 03:00:00        |                                        -7.76   |
| 75%    | 236575   | 236575   | nan          | nan      |               36 | nan       |                 507 | nan        | nan      | nan     | nan       | nan     | nan     | nan         | nan            | nan               | nan           |    17.4704    |    78.5001    |      nan | 2024-12-29 00:00:00        |                                        -3.98   |
| max    | 442037   | 442037   | nan          | nan      |               36 | nan       |                 507 | nan        | nan      | nan     | nan       | nan     | nan     | nan         | nan            | nan               | nan           |    17.4704    |    78.5181    |      nan | 2025-12-31 18:00:00        |                                         1.03   |
| std    |  78230.5 |  78230.5 | nan          | nan      |                0 | nan       |                   0 | nan        | nan      | nan     | nan       | nan     | nan     | nan         | nan            | nan               | nan           |     0.0308192 |     0.0213872 |      nan | nan                        |                                        12.3698 |
