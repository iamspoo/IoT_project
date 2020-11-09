from django.db import models

# Create your models here.

class light(models.Model):
    status=models.CharField(max_length=1)
    mode=models.CharField(max_length=1)
    areafk=models.ForeignKey("area",on_delete=models.CASCADE,)

class area(models.Model):
    areacode=models.CharField(max_length=10,primary_key=True)
    address=models.TextField()
