# file: gym_bro/urls.py
#description : direct URL requests to the desired functions 

from django.urls import path #django function that maps urls to functions
from .views import HomePageView , WorkoutsPageView , SingleWorkoutPageView

urlpatterns = [
    path ('',HomePageView.as_view(),name='home'),#view that maps the /gym_bro url to the view , and to the template of the same name as the view

    path ('workouts',WorkoutsPageView.as_view(),name='workouts'),
    path ('single_workout/<int:pk>',SingleWorkoutPageView.as_view(),name='One Workout'),
] 
