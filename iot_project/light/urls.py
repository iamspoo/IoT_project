from . import views
from django.urls import path,include
from django.conf.urls import url
from django.contrib import admin


urlpatterns=[
path('register/',views.register,name='register'),
#path('accounts/', include('django.contrib.auth.urls'))
]