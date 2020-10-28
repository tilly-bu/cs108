
from django.shortcuts import render
from django.views.generic import TemplateView 

# Create your views here.
class HomePageView(TemplateView): 
    '''A specialized version of the Template view to display our home page ''' 

    template_name = 'pages/home.html'


