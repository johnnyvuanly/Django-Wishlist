from django import forms
from django.forms import FileInput, DateInput
from .models import Place

class NewPlaceForm(forms.ModelForm): # Form for the webpage
    class Meta:
        model = Place
        fields = {'name', 'visited'}

""" by default Django will show regular plain text field that accepts
 text for a data field, con is no validation to see if they're entering
  a real date. Reason why class is included here. """
class DateInput(forms.DateInput):
    input_type = 'date'

class TripReviewForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('notes', 'date_visited', 'photo')
        widgets = {
            'date_visited': DateInput() 
        }