from django.urls import path
from .views import FormPage,ThanksPage, AdminPage, Active, Pending, Eliminated



app_name =  'Form'
urlpatterns = [
    path('', FormPage, name="Home"),
    path('thanks', ThanksPage, name="thanks"),
    path('admin-page', AdminPage, name="adminpage"),
    path('admin-page/active', Active, name="active"),
    path('admin-page/pending', Pending, name="pending"),
    path('admin-page/eliminated', Eliminated, name="eliminated"),
]
