from django.urls import path
from .views import FormPage,ThanksPage



app_name =  'Form'
urlpatterns = [
    path('', FormPage, name="Home"),
    path('thanks', ThanksPage, name = "thanks")
]
