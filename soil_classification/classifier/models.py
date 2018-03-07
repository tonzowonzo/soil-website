from django.db import models

# Create your models here.
class Photo(TimeStampedModel):
    album = models.ForeignKey(Album)
    