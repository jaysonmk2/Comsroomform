from django.urls import path
from .views import FormPage,ThanksPage, AdminPage, Active, Pending, Eliminated, ViewUser, MasterAdmin,FormUpd
from django.conf import settings
from django.urls.conf import include
from django.conf.urls.static import static


app_name =  'Form'
urlpatterns = [
    path('', FormPage, name="Home"),
    path('thanks', ThanksPage, name="thanks"),
    path('admin-page', AdminPage, name="adminpage"),
    path('admin-page/active', Active, name="active"),
    path('admin-page/pending', Pending, name="pending"),
    path('admin-page/eliminated', Eliminated, name="eliminated"),
    path('<int:form_id>',ViewUser, name='user' ),
    path('admin-page/formupdate/<int:user_detail_id>', FormUpd, name="formupd"),

    path('master', MasterAdmin, name='master')
]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
