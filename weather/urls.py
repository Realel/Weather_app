from django.urls import path
from . import views

urlpatterns = [
    path('', views.weather_view, name='home'),
]
# dd2f0cfb6001141c51df338c1d548d42