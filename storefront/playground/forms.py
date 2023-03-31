from django import forms
from .models import Dream

class DreamForm(forms.ModelForm):
    class Meta:
        model = Dream
        fields = ['description', 'duration', 'stress_level', 'energy']