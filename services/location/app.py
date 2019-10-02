import falcon
from geocoding import Geocoding
from travel_time import TravelTime

api = falcon.API()
geocoding = Geocoding()
travel_time = TravelTime()

api.add_route('/geocoder/address={address}', geocoding)
api.add_route('/geocoder/latlng={latlng}', geocoding)
api.add_route('/geocoder/', geocoding)

api.add_route('/ett/', travel_time)
api.add_route('/ett/origin={origin}&destination={destination}', travel_time)
api.add_route('/ett/origin={origin}&destination={destination}/departure={departure}', travel_time)
api.add_route('/ett/origin={origin}&destination={destination}/arrival={arrival}', travel_time)
