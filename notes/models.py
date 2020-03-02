from django.db import models
from uuid import uuid4

# Create your models here.
class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False ) # "default" generates random uuid when a new note is created
    title = models.CharField(max_length=200)    # allow our note title to only be 200 chars long                  
    content = models.TextField(blank=True)      # our body of the note is a text field with no restrictions
