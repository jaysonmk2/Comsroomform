from django.urls import path
from .views import FormPage,ThanksPage, AdminPage, Filtered



app_name =  'Form'
urlpatterns = [
    path('', FormPage, name="Home"),
    path('thanks', ThanksPage, name="thanks"),
    path('admin-page', AdminPage, name="adminpage"),
    path('filtered', Filtered, name="hello"),
]
