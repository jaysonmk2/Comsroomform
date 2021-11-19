from django.urls import path
from .views import FormPage



app_name =  'Form'
urlpatterns = [
    path('', FormPage, name = "Home")
]
