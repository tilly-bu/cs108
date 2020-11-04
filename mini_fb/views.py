from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Profile

# Create your views here.

class ShowAllProfilesView(ListView):
    """list of all the profiles""" 
    model = Profile
    template_name = "mini_fb/show_all_profiles.html"
    context_object_name = "profiles" #list containing profiles from data base?

class ShowProfilePageView(DetailView): 
    '''Display a single profile'''
    model = Profile
    template_name = 'mini_fb/show_profile_page.html'
    context_object_name = 'Profile' 




