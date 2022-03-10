from django.db import models
from django.utils import timezone

# Create your models here.





class Vlan(models.Model):
    vlan_desc = models.TextField()
    static_ip_conf = models.CharField(max_length=50)
    static_ip_addr = models.CharField(max_length=100)
    internal_ip_config = models.CharField(max_length=100)
    internal_ip_range = models.CharField(max_length=100)
    additional_conf = models.TextField()
    submitted_date_time = models.DateTimeField(default=timezone.now)
    

class Switch(models.Model):
    switch_name = models.CharField(max_length=200)
    switch_model = models.CharField(max_length=100)
    configuration = models.TextField()
    vlan = models.ForeignKey(Vlan, on_delete=models.CASCADE, blank=True, null=True)

    

class Port(models.Model):
    port_number = models.IntegerField()
    port_desc = models.TextField()
    associate = models.CharField(max_length=200)
    # uuid = models.CharField(max_length=200)
    status = models.BooleanField()
    submitted_date_time = models.DateTimeField(default=timezone.now)
    switch = models.ForeignKey(Switch, on_delete= models.CASCADE)


# class Room(models.Model):
#     room = models.CharField(max_length=255)

# class Building(models.Model):
#     room = models.ManyToManyField(Room)
#     building_desc = models.TextField()

# class CommmunicationRoom(models.Model):
#     building_code = models.ForeignKey(Building, on_delete=models.CASCADE)
#     commroomname = models.CharField(max_length=255)
