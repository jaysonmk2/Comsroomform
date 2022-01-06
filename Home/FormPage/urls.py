from django.urls import path
from .views import FormPage,ThanksPage, AdminPage, Active, Pending, Eliminated, ViewUser
from django.conf import settings
from django.conf.urls.static import static


app_name =  'Form'
urlpatterns = [
    path('', FormPage, name="Home"),
    path('thanks', ThanksPage, name="thanks"),
    path('admin-page', AdminPage, name="adminpage"),
    path('admin-page/active', Active, name="active"),
    path('admin-page/pending', Pending, name="pending"),
    path('admin-page/eliminated', Eliminated, name="eliminated"),
    path('<int:form_id>',ViewUser, name='user' )
]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
