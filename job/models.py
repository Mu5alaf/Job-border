from django.db import models
# Create your models here.

#Job_Type
JOB_TYPE = (
    ('Full time','Full Time'),
    ('Part time','Part Time'),
)
class Job(models.Model):
    title = models.CharField(max_length=100,blank=False,null=False)
    job_type = models.CharField(max_length=15,choices=JOB_TYPE,blank=False,null=False)
    description = models.TextField(max_length=999,blank=False,null=False,default='Write a description')
    created_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1,null=False,blank=False)
    salary = models.IntegerField(default=0,null=False,blank=False)
    experiences = models.IntegerField(default=1,null=False,blank=False)
    
    def __str__(self):
        return self.title