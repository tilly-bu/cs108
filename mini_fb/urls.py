
from django.urls import path
from .views import ShowAllProfilesView, ShowProfilePageView  #our view class definition -> connects the model to the template 

urlpatterns =  [
    path('All', ShowAllProfilesView.as_view(), name="profile_page"),
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name="show_profile_page"),

]