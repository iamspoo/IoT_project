from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import UserForm, ProfileForm
from django.http import HttpResponseRedirect

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST,instance=request.user)
        form2= ProfileForm(request.POST,instance=request.user.profile)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/')
    else:
        form = UserForm(instance=request.user)
        form2= ProfileForm(instance=request.user.profile)
    dic = {'form': form,'form2':form2}
    return render(request, 'register.html',dic)
    
