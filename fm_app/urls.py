from django.urls import path
from .views import all_station,home,country_list



urlpatterns =[
    path('', home,name="home"),
    path('stations/',all_station),
    path('countries/', country_list),
]