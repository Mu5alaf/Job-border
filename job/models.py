from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.

#Job_Type
JOB_TYPE = (
    ('Full time','Full Time'),
    ('Part time','Part Time'),
)
#rename upload image
def image_rename(instance,filename):
    image_name , extension = filename.split('.')
    new_filename = "job/%s/%s.%s" % (instance.id, instance.id, extension)
    return new_filename
class Job(models.Model):
    owner =  models.ForeignKey(User,related_name='job_owner',on_delete=models.CASCADE)
    title = models.CharField(max_length=100,blank=False,null=False)
    job_type = models.CharField(max_length=15,choices=JOB_TYPE,blank=False,null=False)
    description = models.TextField(max_length=999,blank=False,null=False,default='Write a description')
    created_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1,null=False,blank=False)
    salary = models.IntegerField(default=0,null=False,blank=False)
    experiences = models.IntegerField(default=1,null=False,blank=False)
    category = models.ForeignKey('Category',on_delete=models.CASCADE,null=True,blank=False)
    image = models.ImageField(upload_to=image_rename,blank=True,null=True)
    slug = models.SlugField(null=True,blank=True)
    
    def __str__(self):
        return self.title
    #auto save slug as title
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
class Category(models.Model):
    name = models.CharField(max_length=25,blank=False,null=False)
    
    def __str__ (self):
        return self.name
    
    

class Apply(models.Model):
    job = models.ForeignKey(Job,related_name='apply_job',on_delete=models.CASCADE)
    name = models.CharField(max_length=30,blank=False,null=False)    
    email = models.EmailField(max_length=30,blank=False,null=False)
    portfolio_url = models.URLField(max_length=200,blank=True,null=True)
    cover_letter = models.TextField(max_length=340,blank=True,null=True)    
    cv_upload = models.FileField(upload_to='apply/',max_length=340,blank=True,null=True,default='Choice file')    
    
    def __str__(self):
        return self.name