from django import forms
from . models import Switch, Port


class SwitchInp(forms.ModelForm):
    class Meta:
        model=Switch
        fields='__all__'
        exclude = ['submitted_date_time',]