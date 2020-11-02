from django.shortcuts import render
from django.views.generic import ListView
from .models import Quote

class HomePageView(ListView): #present many objects from one model in a single screen? 
    """show a listing of Quotes."""
    model = Quote #retrive Quote obejcts from the model database 
    template_name = 'quotes/home.html' #provide the name of the template we will use to display the data and create file 'home'
    context_object_name = "quotes" 

    #context object name = name of variable from the database that we can call to deliver the data



# Create your views here.
