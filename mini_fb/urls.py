
from django.urls import path
from .views import ShowAllProfilesView  #our view class definition -> connects the model to the template 

urlpatterns =  [
    path('', ShowAllProfilesView.as_view(), name="profile_page"),

]