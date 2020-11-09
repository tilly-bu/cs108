#forms.py 

from django import forms
from .models import Quote , Image

class CreateQuoteForm(forms.ModelForm): #inherits from django library that creates a specific form
    """A form to create a new Quote object """ 

    class Meta: 
        '''additional data about this form''' 
        model = Quote # which model to create 
        fields = ['text','person'] # which fields to create 


class UpdateQuoteForm(forms.ModelForm): #inherits from django library that creates a specific form
    """A form to create a new Quote object """ 

    class Meta: 
        '''additional data about this form''' 
        model = Quote # which model to create 
        fields = ['text','person'] # which fields to create 


class AddImageForm (forms.ModelForm): 
    'A form to collect an image from the user' 

    class Meta : 
        model = Image  
        fields = ["image_file",] 


