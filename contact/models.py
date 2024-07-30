from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    massage = models.TextField(max_length=550)
    mail = models.EmailField(max_length=35)
    def __str__(self):
        return self.name
    