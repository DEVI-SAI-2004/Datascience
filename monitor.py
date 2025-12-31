import os
import sqlite3
from datetime import datetime

def check_system_health():
    print("🔍 SYSTEM HEALTH CHECK")
    print("-" * 30)
    
    # 1. Check Database File
    db_file = 'weather_data.db'
    if os.path.exists(db_file):
        size_kb = os.path.getsize(db_file) / 1024
        print(f"✅ Database Status: Online ({round(size_kb, 2)} KB)")
    else:
        print("❌ Database Status: Offline (File not found)")
        return

    # 2. Check Data Volume
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM weather_data")
    count = cursor.fetchone()[0]
    print(f"📈 Total Records: {count}")

    # 3. Check Last Run
    cursor.execute("SELECT MAX(timestamp) FROM weather_data")
    last_run = cursor.fetchone()[0]
    print(f"⏰ Last Successful Run: {last_run}")

    # 4. Check Error Logs
    log_file = 'pipeline.log'
    if os.path.exists(log_file):
        with open(log_file, 'r') as f:
            errors = [line for line in f.readlines() if "ERROR" in line]
            print(f"🚨 Total System Errors: {len(errors)}")
    
    conn.close()

if __name__ == "__main__":
    check_system_health()