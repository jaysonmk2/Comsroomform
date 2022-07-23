from sqlite3 import Connection
from django.db import models
from django.forms import DateField
from django.utils import timezone
from smart_selects.db_fields import ChainedForeignKey


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

    def __str__(self):
        return self.company_name


class CustomerVlan(models.Model):
    customor = models.ForeignKey(Customer, on_delete=models.CASCADE)
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

    def __str__(self):
        return str(self.vlan_number)


class Building(models.Model):
    building_desc = models.TextField()

    def __str__(self):
        return self.building_desc

class Room(models.Model):
    room = models.CharField(max_length=255)
    building_code = models.ForeignKey(Building, on_delete=models.CASCADE)

    def __str__(self):
        return self.room

class CommmunicationRoom(models.Model):
    building_code = models.ForeignKey(Building, on_delete=models.CASCADE)
    commroomname = models.CharField(max_length=255)

    def __str__(self):
        return self.commroomname



class DataOutlet(models.Model):
    comroom= models.ForeignKey(CommmunicationRoom, on_delete=models.CASCADE)
    patch_panel = models.IntegerField()
    port_status =models.CharField(choices=status, max_length=200)
    office_number = models.ForeignKey(Room, on_delete=models.CASCADE)
    

class Connections(models.Model):
    company = models.ForeignKey(Customer, on_delete=models.CASCADE)
    customerVlan = models.ForeignKey(CustomerVlan, on_delete=models.CASCADE)
    data_outlet = models.ForeignKey(DataOutlet, on_delete=models.CASCADE,null=True, blank=True)
    switch_port_number = models.IntegerField(default=0)
    duplex = models.CharField(choices=duplex, max_length=200)
    voice_vlan_number = models.IntegerField(default=0)
    phone_mac_address = models.CharField(max_length=200)
    phone_extension = models.CharField(max_length=200)
    purpose = models.TextField()
    sticky_port = models.CharField(choices=yesno, max_length=200)
    additional_configuration = models.TextField()
    remark = models.TextField()
    actual_user = models.CharField(max_length=200)
    status = models.CharField(choices= status, max_length=200)
    connection_date = models.DateField(default=timezone.now)
    disconnection_date = models.DateField(default=timezone.now,null=True, blank=True)

    def __str__(self):
        return self.actual_user

    

class WorkOrder(models.Model):
    work_order_date = models.DateTimeField(default=timezone.now)
    request_date = models.DateField(default=timezone.now)
    company_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    connections= ChainedForeignKey(
        Connections,
        chained_field="company_id",
        chained_model_field="company",
        show_all=False,
        auto_choose=True,
        sort=True)
    service_desk_ticket_number = models.CharField(max_length=200)
    request_type = models.CharField(choices=requestType, max_length=200)
    request_description = models.TextField()
    configuration_remark = models.TextField()
    comment = models.TextField()
    engineer_assigned = models.CharField(max_length=200)
    vlan_number = models.ForeignKey(CustomerVlan, on_delete=models.CASCADE)
    submitted_date_time = models.DateTimeField(default=timezone.now)
    
    
    




class Switch(models.Model):
    communication_room = models.ForeignKey(CommmunicationRoom, on_delete=models.CASCADE)
    switch_name = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    port_capacity = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)
    supplier = models.CharField(max_length=200) 
    poe_enabled = models.CharField(choices=yesno, max_length=200)
    rack_number = models.CharField(max_length=200)
    purchase_date = models.DateField(default=timezone.now)
    status = models.CharField(choices=status, max_length=200)

    def __str__(self):
        return self.switch_name




