from django.urls import path
from . import views
app_name = 'accounts'
urlpatterns = [
    path('signup',views.signup_view,name='sign_up'),
    path('profile',views.Profile_view,name='profile'),
    path('profile/edit',views.Profile_edit_view,name='profile_edit'),
]



