from datetime import datetime
from xmlrpc.client import DateTime
from django.db import models
import django.utils

# Create your models here.

class Account(models.Model):
    name = models.CharField(max_length=20)
    createdDate = models.DateField(default= django.utils.timezone.now)

class Component(models.Model):
    name = models.CharField(max_length=20)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    type = models.CharField(max_length=10)
    icon = models.CharField(max_length=20)

class Assembly(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=10)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    icon = models.CharField(max_length=20)    

class AssemblyDetail(models.Model):
    name = models.CharField(max_length=20)
    assembly = models.ForeignKey(Assembly, on_delete=models.CASCADE)
    assemblyComponentName = models.CharField(max_length=20)
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    order = models.IntegerField()
    icon = models.CharField(max_length=20)
