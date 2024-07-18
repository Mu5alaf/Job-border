from django.urls import path
from . import views
urlpatterns = [
    path('',views.Job_List),
    path('<int:id>',views.Job_Details),
]



