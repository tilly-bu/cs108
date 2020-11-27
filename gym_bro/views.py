from django.shortcuts import render
from django.views.generic import TemplateView # generic view to display a simple webpage

# Create your views here.

class HomePageView(TemplateView): 
    "specialized version of template view that will display our homepage"

    template_name = "gym_bro/Gym_Bro_Home_PageView.html" # template that is the homepage


class ExcerciseView (TemplateView): 
    "specialized template that will show us all the excercies that we have available" 

    template_name = "gym_bro/excercise.html"
     

