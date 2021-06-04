# from django.http import request
from django.urls import path
from . import views, api


app_name = 'job'

urlpatterns = [
    #don't make excute to job_list because you will have an error missing argument 
    path('', views.job_list, name='job_list'),  #this is the main  
    #here you need to make the correct order because you have a slug and don't add / 
    path('add', views.add_job, name='add_job'),
    path('<str:slug>', views.job_detail, name='job_detail'),
    
    ## api
    path('api/jobs',api.job_list_api , name='job_list_api'),
    path('api/jobs/<int:id>',api.job_detail_api , name='job_detail_api'),
    
    ## class based views
    path('api/v2/jobs',api.JobListApi.as_view() , name='job_list_api'),
    path('api/v2/jobs/<int:id>',api.JobDetail.as_view() , name='job_detail_api'),

]
