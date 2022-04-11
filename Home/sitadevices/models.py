from django.db import models
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
        ('DOWN', 'down'),
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
        company_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
        vlan_number = models.ForeignKey(CustomerVlan, on_delete=models.CASCADE)
        submitted_date_time = models.DateTimeField(default=timezone.now)



class Connections(models.Model):
    company = models.ForeignKey(Customer, on_delete=models.CASCADE)
    customerVlan = models.ForeignKey(CustomerVlan, on_delete=models.CASCADE)


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

class DataOutlet(models.Model):
    connection = models.ForeignKey(Connections, on_delete=models.CASCADE)
    comroom= models.ForeignKey(CommmunicationRoom, on_delete=models.CASCADE)
    patch_panel = models.IntegerField()
    port_status =models.CharField(choices=status, max_length=200)
    data_number = models.IntegerField(default=1)
