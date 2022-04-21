from django.db import models
from django.forms import DateField
from django.utils import timezone

# Create your models here.


yesno = [
        ('YES', 'yes'),
        ('NO', 'no'),
]

usages = [
        ('ACCESS', 'access'),
        ('VOICE', 'voice'),
]

ip = [
        ('STATIC', 'static'),
        ('DHCP', 'dhcp'),
]

status = [
        ('ACTIVE', 'active'),
        ('DISABLED', 'disabled'),
]

requestType = [
        ('CONFIGURE', 'configure'),
        ('MODIFY', 'modify'),
        ('DISCONNECT', 'disconnect'),
        ('RESET','reset')
]
workOrderStatus = [
        ('CONFIGURE', 'configure'),
        ('MODIFY', 'modify'),
        ('DISCONNECT', 'disconnect'),
        ('RESET','reset')
]
duplex = [
        ('HALF', 'half'),
        ('FULL', 'full'),
        ('AUTO', 'auto'),  
]

class Customer(models.Model):
    company_name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.IntegerField()
    active = models.CharField(choices=yesno, max_length=200)
    submitted_date_time = models.DateTimeField(default=timezone.now)


class CustomerVlan(models.Model):
    custumor = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vlan_number = models.IntegerField()
    usage = models.CharField(choices=usages, max_length=200)
    config_date = models.DateTimeField()
    vlan_description = models.TextField()
    ip_config = models.CharField(choices=ip, max_length=200)
    dhcp_ip_range = models.CharField(max_length=50)
    lan_ip_range = models.CharField(max_length=50)
    lan_subnet_mask = models.CharField(max_length=50)
    wan_public_ip = models.CharField(max_length=50)
    wan_subnet_mask = models.CharField(max_length=50)
    bandwidth = models.IntegerField()
    additional_config = models.TextField()
    remark = models.TextField()
    disconnection_date = models.DateField(null=True, blank=True)
    submitted_date_time = models.DateTimeField(default=timezone.now)


class WorkOrder(models.Model):
    work_order_date = models.DateTimeField(default=timezone.now)
    request_date = models.DateField(default=timezone.now)
    service_desk_ticket_number = models.CharField(max_length=200,default="none")
    request_type = models.CharField(choices=requestType, max_length=200,default="none")
    request_description = models.TextField(default="none")
    configuration_remark = models.TextField(default="none")
    comment = models.TextField(default="none")
    engineer_assigned = models.CharField(max_length=200,default="none")
    company_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vlan_number = models.ForeignKey(CustomerVlan, on_delete=models.CASCADE)
    submitted_date_time = models.DateTimeField(default=timezone.now)



class Connections(models.Model):
    company = models.ForeignKey(Customer, on_delete=models.CASCADE)
    customerVlan = models.ForeignKey(CustomerVlan, on_delete=models.CASCADE)
    switch_port_number = models.IntegerField(default=0)
    duplex = models.CharField(choices=duplex, max_length=200,default="none")
    voice_vlan_number = models.IntegerField(default=0)
    phone_mac_address = models.CharField(max_length=200,default="none")
    phone_extension = models.CharField(max_length=200,default="none")
    purpose = models.TextField(default="none")
    sticky_port = models.CharField(choices=yesno, max_length=200,default="none")
    additional_configuration = models.TextField(default="none")
    remark = models.TextField(default="none")
    actual_user = models.CharField(max_length=200,default="none")
    status = models.CharField(choices= status, max_length=200,default="none")
    connection_date = models.DateField(default=timezone.now)
    disconnection_date = models.DateField(default=timezone.now)

class Building(models.Model):
    building_desc = models.TextField()

class Room(models.Model):
    room = models.CharField(max_length=255)
    building_code = models.ForeignKey(Building, on_delete=models.CASCADE)

class CommmunicationRoom(models.Model):
    building_code = models.ForeignKey(Building, on_delete=models.CASCADE)
    commroomname = models.CharField(max_length=255)


class Switch(models.Model):
    comms_room = models.ForeignKey(CommmunicationRoom, on_delete=models.CASCADE)
    switch_name = models.CharField(max_length=200,default="none")
    model = models.CharField(max_length=200,default="none")
    brand = models.CharField(max_length=200,default="none")
    port_capacity = models.CharField(max_length=200,default="none")
    owner = models.CharField(max_length=200,default="none")
    supplier = models.CharField(max_length=200,default="none")
    brand = models.CharField(max_length=200,default="none")
    poe_enabled = models.CharField(choices=yesno, max_length=200,default="none")
    rach_number = models.CharField(max_length=200,default="none")
    purchase_date = models.DateField(default=timezone.now)
    status = models.CharField(choices=status, max_length=200,default="none")

class DataOutlet(models.Model):
    connection = models.ForeignKey(Connections, on_delete=models.CASCADE)
    comroom= models.ForeignKey(CommmunicationRoom, on_delete=models.CASCADE)
    patch_panel = models.IntegerField()
    port_status =models.CharField(choices=status, max_length=200)
    data_number = models.IntegerField(default=1)
