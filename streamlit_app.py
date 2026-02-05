import streamlit as st
from Backend.algorithms.optimizer import optimize_route
from Backend.services.mapbox import geocode_location, get_route

st.title("Running Route Optimizer")
st.write("Optimize your running routes using Mapbox's powerful APIs.")
place_name = st.text_input("Enter a location to geocode:")
if place_name:
    try:
        lat, lng = geocode_location(place_name)
        st.write(f"Coordinates for {place_name}: Latitude {lat}, Longitude {lng}")

        start_coords = (lat, lng)
        end_coords = (lat + 0.01, lng + 0.01)  # Example end coordinates for demonstration

        route = get_route(start_coords, end_coords)
        st.write(f"Route Distance: {route['distance']} meters")
        st.write(f"Route Duration: {route['duration']} seconds")

        coords_list = [start_coords, end_coords]
        optimized_route = optimize_route(coords_list)

        st.write("Optimized Route:")
        st.write(f"Distance: {optimized_route['distance']} meters")
        st.write(f"Duration: {optimized_route['duration']} seconds")
        st.write(f"Ordered Waypoints: {optimized_route['ordered_waypoints']}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
        