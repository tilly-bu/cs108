from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Quote
import random

class HomePageView(ListView): #present many objects from one model in a single screen? 
    """show a listing of Quotes."""
    model = Quote #retrive Quote obejcts from the model database 
    template_name = 'quotes/home.html' #provide the name of the template we will use to display the data and create file 'home'
    context_object_name = "quotes" 

    #context object name = name of variable from the database that we can call to deliver the data

class QuotePageView(DetailView): 
    '''Display a single quote item'''
    model = Quote #retrive Quote obejcts from the model database 
    template_name = 'quotes/quote.html' #provide the name of the template we will use to display the data and create file 'home'
    context_object_name = "quote" 

class RandomQuotePageView(DetailView): 
    '''Display a single qoute item'''
    model = Quote #retrive Quote obejcts from the model database 
    template_name = 'quotes/quote.html' #provide the name of the template we will use to display the data and create file 'home'
    context_object_name = "quote" 

    def get_object(self):
        '''select a random quote to display in the quote.html template'''
        #obtain all quotes using managet 
        quotes = Quote.objects.all()
        #select one at random 
        q = random.choice(quotes) 
        return q 






