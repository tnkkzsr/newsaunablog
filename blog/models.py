from asyncio import FastChildWatcher
from email.policy import default
from pickle import TRUE
from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import date
from django.contrib.auth.models import User

class SaunaImformation(models.Model):

    ROURYU_CHOICE = (
    
        (True,'あり'),
        (False,'なし'),
    )

    name = models.CharField( max_length=100)
    author = models.CharField( max_length=100, default = "")
    created = models.DateField(default = date.today)
    fee =  models.CharField(max_length=100,default = " ")
    rouryu = models.BooleanField(choices=ROURYU_CHOICE)
    place = models.CharField(max_length = 50)
    FreeText =  models.TextField() 

    def __str__(self):
        	return self.name

class Account(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    


				
    