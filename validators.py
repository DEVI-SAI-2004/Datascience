import logging

def validate_weather_data(data):
    """
    Checks if the fetched weather data meets quality standards.
    Returns True if valid, False otherwise.
    """
    if data is None:
        return False
        
    try:
        # 1. Check for realistic temperature (Celsius)
        if not (-60 <= data['temp'] <= 60):
            logging.warning(f"⚠️ Validation Failed: Extreme temp detected ({data['temp']}°C)")
            return False
            
        # 2. Check humidity percentage (0-100)
        if not (0 <= data['humidity'] <= 100):
            logging.warning(f"⚠️ Validation Failed: Invalid humidity ({data['humidity']}%)")
            return False
            
        # 3. Check for missing critical fields
        required_fields = ['temp', 'humidity', 'city_name', 'timestamp']
        if not all(field in data for field in required_fields):
            logging.warning("⚠️ Validation Failed: Missing data fields")
            return False
            
        return True
        
    except Exception as e:
        logging.error(f"❌ Error during validation: {e}")
        return False