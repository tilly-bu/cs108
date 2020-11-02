
from django.urls import path
from .views import HomePageView  #our view class definition -> connects the model to the template 

urlpatterns =  [
    path('', HomePageView.as_view(), name="home_page"),
]
