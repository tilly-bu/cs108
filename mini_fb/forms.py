from  django import forms
from .models import* # Profile , StatusMessage

class CreateProfileForm(forms.ModelForm): 
    "A form to create a profile"

    class Meta: 
        'aditional data about this form' 
        model = Profile
        fields = ['first_name','last_name','email_address'] #which fields to create with this quote form


class UpdateProfileForm(forms.ModelForm):
    "form to update a profile"

    class Meta: 
        'aditional data about this form' 
        model = Profile
        fields = ['first_name','last_name','email_address'] #which fields to create with this quote form


class CreateStatusMessageForm(forms.ModelForm): 
    "form to update status" 

    class Meta: 
        'inherit the model to update data too' 
        model = StatusMessage
        fields = ['message','img_file']



