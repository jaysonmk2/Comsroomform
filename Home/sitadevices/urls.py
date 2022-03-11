from django.urls import path
from . views import DeviceHome, SwitchForm, SwitchViews, SwitchIndividualView


app_name = 'device'

urlpatterns =[
    path('',DeviceHome, name="deviceHome"),
    path('switchInp', SwitchForm, name='switchInp'),
    path('switchlist', SwitchViews, name='switchlist'),
    path('<int:switch_id>', SwitchIndividualView, name='individualswitch')
]