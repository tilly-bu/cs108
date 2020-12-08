#forms.py 
from django import forms
from .models import Workout, Program

class UpdateProgramForm(forms.ModelForm): 
    'a form to add a workout day to our programs model' 

    class Meta: 
        'additional data to inform the form what model to update' 
        model = Program #which program to update
        fields = ['user','excercises','reps','sets','date'] #data attributes to pick


class CreateWorkoutForm(forms.ModelForm): 
    'a form to add an excercise to the workouts directory ' 

    class Meta: 
        'additional data for the form' 
        model = Workout 
        fields = ['name','description','image_url']
        