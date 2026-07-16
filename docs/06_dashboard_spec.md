# Dashboard Specification

This document details the frontend dashboard for the Groundwater Intelligence Platform.

## Overview
The dashboard will serve as the primary interface for users to visualize historical groundwater data, view future forecasts, and monitor anomalies. 

## Key Sections

### 1. Overview Cards (Homepage)
High-level summary metrics:
- Total active monitoring stations.
- Average groundwater level across all stations (current week vs previous week).
- Number of active anomalies detected.
- System health / Latest data sync timestamp.

### 2. Interactive Map (GIS Visualization)
- **Features**: A map of Hyderabad showing pinpoints for every monitoring station.
- **Interactions**: 
  - Color-coded pins (Green = Normal, Red = Anomaly/Critical Level).
  - Hovering displays a tooltip with the station name and current water level.
  - Clicking a pin navigates to the detailed Station Page.

### 3. Station Page
Deep dive into a specific station's data.
- **Charts**: 
  - A primary time-series line chart displaying historical water levels.
  - Overlay of predicted water levels (forecasts) with confidence intervals (if supported by the model).
- **Statistics**: Max, min, and average levels for the selected time range.
- **Filters**: Date range picker to adjust the chart view (e.g., Last 7 days, 1 Month, 1 Year).

### 4. Forecast Page
Aggregate view of predictions.
- **Charts**: Bar charts or heatmaps comparing predicted critical levels across different stations.
- **Export**: Ability to export forecast data to CSV/Excel for external reporting.

### 5. Anomaly Page
A dedicated inbox-style view for anomalies.
- **Table**: List of recent anomalies, sortable by severity (anomaly score) or date.
- **Action**: (Future) Ability for an admin to mark an anomaly as "Verified" or "False Alarm".

## Responsive Behavior
- The dashboard must be fully responsive, functioning smoothly on desktop monitors, tablets, and mobile devices.
- Sidebar navigation should collapse into a hamburger menu on smaller screens.
- Charts should automatically resize to fit container widths.

## Theme Support
- **Light/Dark Mode**: Built-in toggle for user preference. Map tiles should ideally switch to a dark theme variant when in dark mode to reduce eye strain.

## Frameworks (Assumption)
- Built using React/Vite (indicated by `frontend/vite.config.ts`).
- Charts powered by libraries like Recharts or Chart.js.
- Map powered by Leaflet or React Map GL.
