from django.shortcuts import render
from .models import Job
# Create your views here.
#Job_List

def Job_List(request):
    job_list = Job.objects.all()
    context={'job_list':job_list}
    return render(request,'./job/jobs.html',context)
    


def Job_Details(request,id):
    job_details = Job.objects.get(id=id)
    context = {'job_details':job_details}
    return render(request,'./job/job_details.html',context)
