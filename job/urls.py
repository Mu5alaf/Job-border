from django.urls import path
from . import views
app_name = 'job'
urlpatterns = [
    path('',views.Job_List_view,name='Job_List'),
    path('add/',views.add_job,name='add_job'),
    path('<str:slug>/',views.Job_Details_view,name='Job_Details'),
]



