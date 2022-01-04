from django.contrib import admin
from .models import MainCommunicationRoom,OldTerminalBuilding,NewTerminalBuilding,OtherBuilding,Form,FormFiles
# Register your models here.



class MainCommunicationRoomAdmin(admin.ModelAdmin):
    list_display= ('room_name',)

class OldTerminalBuildingAdmin(admin.ModelAdmin):
    list_display=('OTB_code','OTB_name',)

class NewTerminalBuildingAdmin(admin.ModelAdmin):
    list_display=('NTB_code', 'NTB_number',)

class OtherBuildingAdmin(admin.ModelAdmin):
    list_display=('building_name',)

class FormAdmin(admin.ModelAdmin):
    list_display=('company_name','first_name','last_name','AIB_number','telephone','required_access',)
    search_fields = (
        'first_name',
        'last_name',
        'company_name',
        'required_access',
    )


admin.site.register(MainCommunicationRoom,MainCommunicationRoomAdmin)
admin.site.register(OldTerminalBuilding,OldTerminalBuildingAdmin)
admin.site.register(NewTerminalBuilding, NewTerminalBuildingAdmin)
admin.site.register(OtherBuilding, OtherBuildingAdmin)
admin.site.register(Form,FormAdmin)
admin.site.register(FormFiles)

