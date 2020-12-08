# file: gym_bro/urls.py
#description : direct URL requests to the desired functions 

from django.urls import path #django function that maps urls to functions
from .views import * # HomePageView , WorkoutsPageView , SingleWorkoutPageView,RandomWorkoutPageView

urlpatterns = [
    path ('',HomePageView.as_view(),name='home'),#view that maps the /gym_bro url to the view , and to the template of the same name as the view
    path ('workouts',WorkoutsPageView.as_view(),name='workouts'),
    path ('single_workout/<int:pk>',SingleWorkoutPageView.as_view(),name='One Workout'),
    path ('random',RandomWorkoutPageView.as_view(), name='random'),
    path ('program/<int:pk>',ProgramPageView.as_view(),name='program'),
    path ('user_page/<int:pk>',UserPageView.as_view(),name='user_page'),
    path ('update_program',UpdateProgramView.as_view(),name='update_program'),
    path ('create_workout',CreateWorkoutView.as_view(),name='create_workout'),
] 


