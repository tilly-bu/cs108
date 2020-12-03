from django.shortcuts import render
from django.views.generic import TemplateView , ListView , DetailView, CreateView
from .models import Workout , Program , User
import random
from .forms import UpdateProgramForm
# Create your views here.

class HomePageView(ListView): 
    "specialized version of template view that will display our homepage"

    model = User

    template_name = "gym_bro/Gym_Bro_Home_PageView.html" # template that is the homepage

    context_object_name = 'user_names'


class WorkoutsPageView (ListView): # list view allows us to represent many objects from the same model
    "show us a list of the Workouts hard coded into admin" 

    model = Workout
    template_name = "gym_bro/workouts.html"


    context_object_name = 'workouts' #remember lowercase w 
    # ^ name of the variable to call from templates 


class SingleWorkoutPageView (DetailView):
    "render a single workout by entering a pk"

    model = Workout
    template_name = "gym_bro/single_workout.html"


    context_object_name = 'workout' #singular , only 1


class RandomWorkoutPageView (DetailView):
    "display a random workout for inspiration"

    model = Workout
    template_name = "gym_bro/single_workout.html"


    context_object_name = 'workout' #singular , only 1

    def get_object(self): 
        "select a random workout to display"

        #obtain all workouts 
        all_workouts = Workout.objects.all()
        #select one at random 
        random_workout = random.choice(all_workouts) 

        return random_workout 


class ProgramPageView (ListView): 
    model = Program  #retrive the program objects from database
    template_name = "gym_bro/program.html" # delegate display to this url 
    context_object_name = "program" #use this variable name to call objects in the template 


class UserPageView (DetailView):
    "User page with program info and ability to update with new workouts"

    model = User
    template_name = "gym_bro/user_page.html"


    context_object_name = 'user_page' 

class UpdateProgramView(CreateView): 
    "update the program of a user"

    model = Program 
    form_class = UpdateProgramForm
    template_name = "gym_bro/update_program_form.html"




    




        


    


