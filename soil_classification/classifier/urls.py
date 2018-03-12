from django.urls import path
from . import views
import re

urlpatterns = [
        path('', views.title, name='title'),
        path('about/', views.about, name='about' ),
        path('statistics/', views.statistics, name='statistics' ),
        path('process/', views.process, name='process' ),
        path('examples/', views.examples, name='examples' ),
        path('contact/', views.contact, name='contact' ),
        path('contact/thanks/', views.thanks, name='thanks'),
]