# CarPartsSite/products/forms.py

from django import forms
from .models import Part

class PartForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = ['name', 'description', 'price', 'image']  # <--- ¡Agregado!
