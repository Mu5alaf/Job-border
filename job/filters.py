import django_filters
from .models import Job

class Job_Filter(django_filters.FilterSet):
    class Meta:
        model = Job
        fields = ['title', 'job_type', 'category']