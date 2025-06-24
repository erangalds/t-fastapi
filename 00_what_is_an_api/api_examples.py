# To run this code, you first need to install the 'requests' library.
# In your terminal, run: pip install requests

import requests

def get_fake_post():
    """
    Example 1: Using JSONPlaceholder to get a single fake blog post.
    JSONPlaceholder is a great free API for testing and prototyping.
    """
    print("--- Example 1: Fetching a single blog post ---")
    
    # The API endpoint is the URL we want to get data from.
    # Here, we are asking for the post with an ID of 1.
    endpoint = "https://jsonplaceholder.typicode.com/posts/1"
    
    try:
        # We use requests.get() to send a GET request to the endpoint.
        response = requests.get(endpoint)
        
        # Good practice: check if the request was successful.
        # A status code of 200 means "OK". This line will raise an error for bad responses (4xx or 5xx)
        response.raise_for_status() 
        
        # The response from the API is usually in JSON format.
        # We can use .json() to parse it into a Python dictionary.
        post_data = response.json()
        
        print(f"Successfully fetched post with ID: {post_data.get('id')}")
        print(f"Title: {post_data.get('title')}")
        print("-" * 40)
        
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def get_sunrise_sunset_time():
    """
    Example 2: Using Sunrise Sunset API to get sunrise and sunset times for a specific location.
    This API provides interesting real-world data based on geographical coordinates.
    """
    print("\n--- Example 2: Fetching sunrise and sunset times for London ---")
    
    # API endpoint for Sunrise Sunset API.
    # We'll use London's latitude and longitude as an example.
    endpoint = "https://api.sunrise-sunset.org/json"

    # Parameters for London.
    # You can change these to get sunrise/sunset times for different locations.
    params = {
        "lat": 51.5074,  # Latitude of London
        "lng": 0.1278,   # Longitude of London
        "formatted": 0  # We want the times in UTC ISO 8601 format
    }

    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        data = response.json()
        results = data.get('results', {})
        print(f"Sunrise: {results.get('sunrise')}")
        print(f"Sunset: {results.get('sunset')}")
        print("-" * 40)
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def get_current_weather():
    """
    Example 3: Using Open-Meteo API to get the current weather for a location.
    This shows how to use query parameters to send specific data (latitude/longitude).
    """
    print("\n--- Example 3: Getting the current weather for Berlin ---")
    
    base_endpoint = "https://api.open-meteo.com/v1/forecast"
    
    # We provide parameters to specify the location and what data we want.
    # This is like asking the waiter for "the current temperature for Berlin".
    params = {
        "latitude": 52.52,
        "longitude": 13.41,
        "current_weather": "true"
    }
    
    try:
        response = requests.get(base_endpoint, params=params)
        response.raise_for_status()
        data = response.json()
        
        # The data is nested, so we access it step-by-step.
        current_weather = data.get('current_weather', {})
        temperature = current_weather.get('temperature')
        windspeed = current_weather.get('windspeed')
        
        print(f"Successfully fetched weather for Berlin.")
        print(f"Current Temperature: {temperature}°C")
        print(f"Current Windspeed: {windspeed} km/h")
        print("-" * 40)
        
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    get_fake_post()
    get_sunrise_sunset_time()
    get_current_weather()