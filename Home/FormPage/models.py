from datetime import time
from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields import BLANK_CHOICE_DASH, CharField
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


RequestAccessChoices = [
        ('PERMANENT', 'Permanent'),
        ('TEMPORARY', 'Temporary'),
]

ApprovedOrNot = [
        ('APPROVED', 'Approve'),
        ('REJECT', 'Reject'),
]


class MainCommunicationRoom(models.Model):
    room_name = models.CharField(max_length=100)
    submitted_date_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.room_name

class NewTerminalBuilding(models.Model):
    NTB_code = models.CharField(max_length=100)
    NTB_number = models.IntegerField()
    submitted_date_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.NTB_code

class OldTerminalBuilding(models.Model):
    OTB_code = models.CharField(max_length=100)
    OTB_name = models.CharField(max_length=100)
    submitted_date_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.OTB_name

class OtherBuilding(models.Model):
    building_name = models.CharField(max_length=100)
    submitted_date_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.building_name

class Form(models.Model):
    company_name = models.CharField(max_length=200, null=False, blank=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    AIB_number = models.CharField(max_length=100)
    position_title = models.CharField(max_length=200)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    job_duties = models.TextField() 
    access_justification = models.TextField()
    wap_roa = models.CharField(max_length=255)
    required_access = models.CharField(choices=RequestAccessChoices, max_length=200)
    start_time = models.DateField(blank=True, null=True)
    end_time = models.DateField(blank=True, null=True)
    main_communications_room = models.ManyToManyField(MainCommunicationRoom, blank=True)
    new_terminal_building = models.ManyToManyField(NewTerminalBuilding, blank=True)
    old_terminal_building = models.ManyToManyField(OldTerminalBuilding, blank=True)
    building = models.ManyToManyField(OtherBuilding, blank=True)
    other_locations = models.TextField(blank=True )
    specify_system_list = models.TextField(blank=True)
    specify_equipment_list = models.TextField(blank=True)
    specify_server_list = models.TextField(blank=True)
    Specify_cables = models.TextField(blank=True)
    agreed_to_terms = models.BooleanField(default=False)
    submitted_date_time = models.DateTimeField(default=timezone.now)
    approved_or_not = models.CharField(choices=ApprovedOrNot, max_length=200, blank=True, null=True)
    
    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.last_name

    


class FormFiles(models.Model):
    files = models.FileField(upload_to = "uploaded_files", null=True, blank=True)
    form_fk = models.ForeignKey(Form, on_delete=models.CASCADE, null=True, blank=True)