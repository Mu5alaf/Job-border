from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from .forms import signup_form
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