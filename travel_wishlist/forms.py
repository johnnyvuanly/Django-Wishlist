from django import forms
from .models import Place

class NewPlaceForm(forms.ModelForm): # Form for the webpage
    class Meta:
        model = Place
        fields = {'name', 'visited'}

class TripReviewForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = {'notes', 'date_visited', 'photo'}
        widgets = {
            'date_visited': DateInput() # by default Django will show regular plain text field that accepts text for a data field, con is no validation to see if they're entering a real date
        }