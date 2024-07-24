from django import forms
from .models import Apply ,Job

class apply_form (forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['name', 'email', 'portfolio_url', 'cover_letter', 'cv_upload']
        
        
class add_job_form(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['slug','owner']