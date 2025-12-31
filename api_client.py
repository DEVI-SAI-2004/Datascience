import requests
import logging
from datetime import datetime
from config import API_KEY, DB_NAME

# Configure logging to track API performance and errors
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_weather_data(api_key, city):
    """
    Fetches real-time weather data for a specific city.
    Includes error handling for rate limits and connection issues.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use Celsius
    }
    
    try:
        # Implementing a 10-second timeout to prevent the pipeline from hanging
        response = requests.get(base_url, params=params, timeout=10)
        
        # Check for HTTP errors (like 401 Unauthorized or 404 Not Found)
        response.raise_for_status()
        
        data = response.json()
        
        # Transform raw JSON into a clean dictionary for our database
        return {
            'city_name': city,
            'country': data['sys'].get('country'),
            'latitude': data['coord'].get('lat'),
            'longitude': data['coord'].get('lon'),
            'temp': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure'],
            'wind_speed': data['wind']['speed'],
            'condition': data['weather'][0]['description'],
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred for {city}: {http_err}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Connection error for {city}: {e}")
    
    return None

if __name__ == "__main__":
    # Test the client (Replace 'YOUR_API_KEY_HERE' with your real key)
    API_KEY = "ad503637bed31485acc25d2a0af5ea87" 
    sample_data = fetch_weather_data(API_KEY, "London")
    if sample_data:
        print(f"✅ Success! Current temp in London: {sample_data['temp']}°C")