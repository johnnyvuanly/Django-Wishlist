from django.db import models
from django.contrib.auth.models import User # Import django user model
from django.core.files.storage import default_storage

# Create your models here.
class Place(models.Model):
    user = models.ForeignKey('auth.User', null=False, on_delete=models.CASCADE) # first name the other table using a string, second we don't want the user to be null/empty, lastly specify when user is deleted which delete all associated places with 'CASCADE'
    name = models.CharField(max_length=200)
    visited = models.BooleanField(default=False) # We'll assume that the user is creating a place they haven't been to yet
    notes = models.TextField(blank=True, null=True) # Allow blanks
    date_visited = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='user_images/', blank=True, null=True ) # Where the images get uploaded to our directory user images

    # What this method does is going to override Django's save method 
    def save(self, *args, **kwargs): # When we call save on our place object, we'll do our own tasks and then call through to the actual Django save
        old_place = Place.objects.filter(pk=self.pk).first()
        if old_place and old_place.photo:
            if old_place.photo != self.photo: # Check if the photo is being changed. If old photo is not equal to new photo
                self.delete_photo(old_place.photo) # Then delete that photo

        super().save(*args, **kwargs) # super class method save
    
    def delete_photo(self, photo):
        # Check to see if a photo exists
        if default_storage.exists(photo.name):
            default_storage.delete(photo.name)

    # Overide the delete function self args, method is called before a object is deleted
    def delete(self, *args, **kwargs):
        if self.photos:
            self.delete_photo(self.photo)

        super().delete(*args, kwards)


    # Adding a string method
    def __str__(self): # Method in a class
        photo_str = self.photo.url if self.photo else 'no photo'
        notes_str = self.notes[100:] if self.notes else 'no notes' # If you wanted to include info about notes
        return f'{self.name} visited? {self.visited} on {self.date_visited}. Notes: {notes_str}. Photo {photo_str}' # This is never going to be displayed to the user. This is something helpful for the developer to see
