from django.shortcuts import render, redirect, get_object_or_404
from .models import Place # import our place models
from .forms import NewPlaceForm # import import forms

# Create your views here.

# This function will be called by Django and it will be given information about the request the user is making the request, the browser's making
def place_list(request):

    if request.method == 'POST':
        # Create a new place
        form = NewPlaceForm(request.POST) # This is creating a form from the form data sent in the request
        place = form.save() # This creates a new place object from data in the form
        if form.is_valid(): # Validation against DB constraints
            place.save() # saves the models to the database
            return redirect('place_list') # We always have to return a response. This reloads the homepage

    # Before sending a response back, make a query to the database
    places = Place.objects.filter(visited=False).order_by('name') # Djangos ORMs
    # Create a form
    new_place_form = NewPlaceForm() # Creating a brand new, empty new place formand send it to a template below
    # rendering is another word for combining a template and data to form web page
    return render(request, 'travel_wishlist/wishlist.html', {'places': places, 'new_place_form': new_place_form}) # /wishlist.html is the name of a template. Add form to our dictionary of data which will be a new place object

def places_visited(request):
    visited = Place.objects.filter(visited=True)
    return render(request, 'travel_wishlist/visited.html', { 'visited': visited })

def place_was_visited(request, place_pk): # needs another arguement, django will extract the number created in urls.py within the int tag. Needs to match the variable name
    # We only want this to respond to POST request
    if request.method == 'POST':
        # place = Place.objects.get(pk=place_pk) # db query, returns the match one, one object
        place = get_object_or_404(Place, pk=place_pk) # Place is the class name and the query place is gong to be get object or 404. Try to make the query if found or 404 error
        place.visited = True
        place.save() # Any changes in code will not be reflected in the database unless you save

    return redirect('places_visited')

def about(request):
    # Create some data
    author = 'Johnny'
    about = 'A website to create a list of places to visit'
    return render(request, 'travel_wishlist/about.html', {'author': author, 'about': about})
