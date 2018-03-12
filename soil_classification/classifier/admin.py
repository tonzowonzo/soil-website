from django.contrib import admin
from .models import User, Location, Image

# Register your models here.

# Split up names
class NameAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')  
    search_fields = ('first_name', 'last_name')
    
#class LocationAdmin(admin.ModelAdmin):
#    list_display = ('city_town')
#    list_filter = ('city_town',)

class ImageAdmin(admin.ModelAdmin):
    date_hierarchy = 'upload_date'
    
admin.site.register(User, NameAdmin)
admin.site.register(Location)
admin.site.register(Image, ImageAdmin)

