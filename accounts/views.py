from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from .forms import signup_form ,User_Form,Profile_Form
from .models import Profile
from django.contrib import messages

# Create your views here.
def signup_view(request):
    if request.method=='POST':
        form = signup_form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(user=username,password=password)
            login(request,user)
            messages.success(request,"You have been successfully Signup.")
            return redirect('accounts/profile')
        else:
            messages.error(request,"There was an error during apply")
            return redirect('accounts:sign_up')
    else:
        form = signup_form()
    return render(request,'registration/signup.html',{'form':form})

def Profile_view(request):
    user = Profile.objects.get(user=request.user)
    if request.user.is_authenticated:
        return render(request, "accounts/profile.html", {'user':user})
    else:
        return render(request, "registration/login.html")


def Profile_edit_view(request):
    profile = Profile.objects.get(user=request.user)
    if request.method=='POST':
        user_form = User_Form(request.POST,instance=request.user)
        profile_form = Profile_Form(request.POST,request.FILES,instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            my_profile = profile_form.save(commit=False)
            my_profile.user = request.user
            my_profile.save()
            messages.success(request,"You have been successfully Edited.")
            return redirect('accounts:profile')
        else:
            messages.error(request,"There was an error during apply")
            return redirect('accounts:profile_edit')
    else:
        user_form = User_Form(instance=request.user)
        profile_form = Profile_Form(instance=profile)
    return render(request,'accounts/edit_profile.html',{'user_form':user_form,'profile_form':profile_form})
        