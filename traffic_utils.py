import requests

def get_coordinates(location, api_key):
    """Convert a location name into latitude & longitude using TomTom Geocoding API."""
    url = f"https://api.tomtom.com/search/2/geocode/{location}.json?key={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data["results"]:
            lat = data["results"][0]["position"]["lat"]
            lon = data["results"][0]["position"]["lon"]
            return lat, lon
    return None

def get_traffic_flow_data(lat, lon, api_key):
    """Fetch real-time traffic flow data from TomTom API."""
    url = f"https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json?point={lat},{lon}&unit=KMPH&key={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    return None
