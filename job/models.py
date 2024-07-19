from django.db import models
# Create your models here.

#Job_Type
JOB_TYPE = (
    ('Full time','Full Time'),
    ('Part time','Part Time'),
)
#rename upload image
def image_rename(instance,filename):
    image_name , extension = filename.split('.')
    return "job/%s/%s.%s"%(instance.id,instance.id,extension)
class Job(models.Model):
    title = models.CharField(max_length=100,blank=False,null=False)
    job_type = models.CharField(max_length=15,choices=JOB_TYPE,blank=False,null=False)
    description = models.TextField(max_length=999,blank=False,null=False,default='Write a description')
    created_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1,null=False,blank=False)
    salary = models.IntegerField(default=0,null=False,blank=False)
    experiences = models.IntegerField(default=1,null=False,blank=False)
    category = models.ForeignKey('Category',on_delete=models.CASCADE,null=True,blank=False)
    image = models.ImageField(upload_to=image_rename,blank=True,null=True)
    def __str__(self):
        return self.title
    
    
class Category(models.Model):
    name = models.CharField(max_length=25,blank=False,null=False)
    
    def __str__ (self):
        return self.name