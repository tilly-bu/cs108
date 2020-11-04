from django.db import models

# Create your models here.
class Quote(models.Model): 
    """represents a quoute attributable to a famous person""" 
    
    #data attribultes 
    text = models.TextField(blank=True) # allows us to have a blank feild without breaking the database 
    author = models.TextField(blank=True) 
    image_url = models.URLField (blank=True) # feild that will accept image url 

    #!! remember any time you change a model you have to make a migration : makemigration then migrate{}

    #produce a string representation of this object 
    def __str__(self): 
        """return a formatted string that will output the data attributes"""

        return f'{self.text} - {self.author}'