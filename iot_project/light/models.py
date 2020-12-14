from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(User):
    areafk=models.ForeignKey("area",on_delete=models.CASCADE,default="000")

class light(models.Model):
    status=models.CharField(max_length=1,default='L')
    mode=models.CharField(max_length=1,default='A')
    areafk=models.ForeignKey("area",on_delete=models.CASCADE,)

class area(models.Model):
    areacode=models.CharField(max_length=10,primary_key=True)
    address=models.TextField()

class history(models.Model):
    lid=models.IntegerField(default=0)
    status=models.CharField(max_length=1)
    mode=models.CharField(max_length=1)
    time=models.CharField(max_length=50)
