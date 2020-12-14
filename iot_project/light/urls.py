from . import views
from django.urls import path,include
from django.conf.urls import url
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'mode', views.ModeViewSet)
router.register(r'state', views.StateViewSet)


urlpatterns=[
path('adminpage/',views.adminview,name='adminpage'),
path('emppage/',views.empview,name='emppage'),
path('register/',views.register,name='register'),
path('adminsignin/',views.adminsignin,name='adminsignin'),
path('empsignin/',views.empsignin,name='empsignin'),
path('lightreg/',views.lightreg,name='lightreg'),
path('areareg/',views.areareg,name='areareg'),
path('logout/',views.logoutview,name='logout'),
path('lightview/',views.lightview,name='lightview'),
path('automanual/',views.automanual,name='automanual'),
path('LowHigh/',views.LowHigh,name='LowHigh'),
path('report/',views.report,name='report'),
path('', include(router.urls)),
]