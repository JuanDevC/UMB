
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ 
    path("sitios/", views.sitios_interes, name="Sitios"),
]


#https://www.latlong.net/convert-address-to-lat-long.html