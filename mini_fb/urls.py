
from django.urls import path
from .views import * #ShowAllProfilesView, ShowProfilePageView  #our view class definition -> connects the model to the template 

urlpatterns =  [
    path('', ShowAllProfilesView.as_view(), name="profile_page"),
    path('Profile/<int:pk>', ShowProfilePageView.as_view(), name="show_profile_page"),
    path('create_profile', CreateProfileView.as_view(), name="create_profile"), 
    path('Profile/<int:pk>/update', UpdateProfileView.as_view(), name="update_profile"),
    path('Profile/<int:pk>/post_status_message', post_status_message, name="create_status_form"),

]