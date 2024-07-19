from django.urls import path
from . import views
app_name = 'job'
urlpatterns = [
    path('',views.Job_List,name='Job_List'),
    path('<str:slug>/',views.Job_Details,name='Job_Details'),
]



