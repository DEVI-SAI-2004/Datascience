# Weather Data Pipeline System

## 📌 Project Overview
An end-to-end data engineering pipeline that extracts real-time weather data from OpenWeatherMap, transforms it, and loads it into a normalized SQLite database.

## 🏗️ Architecture
- **Extract**: Fetches JSON data via OpenWeatherMap API.
- **Transform**: Validates data ranges and cleans timestamps.
- **Load**: Inserts data into a 3-table normalized SQLite schema.
- **Monitor**: Automated reporting and system health checks.

## 🚀 Setup Instructions
1. Clone the repository.
2. Install dependencies: `pip install requests pandas schedule`.
3. Add your API key to `config.py`.
4. Run the scheduler: `python scheduler.py`.

## 📊 Database Schema
- `cities`: Master list of locations.
- `weather_data`: Historical weather records.
- `alerts`: Log of extreme weather events.