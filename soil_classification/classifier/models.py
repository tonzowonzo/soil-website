from django.db import models

# Create your models here.
city_list = []

class Location(models.Model):
    '''
    Class to store location of an individual.
    '''
    is_city = True # Change to false when done testing
    city_town = models.CharField(max_length=50, blank=True)
    

    if city_town in city_list:
        is_city = True

    def __str__(self):
        if self.is_city:
            return self.city_town
        
class Image(models.Model):
    '''
    Class to store image data and verify whether it is an image.
    '''
    soil_image = models.ImageField(upload_to='tmp')
    upload_date = models.DateTimeField()
    
    def handle_file(f):
        with open()

class User(models.Model):
    '''
    Class to store user information
    '''
    first_name = models.CharField(max_length=30, blank=True, verbose_name = 'First Name')
    last_name = models.CharField(max_length=30, blank=True, verbose_name = 'Last Name')

    email = models.EmailField(blank=True, verbose_name='E-mail')
    
    def __str__(self):
        return 'name: {}, email: {}'.format(self.first_name, self.last_name, self.email)