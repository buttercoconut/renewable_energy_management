# Renewable Energy Management Project

## Overview
This repository contains a full-stack application for managing renewable energy assets, including predictive analytics, maintenance scheduling, and safety reporting.

## Directory Structure
- **backend/** – FastAPI backend with LSTM prediction service.
- **frontend/** – Vue 3 SPA with charts and dashboards.

## Getting Started
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   npm install
   ```
2. Run the backend:
   ```bash
   uvicorn backend.api.main:app --reload
   ```
3. Run the frontend:
   ```bash
   npm run dev
   ```

## Testing
Run the test suite:
```bash
pytest
```
