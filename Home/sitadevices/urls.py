from django.urls import path
from . views import DeviceHome


app_name = 'device'

urlpatterns =[
    path('',DeviceHome, name="deviceHome")
]