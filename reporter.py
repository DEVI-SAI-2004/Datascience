import sqlite3
import pandas as pd
from datetime import datetime

def get_db_connection():
    return sqlite3.connect('weather_data.db')

def generate_daily_report():
    conn = get_db_connection()
    
    print("\n" + "="*30)
    print("📊 WEATHER SYSTEM REPORT")
    print(f"⏰ Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*30)

    # 1. Query: Current Snapshot (Latest record for each city)
    print("\n🌤️ CURRENT WEATHER SNAPSHOT:")
    query_snapshot = '''
        SELECT c.city_name, w.temperature_c, w.humidity, w.weather_condition
        FROM cities c
        JOIN weather_data w ON c.city_id = w.city_id
        WHERE w.timestamp = (SELECT MAX(timestamp) FROM weather_data w2 WHERE w2.city_id = w.city_id)
    '''
    df_snapshot = pd.read_sql_query(query_snapshot, conn)
    for index, row in df_snapshot.iterrows():
        print(f"📍 {row['city_name']}: {row['temperature_c']}°C, {row['humidity']}% humidity, {row['weather_condition']}")

    # 2. Analytics: Highest Average Temperature
    print("\n📈 ANALYTICS INSIGHTS:")
    query_avg = '''
        SELECT c.city_name, AVG(w.temperature_c) as avg_temp
        FROM cities c
        JOIN weather_data w ON c.city_id = w.city_id
        GROUP BY c.city_name
        ORDER BY avg_temp DESC
        LIMIT 1
    '''
    cursor = conn.cursor()
    cursor.execute(query_avg)
    top_city = cursor.fetchone()
    if top_city:
        print(f"🔥 Highest Avg Temp: {top_city[0]} ({round(top_city[1], 2)}°C)")

    # 3. Alerts: Check for extreme conditions (e.g., Temp > 30°C)
    print("\n📅 TODAY'S ALERTS:")
    alert_threshold = 30.0
    alerts_found = df_snapshot[df_snapshot['temperature_c'] > alert_threshold]
    
    if not alerts_found.empty:
        for _, alert in alerts_found.iterrows():
            print(f"⚠️ High Temp Alert: {alert['city_name']} ({alert['temperature_c']}°C)")
            # Log alert to the 'alerts' table
            cursor.execute('''INSERT INTO alerts (city_id, alert_type, threshold_value, actual_value)
                              SELECT city_id, 'High Temperature', ?, ? 
                              FROM cities WHERE city_name = ?''', 
                           (alert_threshold, alert['temperature_c'], alert['city_name']))
    else:
        print("✅ No extreme weather alerts.")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    generate_daily_report()