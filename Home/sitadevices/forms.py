from django import forms
from . models import Customer


class CustomerInp(forms.ModelForm):
    class Meta:
        model=  Customer
        fields='__all__'
        exclude = ['submitted_date_time',]