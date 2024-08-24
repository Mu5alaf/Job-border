from django.urls import path
from . import views
from . import api

app_name = 'job'
urlpatterns = [
    path('',views.Job_List_view,name='Job_List'),
    path('add/',views.add_job,name='add_job'),
    path('<str:slug>/',views.Job_Details_view,name='Job_Details'),
    #api
    path('api/list',api.job_list_api,name='job_list_api'),
    path('api/jobs/<int:id>',api.job_detail_api,name='job_detail_api'),
]



