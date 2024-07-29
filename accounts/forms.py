from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from .models import Profile
class signup_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
class User_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        
class Profile_Form(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['city','phone_number','image']
