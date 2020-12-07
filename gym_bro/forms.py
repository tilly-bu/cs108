#forms.py 
from django import forms
from .models import Workout, Program

class UpdateProgramForm(forms.ModelForm): 
    'a form to add a workout day to our programs model' 

    class Meta: 
        'additional data to inform the form what model to update' 
        model = Program #which program to update
        fields = ['user','workouts','reps','sets','date'] #data attributes to pick
        