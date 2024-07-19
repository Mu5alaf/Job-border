from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator
# Create your views here.
#Job_List

def Job_List(request):
    job_list = Job.objects.all()
    paginator = Paginator(job_list, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context={'job_list':page_obj,'job_num':job_list}
    return render(request,'./job/jobs.html',context)
    


def Job_Details(request,slug):
    job_details = Job.objects.get(slug=slug)
    context = {'job_details':job_details}
    return render(request,'./job/job_details.html',context)
