from django.shortcuts import render
from .models import light,area,Profile
from .forms import EmpForm,AreaForm,LightForm
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def adminview(request):
    l=light.objects.all()
    for i in l:
        areaobj=area.objects.get(areacode=i.areafk_id)
        i.address=areaobj.address
    eform=EmpForm()
    aform=AreaForm()
    lform=LightForm()
    return render(request,'light/admin_page.html',{"lights":l,"eform":eform,"aform":aform,"lform":lform})

@login_required(login_url='/')
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

@login_required(login_url='/')
def lightreg(request):
    lform=LightForm(request.POST)
    if lform.is_valid():
        try:
            l=lform.save()
            data={"s":"success","id":l.id}
            return JsonResponse(data)
        except Exception:
            pass
    data={"s":"failed"}
    return JsonResponse(data)

@login_required(login_url='/')
def areareg(request):
    aform=AreaForm(request.POST)
    if aform.is_valid():
        try:
            aform.save()
            data={"s":"success"}
            return JsonResponse(data)
        except Exception:
            pass
    data={"s":"failed"}
    return JsonResponse(data)

@login_required(login_url='/')
def empview(request):
    emp=request.user
    p=Profile.objects.get(user_ptr_id=emp.id)  
    l=light.objects.filter(areafk_id=p.areafk_id)
    for i in l:
        areaobj=area.objects.get(areacode=i.areafk_id)
        i.address=areaobj.address
    return render(request,'light/emp_page.html',{"lights":l})
    
    
def adminsignin(request):
    admin=None
    username=request.POST.get("username")
    password=request.POST.get("password")
    admin = authenticate(request, username=username, password=password)
    if admin is not None:
        if admin.is_superuser!=1:
            return render(request,'home.html',{'m':'Acess Denied, Not an admin'})
        else:
            login(request, admin)
            return HttpResponseRedirect('/light/adminpage') 
    else:
        return render(request,'home.html',{'m':'Invalid username or password'})
            
            
def empsignin(request):
    user=None
    username=request.POST.get("eusername")
    password=request.POST.get("epassword")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/light/emppage') 
    else:
        return render(request,'home.html',{'m':'Invalid username or password'})

@login_required(login_url='/')
def logoutview(request):
    logout(request)
    return render(request,'home.html')
            
            
            
            
      