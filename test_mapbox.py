#Just a testing file to trigger recent edits
from Backend.services.mapbox import geocode_location, get_route
print("This is a test file for recent edits.")

location = "Columbus, Ohio"
lat, lng = geocode_location(location)

print(f"{location} = Latitude: {lat}, Longitude: {lng}")

start = "Columbus, Ohio"
end = "Downtown, Columbus, Ohio"

start_coords = geocode_location(start)
end_coords = geocode_location(end)

print(f"Start coordinates: {start_coords}")
print(f"End coordinates: {end_coords}")

distance, duration, geometry = get_route(start_coords, end_coords).values()
print("\nRoute Info:")
print(f"Route distance: {distance} meters")
print(f"Route duration: {duration} seconds")
print(f"Route geometry: {geometry[:5]}...")  # Print first 5 coordinates of the route
