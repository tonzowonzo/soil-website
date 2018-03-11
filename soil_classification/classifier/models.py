from django.db import models

# Create your models here.
city_list = []

class Location(models.Model):
    '''
    Class to store location of an individual.
    '''
    def __init__(self):
        # Change this to a choice in the future.
        self.city_town = models.CharField(max_length=50)
    
    def is_city(self):
        if self.city_town in city_list:
            return self.city_town

    
class Image(models.Model):
    '''
    Class to store image data and verify whether it is an image.
    '''
    soil_image = models.ImageField(upload_to='tmp')
    upload_date = models.DateTimeField()

class User(models.Model):
    '''
    Class to store user information
    '''
    name = models.CharField(max_length=30)
    email = models.EmailField()
    