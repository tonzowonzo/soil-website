from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime
from django.template import Template, Context


# Set variables
version = '0.1'
link = 'https://github.com/tonzowonzo/soil-project'

def title(request):
    return HttpResponse('Welcome to the soil image classifier.')
    
def current_date_time(request):
    '''
    Display the current time, this is dynamic on the website.
    '''
    now = datetime.datetime.now()
    # Take away microseconds so it only displays up to seconds in accuracy.
    now = now.strftime('%Y-%m-%d %H:%M:%S')
    html = '<html><body>It is now %s.</body></html>' % now
    return HttpResponse(html)
    
def hours_ahead(request, offset):
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
    
def about(request):
    raw_template = '''<p> Project Version {{ version }} </p>
    
    <p>The projects goal is to classify soil type based on images alone. It uses
    multiple convolutional neural networks in order to come up with a prediction.
    More information can be found at {{ link }}. </p>'''
    
    t = Template(raw_template)
    c = Context({'version': version,
                 'link': link
                 })
    rendered_template = t.render(c)
    return HttpResponse(rendered_template)
    
def statistics(request):
    time = datetime.datetime.now()
    time = time.strftime('%Y-%m-%d %H:%M:%S')
    raw_template = '''<p> Soil Statistics </p>
    
    <p>This page displays statistics about geolocations and soil distributions
    as well as overall soil commonality at the current time: {{ time }} .</p>'''
    t = Template(raw_template)
    c = Context({'time': time})
    rendered_template = t.render(c)
    return HttpResponse(rendered_template)
    
def process(request):
    return HttpResponse('This is the process page')
    
def examples(request):
    return HttpResponse('Here are some examples')
    
def contact(request):
    return HttpResponse('Contact details: ')
