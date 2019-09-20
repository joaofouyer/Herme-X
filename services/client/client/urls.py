from django.contrib import admin
from django.urls import path, include
from application.routes import passenger_urls, index_urls, driver_urls, line_urls, manager_urls, stop_urls, vehicle_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('passageiro', include(passenger_urls.urlpatterns)),
    path('motorista', include(driver_urls.urlpatterns)),
    path('rota', include(line_urls.urlpatterns)),
    path('funcionario', include(manager_urls.urlpatterns)),
    path('ponto', include(stop_urls.urlpatterns)),
    path('veiculo', include(vehicle_urls.urlpatterns)),
    path('', include(index_urls.urlpatterns))
]
