from django.contrib import messages
from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Job
from .form import apply_form ,add_job_form
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .filters import Job_Filter
# Create your views here.
#Job_List

def Job_List_view(request):
    job_list = Job.objects.all()
    #flitter
    my_filter = Job_Filter(request.GET,queryset=Job.objects.all())
    job_list = my_filter.qs
    paginator = Paginator(job_list, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context={'job_list':page_obj,'job_num':job_list,'my_filter':my_filter}
    return render(request,'./job/jobs.html',context)
    

def Job_Details_view(request,slug):
    job_details = Job.objects.get(slug=slug)
    if request.method=='POST':
        form = apply_form(request.POST,request.FILES)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.job = job_details
            my_form.save()
            messages.success(request,"You have been successfully Apply.")
            return redirect('job:Job_List')
        else:
            messages.error(request,"There was an error during apply")
    else:
        form = apply_form()
    context = {'job_details':job_details,'form':form}
    return render(request,'./job/job_details.html',context)

@login_required
def add_job(request):
    if request.method=='POST':
        form = add_job_form(request.POST,request.FILES)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.owner = request.user
            my_form.save()
            messages.success(request,'Your job post has been added successfully')
            return redirect(reverse('job:Job_List'))
        else:
            messages.error(request,'something went wrong')
            redirect('job:add_job')
    else:
        form = add_job_form()
    context = {'form':form}
    return render(request,'./job/add_job.html',context)

