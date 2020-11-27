
from django.urls import path 
from .views import HomePageView, AboutPageView 

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('about',AboutPageView.as_view(), name='about'),
]

#path('url that will refer',viewclass from views file.as_view(),name=give url a name) 
