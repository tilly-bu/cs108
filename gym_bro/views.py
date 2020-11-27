from django.shortcuts import render
from django.views.generic import TemplateView , ListView 
from .models import Workout

# Create your views here.

class HomePageView(TemplateView): 
    "specialized version of template view that will display our homepage"

    template_name = "gym_bro/Gym_Bro_Home_PageView.html" # template that is the homepage


class ExcerciseView (TemplateView): 
    "specialized template that will show us all the excercies that we have available" 

    template_name = "gym_bro/excercise.html"

class WorkoutsPageView (ListView): # list view allows us to represent many objects from the same model
    "show us a list of the Workouts hard coded into admin" 

    model = Workout
    template_name = "gym_bro/workouts.html"


    context_object_name = 'workouts' #remember lowercase w 
    # ^ name of the variable to call from templates 
    


