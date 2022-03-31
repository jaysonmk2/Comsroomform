from django.urls import path
from . views import *


app_name = 'device'

urlpatterns =[
    path('',DeviceHome, name="deviceHome"),
    path('customers', CustomerViews, name='customerlist'),
    path('customerinp', CustomerInput, name='customerinp'),
    path('<int:customer_id>', CustomerInd, name='customerind'),
    path('del/<int:customer_id>', CustomerDel, name='customerdel'),
    path('upd/<int:customer_id>', CustomerUpd, name='customerupd'),


    path('customerVlan', CustomerVlans, name="customerVlanlist"),
    path('customerVlaninp', CustomerVlanInput, name='customerVlaninp'),
    path('vlan/<int:customerVlan_id>', CustomerVlanInd, name='customerVlanind'),
    path('del/vlan/<int:customerVlan_id>', CustomerVlanDel, name='customerVlandel'),
    path('upd/vlan/<int:customerVlan_id>', CustomerVlanUpd, name='customerVlanupd'),


    path('workorder', WorkOrders, name="workorderlist"),
    path('workorderinp', WorkOrderInput, name='workorderinp'),
    path('workorder/<int:workorder_id>', WorkOrderInd, name='workorderind'),
    path('del/workorder/<int:workorder_id>', WorkOrderDel, name='workorderdel'),
    path('upd/workorder/<int:workorder_id>', WorkOrderUpd, name='workorderupd'),

    path('locations', Location, name="locationlist"),

    path('buildinginp', BuildingInput, name='buildinginp'),
    path('del/building/<int:building_id>', BuildingDel, name='buildingdel'),
    path('upd/building/<int:building_id>', BuildingUpd, name='buildingupd'),

    path('officeinp', OfficeInput, name='officeinp'),
    path('del/office/<int:office_id>', OfficeDel, name='officedel'),
    path('upd/office/<int:office_id>', OfficeUpd, name='officeupd'),

    path('commsinp', CommsInput, name='comsinp'),
    path('del/commsroom/<int:comms_id>', CommsDel, name='commsdel'),
    path('upd/commsroom/<int:comms_id>', CommsUpd, name='commsupd'),

]