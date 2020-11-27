# file: gym_bro/urls.py
#description : direct URL requests to the desired functions 

from django.urls import path #django function that maps urls to functions
from .views import HomePageView , ExcerciseView

urlpatterns = [
    path ('',HomePageView.as_view(),name='home'),#view that maps the /gym_bro url to the view , and to the template of the same name as the view
    path ('excercise',ExcerciseView.as_view(),name='excercise'), 
] 
