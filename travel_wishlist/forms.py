from django import forms
from .models import Place

class NewPlaceForm(forms.ModelForm): # Form for the webpage
    class Meta:
        model = Place
        fields = {'name', 'visited'}