from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
  
class light(models.Model):
    status=models.CharField(max_length=1,default='L')
    mode=models.CharField(max_length=1,default='A')
    areafk=models.ForeignKey("area",on_delete=models.CASCADE,)

class area(models.Model):
    areacode=models.CharField(max_length=10,primary_key=True)
    address=models.TextField()
    
class Profile(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    areaufk=models.ForeignKey("area",on_delete=models.CASCADE,)
    
@receiver(post_save, sender=User)
def create_user_myuser(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_myuser(sender, instance, **kwargs):
    instance.profile.save()
        