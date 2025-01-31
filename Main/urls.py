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
    path("predict_job",views.predict_job,name='predict_job'),
    path("test_skills",views.test_skills,name='test_skills'),
    path("calc_score",views.calc_score,name='calc_score'),
    path("show_prediction",views.show_prediction,name='show_prediction'),
    path("save_academic",views.save_academic,name='save_academic'),
    path("delete_pred_data",views.delete_pred_data,name='delete_pred_data'),
    
    
    
    
]
