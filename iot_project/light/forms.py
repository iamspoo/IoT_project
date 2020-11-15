from django import forms
from .models import Profile,area,light
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelChoiceField

class EmpForm(UserCreationForm):
    class Meta:
        model=Profile
        fields=['username','areafk','email','password1','password2']
        widgets={
            'username':forms.TextInput(attrs={'class':"form-control"}),
            'email':forms.EmailInput(attrs={'class':"form-control"}),
            'areafk':forms.TextInput(attrs={'class':"form-control"}),
        }
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class LightForm(forms.ModelForm):
    class Meta:
        model=light
        fields=['areafk']
        widgets={
            'areafk':forms.TextInput(attrs={'class':"form-control"}),
        }

class AreaForm(forms.ModelForm):
    class Meta:
        model=area
        fields="__all__"
        widgets={
            'areacode':forms.TextInput(attrs={'class':"form-control"}),
            'address':forms.Textarea(attrs={'class':"form-control",'rows':3}),
        }




