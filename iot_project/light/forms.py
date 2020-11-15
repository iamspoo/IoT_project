from .models import Profile
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','email','password')
              
class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('areaufk',)
       
            
