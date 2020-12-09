#forms.py 
from django import forms
from .models import Workout, Program , User

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


class CreateUserForm(forms.ModelForm): 
    ' a form to create users' 

    class Meta: 
        'additional Data for the form ' 
        model = User 
        fields = ['first_name','last_name','user_name'] 


class EditExcerciseForm(forms.ModelForm): 
    'a form to update an excercise to the workouts directory ' 

    class Meta: 
        'additional data for the form' 
        model = Workout 
        fields = ['name','description','image_url']





        
        