from django import forms
from .models import musician_model

class musician_form(forms.ModelForm):
    class Meta:
        model = musician_model
        fields = '__all__'
        
