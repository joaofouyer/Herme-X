import falcon
from geocoding import Geocoding
from travel_time import TravelTime
from distance import Distance

api = falcon.API()
geocoding = Geocoding()
travel_time = TravelTime()
distance = Distance()

api.add_route('/geocoder/address={address}', geocoding)
api.add_route('/geocoder/latlng={latlng}', geocoding)
api.add_route('/geocoder/', geocoding)

api.add_route('/ett/', travel_time)
api.add_route('/ett/origin={origin}&destination={destination}', travel_time)
api.add_route('/ett/origin={origin}&destination={destination}/departure={departure}', travel_time)
api.add_route('/ett/origin={origin}&destination={destination}/arrival={arrival}', travel_time)

api.add_route('/distance/', distance)
api.add_route('/distance/origin={origin}&destination={destination}', distance)
api.add_route('/distance/{mode}/origin={origin}&destination={destination}', distance)
