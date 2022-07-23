from django.contrib import admin

# Register your models here.
from .models import WorkOrder,Connections
# Register your models here.



class WorkOrderAdmin(admin.ModelAdmin):
    list_display= ('request_date','company_id','connections','request_type',)

admin.site.register(WorkOrder,WorkOrderAdmin)

class ConnectionsAdmin(admin.ModelAdmin):
    list_display= ('company','switch_port_number','actual_user','status',)

admin.site.register(Connections,ConnectionsAdmin)
