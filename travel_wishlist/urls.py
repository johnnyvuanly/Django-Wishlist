from django.urls import path # path describes what a URL looks like 
from . import views

urlpatterns = [
    # List of URLs our app will recognize
    path('', views.place_list, name='place_list'), # This is going to represent a request to the path empty string (homepage). Any request made to the homepage should be handled by a function called playlist in the views module
    path('visited', views.places_visited, name='places_visited'),
    path('place/<int:place_pk>/was_visited', views.place_was_visited, name='place_was_visited'),
    path('about', views.about, name='about'),
    path('place/<int:place_pk>', views.place_details, name='place_details'), # <int:place_pk> is called capturing which will capture any url that is place/anynumber
    path('place/<int:place_pk>/delete', views.delete_place, name='delete_place')
]