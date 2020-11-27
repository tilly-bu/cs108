from django.db import models

# Create your models here.

class Workout(models.Model): 
    "represents an excercise, an image of it and how to perform it" 

    # data attributes 
    name = models.TextField(blank=True) 
    description = models.TextField(blank=True) 
    image_url = models.URLField(blank=True)
    

    def __str__ (self): 
        "return a string representation of the excercise" 

        return f'{self.name}'



