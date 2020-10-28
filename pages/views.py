
from django.shortcuts import render
from django.views.generic import TemplateView 

# Create your views here.
class HomePageView(TemplateView): 
    '''A specialized version of the Template view to display our home page ''' 

    template_name = 'pages/home.html'

class AboutPageView(TemplateView): 
    '''specialized version of the template view to display our 'about' page'''

    template_name='pages/about.html'

class SchedulePageView(TemplateView): 
    '''specialized version of the template view to display our 'schedule' page'''

    template_name='pages/schedule.html'
