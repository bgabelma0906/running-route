import os
from dotenv import load_dotenv

load_dotenv()

MAPBOX_API_KEY = os.getenv("MAPBOX_API_KEY")

print("Mapbox key loaded.", MAPBOX_API_KEY is not None)