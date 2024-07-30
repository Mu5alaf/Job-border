from django.shortcuts import render,redirect
from .forms import contact_form
from django.contrib import messages

# Create your views here.
def contact_view(request):
    form = contact_form(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request,'Your massage has been sent')
            return redirect('job:Job_List')
        else:
            messages.error(request,'something went wrong')
            return redirect('contact:contact_us')
    else:
        context = {'contact_form':form}
    return render(request,'contact/contact_us.html',context)