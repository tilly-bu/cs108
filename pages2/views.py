from django.shortcuts import render
from django.views.generic import TemplateView #from the django package install the package that allows
                                                # to view a html temlate

# a url difined in the urls.py file wil refer to this views 
# this views will map to a html template to display 

class HomePageView(TemplateView): 
    #HomePageView is the name that we create, template view is the package that we install to view
    'A specialized version of the TemplateView customized to display our home page'

    template_name = "pages2/home.html"  #must refer to the location and file name of the template we want
    #this 

# Create your views here.

class AboutPageView(TemplateView): 
    'specialized version that displayed our home page' 

    template_name = "pages2/about.html" 

