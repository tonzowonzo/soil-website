from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime
from django.template import Template, Context, RequestContext
from classifier.forms import ContactForm
from classifier.forms import custom_proc
from django.core.mail import send_mail, get_connection
from django.template.loader import get_template

# Set variables
version = '0.1'
link = 'https://github.com/tonzowonzo/soil-project'

def title(request):
    return HttpResponse('Welcome to the soil image classifier.')
        
def about(request):
    '''
    Page that contains information about the project, how it works and links
    to code.
    '''
    t = get_template('about.html')
    c = {'version': version,
         'link': link
         }
    rendered_template = t.render(c)
    return HttpResponse(rendered_template)
    
def statistics(request):
    '''
    Page that contains statistics on soil commanality, distribution along with
    geostatistics using GIS plugin.
    '''
    time = datetime.datetime.now()
    time = time.strftime('%Y-%m-%d %H:%M:%S')

    t = get_template('statistics.html')
    c = {'time': time}
    rendered_template = t.render(c)
    return HttpResponse(rendered_template)
    
def process(request):
    return HttpResponse('This is the process page')
    
def examples(request):
    return HttpResponse('Here are some examples')
    
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cleanData = form.cleaned_data
            connect = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(cleanData['subject'],
                      cleanData['message'],
                      cleanData.get('email', 'twonzo72@gmail.com'),
                      ['twonzo72@gmail.com'],
                      connection=connect)
            return HttpResponseRedirect('/classifier/contact/thanks/')
            
    else:
        form = ContactForm(initial={'subject': 'Subject'})
        
    return render(request, 'contact_form.html', {'form': form})
    
def thanks(request):
    return HttpResponse('Thanks for the email, we will respond shortly')
    
def test_page(request):
    '''
    A page for testing html / css
    '''
    t = get_template('view.html')
    c = {'test_words': 'This is a test.',
         'test_word2': 'This is test number 2.'}
    return HttpResponse(t.render(c))
            
def test_2(request):
    '''
    A page for testing Django backend changes.
    '''
    t = get_template('test2.html')
    c = custom_proc(request)
    return HttpResponse(t.render(c))
    
def base(request):
    '''
    Base layout for all pages.
    '''
    t = get_template('base.html')
    c = {'title_name': 'Soil Image Classifier'}
    return HttpResponse(t.render(c))