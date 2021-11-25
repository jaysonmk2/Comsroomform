from django import forms
from django.db.models import fields
from django.db.models.fields import BooleanField
from django.forms.widgets import DateInput
from .models import Form, FormFiles


class Form(forms.ModelForm):

    class Meta:
        model=Form
        fields='__all__'
        exclude = ['submitted_date_time']
        error_css_class = 'error'
        required_css_class = 'required'
      
        widgets = {
            'main_communications_room' : forms.CheckboxSelectMultiple(attrs={'class':'checkbox'}),
            'new_terminal_building':forms.CheckboxSelectMultiple(attrs={'class':'checkbox'}),
            'old_terminal_building': forms.CheckboxSelectMultiple(attrs={'class':'checkbox'}),
            'building': forms.CheckboxSelectMultiple(attrs={'class':'checkbox'}),
            'start_time':forms.DateInput(attrs={'type': 'date'}),
            'end_time':forms.DateInput(attrs={'type': 'date'}),
            'agreed_to_terms': forms.CheckboxInput(attrs={'required':True})
        }

class FileInput(forms.ModelForm):

    class Meta:
        model = FormFiles
        fields = '__all__'

        widgets ={
            'files': forms.ClearableFileInput(attrs={'multiple':True}),
        }