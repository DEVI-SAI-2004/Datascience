import sqlite3
import logging
from api_client import fetch_weather_data
from validators import validate_weather_data
from reporter import generate_daily_report
from config import API_KEY, DB_NAME
from database import setup_database

# Configuration
API_KEY = "ad503637bed31485acc25d2a0af5ea87"  # Replace with your actual key
CITIES = ["Mumbai", "Delhi", "Bangalore", "London", "New York"]

# Configure logging to track the ETL process
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_etl():
    """Main ETL workflow: Extract, Transform, and Load data."""
    # Ensure database tables exist
    setup_database()
    
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    
    logging.info("🚀 Starting ETL Pipeline...")
    
    for city_name in CITIES:
        # 1. EXTRACT: Fetch data from API
        raw_data = fetch_weather_data(API_KEY, city_name)
        if raw_data and validate_weather_data(raw_data):
            # ... (proceed with database insertion)
        else:
            logging.warning(f"❌ Data for {city_name} failed validation or extraction.")
        if raw_data:
            try:
                # 2. TRANSFORM & LOAD (Phase A): Update/Insert City info
                cursor.execute('''INSERT OR IGNORE INTO cities (city_name, country, latitude, longitude)
                                  VALUES (?, ?, ?, ?)''', 
                               (raw_data['city_name'], raw_data['country'], 
                                raw_data['latitude'], raw_data['longitude']))
                
                # Get the city_id to maintain the relationship
                cursor.execute('SELECT city_id FROM cities WHERE city_name = ?', (city_name,))
                city_id = cursor.fetchone()[0]
                
                # 3. TRANSFORM & LOAD (Phase B): Insert Weather Record
                cursor.execute('''INSERT INTO weather_data 
                                  (city_id, timestamp, temperature_c, humidity, pressure_hpa, wind_speed_mps, weather_condition)
                                  VALUES (?, ?, ?, ?, ?, ?, ?)''',
                               (city_id, raw_data['timestamp'], raw_data['temp'], 
                                raw_data['humidity'], raw_data['pressure'], 
                                raw_data['wind_speed'], raw_data['condition']))
                
                logging.info(f"✅ Successfully processed: {city_name}")
                
            except sqlite3.Error as e:
                logging.error(f"❌ Database error for {city_name}: {e}")
        else:
            logging.warning(f"⚠️ Skipping {city_name} due to extraction failure.")
    
    conn.commit()
    conn.close()
    logging.info("🏁 ETL Pipeline completed.")
generate_daily_report()
if __name__ == "__main__":
    run_etl()
