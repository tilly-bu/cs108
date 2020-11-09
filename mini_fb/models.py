from django.db import models

import time

class Profile (models.Model):
    """ will represent a profile consisting of First name, last name , email address and profile image"""

    #data attributes
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    email_address=models.TextField(blank=True) 
    img_src = models.URLField (blank=True) 

    def __str__(self): 
        "return string representation of the data attributes" 

        return f'First Name: {self.first_name} ,Last Name: {self.last_name} , e-mail: {self.email_address}: {self.img_src}'

    # def get_absolute_url(self): 
    #     "Provide a URL to show this object"
    #     return reverse ('quote', kwargs={'pk'}
        

# class StatusMessage (models.Model): 
#     """status message""" 
#     message = models.TextField(blank=True)
#     profile = models.ForeignKey('Profile', on_delete=models.CASCADE)

#     def __str__ (self): 
#         return f'{self.message} ,' %time.ctime()




