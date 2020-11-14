from django.db import models

import time

from django.urls import reverse

class Profile (models.Model):
    """ will represent a profile consisting of First name, last name , email address and profile image"""

    #data attributes
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    email_address=models.TextField(blank=True) 
    img_src = models.URLField (blank=True) 
    friends = models.ManyToManyField("self")
    


    def __str__(self): 
        "return string representation of the data attributes" 

        return f'{self.first_name} ,{self.last_name} ,'
    
    def get_absolute_url(self):
        'provide a URL to show the object'

        #Profile/<int:pk>
        return reverse('Profile',kwargs={'pk',self.pk})

    def get_status_messages(self): 
        'will vall the status messages'
        status = StatusMessage.objects.filter(profile=self.pk)

        return status

    def get_friends (self): 
        return self.friends.all() 

    def get_news_feed(self):
        'render a news feed of statuses ordered by time posted'
        news = StatusMessage.objects.filter(profile=self.pk).order_by(-"timestamp")

        return news


    def get_friend_suggestions(self): 
        'will suggest possible friends'

        possible_friends = friend_suggestions = Profile.objects.all()

        return possible_friends 
        

        
    # def get_absolute_url(self): 
    #     "Provide a URL to show this object"
    #     return reverse ('quote', kwargs={'pk'}
        

class StatusMessage (models.Model): 
    """status message""" 
    message = models.TextField(blank=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    time_stamp= models.DateTimeField(auto_now=True)
    img_file = models.ImageField(blank=True)

    def __str__ (self): 
        return f'{self.message}'




