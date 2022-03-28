from django.urls import path
from . views import DeviceHome, CustomerViews,CustomerInput,CustomerInd,CustomerDel,CustomerUpd


app_name = 'device'

urlpatterns =[
    path('',DeviceHome, name="deviceHome"),
    path('customers', CustomerViews, name='customerlist'),
    path('customerinp', CustomerInput, name='customerinp'),
    path('<int:customer_id>', CustomerInd, name='customerind'),
    path('del/<int:customer_id>', CustomerDel, name='customerdel'),
    path('upd/<int:customer_id>', CustomerUpd, name='customerupd')
]