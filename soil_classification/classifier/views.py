from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def title(request):
    return HttpResponse('Welcome to the soil image classifier.')