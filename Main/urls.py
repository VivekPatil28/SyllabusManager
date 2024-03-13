from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('signin',views.signin,name='signin'),
    path("signup",views.signup,name='signup'),
    path('roadmap/<str:str>',views.roadmap),
    path('roadmap/subtopic/<str:str>',views.subtopicdesc),
    path('checked',views.checked),
    path('test',views.readyToStartTest),
    path('starttest',views.starttest),
    path('showResult',views.showResult),
    path("signout",views.signout,name='signout'),
    path("sem",views.changeSem,name='changeSem'),
]
