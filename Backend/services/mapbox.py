import requests #Import requests library for HTTP requests
from Backend.config import MAPBOX_API_KEY #Import the API key from config

def geocode_location(place_name: str): 
    """Geocode a place name to coordinates using Mapbox API."""
    url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{place_name}.json" #Mapbox Geocoding API endpoint. {Place_name} is the location to geocode.
    params = {
        "access_token": MAPBOX_API_KEY,
        "limit": 1. #Gets only the top result
    }

    response = requests.get(url, params=params) #Make a GET request to the Mapbox API with the URL and parameters

    if response.status_code != 200:
        raise Exception(f"Error geocoding location: {response.status_code}, {response.text}") #Raise an exception if the response status code is not 200 (OK)

    data = response.json() #Parse the JSON response (Convert the response to a Python dictionary)

    if not data['features']:
        raise ValueError("Location not found.") #Raise an exception if no features are found in the response
    
    longitude, latitude = data['features'][0]['center'] #Extract longitude and latitude from the first feature in the response

    return latitude, longitude #Return the latitude and longitude as a tuple

def get_route(start_coords, end_coords):
    """Get a running route between two coordinates using Mapbox Directions API."""
    url = f"https://api.mapbox.com/directions/v5/mapbox/walking/{start_coords[1]},{start_coords[0]};{end_coords[1]},{end_coords[0]}" #Mapbox Directions API endpoint for walking routes
    params = {
        "access_token": MAPBOX_API_KEY, #API access token
        "geometries": "geojson", #Request the route geometry in GeoJSON format
        "overview": "full" #Request the full overview of the route
    }

    response = requests.get(url, params=params) #Make a GET request to the Mapbox Directions API

    if response.status_code != 200:
        raise Exception(f"Error fetching route: {response.status_code}, {response.text}") #Raise an exception if the response status code is not 200 (OK)
    
    data = response.json() #Parse the JSON response

    if not data['routes']:
        raise ValueError("No route found between the specified coordinates.") #Raise an exception if no routes are found in the response
    
    route = data['routes'][0]
    distance = route['distance'] #Extract the distance of the route
    duration = route['duration'] #Extract the duration of the route
    geometry = route['geometry']["coordinates"] #Extract the geometry of the route and its coordinates
    return {
        "distance": distance,
        "duration": duration,
        "geometry": geometry
    }