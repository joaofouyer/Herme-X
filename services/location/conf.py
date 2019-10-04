import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GOOGLE_GEOCODING = os.environ.get("GOOGLE_GEOCODING")
GOOGLE_DIRECTIONS = os.environ.get("GOOGLE_DIRECTIONS")
BING_KEY = os.environ.get("BING_KEY")
HERE_ID = os.environ.get("HERE_ID")
HERE_CODE = os.environ.get("HERE_CODE")
MAPBOX_KEY = os.environ.get("MAPBOX_KEY")
MAPQUEST_KEY = os.environ.get("MAPQUEST_KEY")
OPENCAGE_KEY = os.environ.get("OPENCAGE_KEY")
LOCATIONIQ_KEY = os.environ.get("LOCATIONIQ_KEY")
URL = os.environ.get("URL", "http: // location: 5050 /")
DB_NAME = os.environ.get("DB_NAME", 'location')
DB_USER = os.environ.get("DB_USER", 'hermex')
DB_PASS = os.environ.get("DB_PASS", 'fe9941445a1e8a693e0335e8200417ec')
DB_ADDR = os.environ.get("DB_ADDR",  'db')
DB_PORT = os.environ.get("DB_PORT",  '5432')
