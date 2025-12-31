import sqlite3

def setup_database():
    # Connect to the database file (it will be created if it doesn't exist)
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    
    # 1. Create 'cities' table (Master data)
    cursor.execute('''CREATE TABLE IF NOT EXISTS cities (
                        city_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        city_name TEXT NOT NULL UNIQUE,
                        country TEXT,
                        latitude REAL,
                        longitude REAL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )''')
    
    # 2. Create 'weather_data' table (Time-series data)
    cursor.execute('''CREATE TABLE IF NOT EXISTS weather_data (
                        record_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        city_id INTEGER,
                        timestamp TIMESTAMP,
                        temperature_c REAL,
                        humidity INTEGER,
                        pressure_hpa REAL,
                        wind_speed_mps REAL,
                        weather_condition TEXT,
                        FOREIGN KEY (city_id) REFERENCES cities (city_id)
                    )''')
    
    # 3. Create 'alerts' table (Monitoring & Reporting)
    cursor.execute('''CREATE TABLE IF NOT EXISTS alerts (
                        alert_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        city_id INTEGER,
                        alert_type TEXT,
                        threshold_value REAL,
                        actual_value REAL,
                        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        FOREIGN KEY (city_id) REFERENCES cities (city_id)
                    )''')
    
    conn.commit()
    conn.close()
    print("✅ Database and 3 normalized tables created successfully.")

if __name__ == "__main__":
    setup_database()