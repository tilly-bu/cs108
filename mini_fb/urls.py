
from django.urls import path
from .views import * #ShowAllProfilesView, ShowProfilePageView  #our view class definition -> connects the model to the template 

urlpatterns =  [
    path('', ShowAllProfilesView.as_view(), name="profile_page"),
    path('Profile/<int:pk>', ShowProfilePageView.as_view(), name="show_profile_page"),
    path('create_profile', CreateProfileView.as_view(), name="create_profile"), 
    path('Profile/<int:pk>/update', UpdateProfileView.as_view(), name="update_profile"),
    path('Profile/<int:pk>/post_status_message', post_status_message, name="create_status_form"),
    path('Profile/<int:pk>/delete_status', DeleteStatusMessageView.as_view(), name="delete_status"),
    path('Profile/<int:pk>/news_feed', ShowNewsFeedView.as_view(), name="news_feed"),
    #path('Profile/<int:pk>/show_possible_friends', ShowPossibleFriendsView.as_view(), name="show_possible_friends"),
]