from django import forms
from . models import Customer,CustomerVlan, WorkOrder, Room,CommmunicationRoom,Building, Connections, Switch


class CustomerInp(forms.ModelForm):
    class Meta:
        model=  Customer
        fields='__all__'
        exclude = ['submitted_date_time',]

class CustomerVlanInp(forms.ModelForm):
    class Meta:
        model=  CustomerVlan
        fields='__all__'
        exclude = ['submitted_date_time',]
    
        widgets = {
            'disconnection_date':forms.DateInput(attrs={'type': 'date'}),
            'config_date':forms.DateInput(attrs={'type': 'date'}),
        }


class WorkOrderInp(forms.ModelForm):
    class Meta:
        model=  WorkOrder
        fields='__all__'
        exclude = ['submitted_date_time','vlan_number']


class BuildingForm(forms.ModelForm):
    class Meta:
        model=  Building
        fields='__all__'

class OfficeForm(forms.ModelForm):
    class Meta:
        model=  Room
        fields='__all__'

class CommsForm(forms.ModelForm):
    class Meta:
        model=  CommmunicationRoom
        fields='__all__'

class ConnectionsForm(forms.ModelForm):
    class Meta:
        model=  Connections
        fields='__all__'

class SwitchForm(forms.ModelForm):
    class Meta:
        model=  Switch
        fields='__all__'