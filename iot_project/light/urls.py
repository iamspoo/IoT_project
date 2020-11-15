from . import views
from django.urls import path,include
from django.conf.urls import url


urlpatterns=[
path('adminpage/',views.adminview,name='adminpage'),
path('emppage/',views.empview,name='emppage'),
path('register/',views.register,name='register'),
path('adminsignin/',views.adminsignin,name='adminsignin'),
path('empsignin/',views.empsignin,name='empsignin'),
path('lightreg/',views.lightreg,name='lightreg'),
path('areareg/',views.areareg,name='areareg'),
path('logout/',views.logoutview,name='logout'),


]