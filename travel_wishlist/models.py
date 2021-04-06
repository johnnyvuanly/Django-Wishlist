from django.db import models
from django.contrib.auth.models import User # Import django user model

# Create your models here.
class Place(models.Model):
    user = models.ForeignKey('auth.User', null=False, on_delete=models.CASCADE) # first name the other table using a string, second we don't want the user to be null/empty, lastly specify when user is deleted which delete all associated places with 'CASCADE'
    name = models.CharField(max_length=200)
    visited = models.BooleanField(default=False) # We'll assume that the user is creating a place they haven't been to yet
    notes = models.TextField(blank=True, null=True) # Allow blanks
    date_visited = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='user_images/', blank=True, null=True ) # Where the images get uploaded to our directory user images

    # Adding a string method
    def __str__(self): # Method in a class
        return f'{self.name} visited? {self.visited}' # This is never going to be displayed to the user. This is something helpful for the developer to see
