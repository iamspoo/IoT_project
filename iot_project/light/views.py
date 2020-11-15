from django.shortcuts import render
from .models import light,area
from .forms import EmpForm
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.

def adminview(request):
    l=light.objects.all()
    for i in l:
        areaobj=area.objects.get(areacode=i.areafk_id)
        i.address=areaobj.address
    eform=EmpForm()
    return render(request,'light/admin_page.html',{"lights":l,"eform":eform})

def register(request):
    eform=EmpForm(request.POST)
    if eform.is_valid():
        try:
            eform.save()
            data={"s":"success"}
            return JsonResponse(data)
        except Exception:
            pass
    data={"s":"failed"}
    return JsonResponse(data)

def empview(request):
    emp=request.user
    print(emp)
    l=light.objects.all()
    for i in l:
        areaobj=area.objects.get(areacode=i.areafk_id)
        i.address=areaobj.address
    return render(request,'light/emp_page.html',{"lights":l})
    
def adminsignin(request):
    admin=None
    uname=request.POST.get("username")
    password=request.POST.get("password")
    admin=User.objects.filter(username=uname)
    if not admin or admin[0].is_superuser!=1:
        return render(request,'home.html',{'m':'Acess Denied, Not a admin'})
    else:
        if admin[0].password == password:
            request.session['adminid']=admin[0].id
            return HttpResponseRedirect('/light/adminpage')
        else:
            return render(request,'home.html',{'m':'Invalid username or password'})
            
            
def empsignin(request):
    user=None
    uname=request.POST.get("username")
    password=request.POST.get("password")
    user=User.objects.filter(username=uname)
    '''user=authenticate(request,username=uname,password=password)
    login(request,user)'''
    if not user or user[0].password != password:
        return render(request,'home.html',{'m':'Invalid username or password'})
    else:
        request.session['userid']=user[0].id
        return HttpResponseRedirect('/light/emppage')
  
    
            
            
            
            
            
            
            
            
            
