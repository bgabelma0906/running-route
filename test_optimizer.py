from Backend.services.mapbox import geocode_location
from Backend.algorithms.optimizer import optimize_route

locations = [
    "Central Park, NY",
    "Times Square, NY",
    "Empire State Building, NY",
    "Grand Central Terminal, NY",
    "Bryant Park, NY"
]

coords = [geocode_location(loc) for loc in locations]

result = optimize_route(coords, profile="walking")

print("Optimized order of coordinates:", result['ordered_waypoints'])
print("Total distance (meters):", result['distance'])
print("Total duration (seconds):", result['duration'])
print("First 5 route coordinates:", result['geometry'][:5])

