
from django.shortcuts import render
from django.views.generic import ListView , DetailView 
from django.views.generic.edit import  CreateView , UpdateView , DeleteView
from .models import Quote , Person  
from .forms import CreateQuoteForm,  UpdateQuoteForm , AddImageForm
from django.urls import reverse
from django.urls import reverse
from django.shortcuts import redirect
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
    '''Display a single quote item'''
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


class PersonPageView(DetailView): 
    '''Display a single persion '''
    model = Person 
    template_name = 'quotes/person.html' #provide the name of the template we will use to display the data and create file 'home'
    #context_object_name = "person" 
    def get_context_data(self, **kwargs) :
        'return a dictionarywith context data for this template to use'

    #get the default context data
        context = super(PersonPageView,self).get_context_data(**kwargs)
        #create the add image form 
        add_image_form = AddImageForm() 
        context ['add_image_form'] = add_image_form

        #return the context dictionary
        return context

class CreateQuoteView(CreateView):
    "create a new quote store in database" 
    model = Quote
    form_class = CreateQuoteForm 
    template_name = "quotes/create_quote_form.html" #


class UpdateQuoteView(UpdateView):
    "update a quote store in database" 
    queryset = Quote.objects.all()
    form_class = UpdateQuoteForm
    template_name = "quotes/update_quote_form.html" #




class DeleteQuoteView(DeleteView):
    "delete a quote and store change in database" 

    queryset = Quote.objects.all()
  
    template_name = "quotes/delete_quote.html" 

    #success_url = '../../all' # where to send after deleting quote 

    def get_success_url(self): 
        "return a URL to be directed too after deletion of quote" 
        # get the PK  
        pk = self.kwargs.get('pk')
        quote = Quote.objects.filter (pk=pk).first()

        # find the person using the quote
        person = quote.person 
        return reverse ('person', kwargs={'pk':person.pk})
        #use reverse to show the person page for that PK


def add_image(request, pk): 
    "custom view func to handle submission of uploaded image"

    #find person object 
    person = Person.objects.get(pk=pk)


    # turn request data into add image form object
    form = AddImageForm(request.POST or None, request.FILES or None)

    #check if form is valid, if so save to database 
    if  form.is_valid():
        image = form.save(commit=False) #create but dont save the object 
        image.person = person 
        image.save() # store to database 

    else: 
        print ("error: the form was not valid")

    # redirict to a new URL display person page
    url = reverse ('person', kwargs={'pk' :pk})
    return redirect(url)




