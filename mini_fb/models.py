from django.db import models

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

        





# Create your models here.
