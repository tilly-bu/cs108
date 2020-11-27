from django.shortcuts import render
from django.views.generic import TemplateView , ListView , DetailView
from .models import Workout

# Create your views here.

class HomePageView(TemplateView): 
    "specialized version of template view that will display our homepage"

    template_name = "gym_bro/Gym_Bro_Home_PageView.html" # template that is the homepage



class WorkoutsPageView (ListView): # list view allows us to represent many objects from the same model
    "show us a list of the Workouts hard coded into admin" 

    model = Workout
    template_name = "gym_bro/workouts.html"


    context_object_name = 'workouts' #remember lowercase w 
    # ^ name of the variable to call from templates 


class SingleWorkoutPageView (DetailView):

    model = Workout
    template_name = "gym_bro/single_workout.html"


    context_object_name = 'workout' #singular , only 1

    


