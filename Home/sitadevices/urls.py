from django.urls import path
from . views import DeviceHome, SwitchForm


app_name = 'device'

urlpatterns =[
    path('',DeviceHome, name="deviceHome"),
    path('switchInp', SwitchForm, name='switchInp')
]