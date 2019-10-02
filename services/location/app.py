import falcon
from geocoding import Geocoding


api = falcon.API()
geocoding = Geocoding()
api.add_route('/geocoder/address={address}', geocoding)
api.add_route('/geocoder/latlng={latlng}', geocoding)
api.add_route('/geocoder/', geocoding)
