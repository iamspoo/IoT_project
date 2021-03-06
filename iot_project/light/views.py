from django.shortcuts import render
from .models import light,area,Profile,history
from .forms import EmpForm,AreaForm,LightForm
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializers import ModeSerializer, StateSerializer
from rest_framework.response import Response
import datetime

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
              
@login_required(login_url='/')       
def lightview(request):
    lid=request.GET.get('lid','')
    request.session['lid']=lid
    liobj=light.objects.filter(id=lid)
    liobj=liobj[0]
    
    if liobj.status == 'H':
        liobj.status='High'
    elif liobj.status == 'L':
        liobj.status='Low'
    else:
        liobj.status='Medium'
        
    if liobj.mode=='M':
        liobj.mode='Manual'
    else:
        liobj.mode='Auto'
        
    
    areafk=liobj.areafk_id
    areaobj=area.objects.filter(areacode=areafk)
    areaobj=areaobj[0]
    areaadd=areaobj.address
    return render(request,'light/light_page.html',{"liobj":liobj,"areaadd":areaadd})
    
    
def automanual(request):
    state=request.GET.get('state')
    if state=='Auto':
        state='A'
    else:
        state='M'
    lid=request.session['lid']
    liobj=light.objects.filter(id=lid)
    liobj=liobj[0]
    liobj.mode=state
    h=history(lid=liobj.id,status=liobj.status,mode=state,time=str(datetime.datetime.now()))
    try:
        liobj.save()
        h.save()
        data={"s":"success"}
        return JsonResponse(data)
    except Exception:
        pass
    data={"s":"failed"}
    return JsonResponse(data)


def LowHigh(request):
    state=request.GET.get('lightstate')
    lid=request.session['lid']
    liobj=light.objects.filter(id=lid)
    liobj=liobj[0]
    if state=='High':
        state='H'
    else:
        state='L'
    liobj.status=state
    h=history(lid=liobj.id,status=state,mode=liobj.mode,time=str(datetime.datetime.now()))
    try:
        liobj.save()
        h.save()
        data={"s":"success"}
        return JsonResponse(data)
    except Exception:
        pass
    data={"s":"failed"}
    return JsonResponse(data)
    
def report(request):
    report=history.objects.all()
    return render(request,'light/report.html',{"report":report})


class StateViewSet(viewsets.ModelViewSet):
    queryset = light.objects.all()
    serializer_class = StateSerializer
    def update(self, request, *args, **kwargs):
        partial = True
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        h=history(lid=instance.id,status=request.data['status'],mode=instance.mode,time=str(datetime.datetime.now()))
        h.save()
        self.perform_update(serializer)
        return Response(serializer.data)
    
class ModeViewSet(viewsets.ModelViewSet):
    queryset = light.objects.all()
    serializer_class = ModeSerializer
    def update(self, request, *args, **kwargs):
        partial = True
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        h=history(lid=instance.id,status=instance.status,mode=request.data['mode'],time=str(datetime.datetime.now()))
        h.save()
        self.perform_update(serializer)
        return Response(serializer.data)

    
      