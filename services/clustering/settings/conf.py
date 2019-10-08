import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOCATION_URL = os.environ.get("LOCATION_URL",  'http://location:5050')
