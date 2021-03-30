from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=200)
    visited = models.BooleanField(default=False) # We'll assume that the user is creating a place they haven't been to yet

    # Adding a string method
    def __str__(self): # Method in a class
        return f'{self.name} visited? {self.visited}' # This is never going to be displayed to the user. This is something helpful for the developer to see
