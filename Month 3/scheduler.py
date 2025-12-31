import schedule
import time
import logging
from etl_pipeline import run_etl

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def job():
    logging.info("⏰ Scheduler: Triggering ETL Pipeline...")
    run_etl()

# Schedule the pipeline to run every 1 hour
schedule.every(1).hours.do(job)

# For testing purposes, you can uncomment the line below to run every minute:
# schedule.every(1).minutes.do(job)

if __name__ == "__main__":
    logging.info("🚀 Weather Pipeline Scheduler Started. Press Ctrl+C to stop.")
    # Run once immediately on start
    job()
    
    while True:
        schedule.run_pending()
        time.sleep(1)
