from django.shortcuts import render
from .models import light,area
from .forms import EmpForm
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse


# Create your views here.

def signup(request):
    return render(request, 'register.html')



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
