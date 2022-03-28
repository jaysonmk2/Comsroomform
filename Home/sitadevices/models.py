from django.db import models
from django.utils import timezone

# Create your models here.


yesno = [
        ('YES', 'yes'),
        ('NO', 'no'),
]

class Customer(models.Model):
    company_name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.IntegerField()
    active = models.CharField(choices=yesno, max_length=200)
    submitted_date_time = models.DateTimeField(default=timezone.now)

# class Room(models.Model):
#     room = models.CharField(max_length=255)

# class Building(models.Model):
#     room = models.ManyToManyField(Room)
#     building_desc = models.TextField()

# class CommmunicationRoom(models.Model):
#     building_code = models.ForeignKey(Building, on_delete=models.CASCADE)
#     commroomname = models.CharField(max_length=255)
