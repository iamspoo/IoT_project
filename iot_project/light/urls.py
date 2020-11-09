from . import views
from django.urls import path,include
from django.conf.urls import url


urlpatterns=[
path('signup/',views.signup,name='signup'),

]