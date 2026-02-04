import requests
from Backend.config import MAPBOX_API_KEY

def optimize_route(coords_list, profile = "walking"):
    """Optimize a running route using Mapbox Optimization API."""
    if len(coords_list) < 2:
        raise ValueError("At least two coordinates are required to optimize a route.")
    
    coords_str = ";".join([f"{lng},{lat}" for lat, lng in coords_list])

    url = f"https://api.mapbox.com/optimized-trips/v1/mapbox/{profile}/{coords_str}.json"

    params = {
        "access_token": MAPBOX_API_KEY,
        "geometries": "geojson",
        "overview": "full",
        "roundtrip": "true"
    }
    
    response = requests.get(url, params=params) #Make a GET request to the Mapbox Optimization API, Also includes parameters for the request

    if response.status_code != 200: #makes sure the response is valid
        raise Exception(f"Error optimizing route: {response.status_code}, {response.text}")
    
    data = response.json() #Parse the JSON response

    if not data['trips']:
        raise ValueError("No optimized trip found for the given coordinates.")
    
    trip = data['trips'][0]
    distance = trip['distance'] #Extract the distance of the optimized trip
    duration = trip['duration'] #Extract the duration of the optimized trip
    geometry = trip['geometry']["coordinates"] #Extract the geometry of the optimized trip and its coordinates
    waypoint_order = trip.get('waypoint_order', list(range(len(coords_list)))) #Get the ordered waypoints based on the optimized trip
    ordered_waypoints = [coords_list[i] for i in waypoint_order] #Reorder the original coordinates based on the optimized order

    return {
        "distance": distance,
        "duration": duration,
        "geometry": geometry,
        "ordered_waypoints": ordered_waypoints
    }
