from django.db import models

# Create your models here.






class Port(models.Model):
    port_number = models.IntegerField()
    port_desc = models.TextField()
    associate = models.CharField(max_length=200)
    uuid = models.CharField(max_length=200)
    status = models.BooleanField()

# class Room(models.Model):
#     room = models.CharField(max_length=255)

# class Building(models.Model):
#     room = models.ManyToManyField(Room)
#     building_desc = models.TextField()

# class CommmunicationRoom(models.Model):
#     building_code = models.ForeignKey(Building, on_delete=models.CASCADE)
#     commroomname = models.CharField(max_length=255)
