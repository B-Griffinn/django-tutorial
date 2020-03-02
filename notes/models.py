from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False ) # "default" generates random uuid when a new note is created
    title = models.CharField(max_length=200)    # allow our note title to only be 200 chars long                  
    content = models.TextField(blank=True)      # our body of the note is a text field with no restrictions

    # Adding New fields for the Migrations II videos
    created_at = models.DateTimeField(auto_now_add=True) # Returns True when the argument x is true, False otherwise.
    last_modified = models.DateTimeField(auto_now=True) #Returns True when the argument x is true, False otherwise.

class PersonalNote(Note):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
