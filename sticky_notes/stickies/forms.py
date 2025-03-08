from django import forms
from . models import Sticky

class StickyForm(forms.ModelForm):
    
    class Meta:
        model = Sticky
        fields = ["name", "description"]
