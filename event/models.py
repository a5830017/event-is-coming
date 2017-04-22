from django.db import models
#from django.utils import timezone

class Event(models.Model):
    event_name = models.TextField(default='') #name
    event_detail = models.TextField(default='') #detail
    event_numset = models.TextField(default='') #limit for start
    event_location = models.TextField(default='') #location
    #date = models.DateTimeField(default=timezone.now())#'date published')YYYY-MM-DD HH:MM

class Person(models.Model):
    fname = models.TextField(default='') #first name
    lname = models.TextField(default='') #last name
    pcount = models.IntegerField(default=0) #person count