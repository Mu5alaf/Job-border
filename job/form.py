from django import forms
from .models import Apply

class apply_form (forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['name', 'email', 'portfolio_url', 'cover_letter', 'cv_upload']