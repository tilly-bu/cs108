from django.db import models
import random

# Create your models here.
class Person(models.Model):
    "represent a single person that said something nootable"

    name=models.TextField(blank=True)

    def __str__ (self): 
        return self.name
   
    def get_random_image(self):
        "return a string of img url of this person"
        images = Image.objects.filter(person=self.pk) # why is there this error? 

        #select one at random 
        return random.choice(images)

class Quote(models.Model): 
    """represents a quoute attributable to a famous person""" 
    
    #data attribultes 
    text = models.TextField(blank=True) # allows us to have a blank feild without breaking the database 
    person = models.ForeignKey('Person', on_delete=models.CASCADE) 

    #produce a string representation of this object 
    def __str__(self): 
        """return a formatted string that will output the data attributes"""

        return f'{self.text}'



class Image(models.Model): 
    '''represent the image URL for a person''' 

    image_url = models.URLField (blank=True) # feild that will accept image url 
    person = models.ForeignKey('Person', on_delete=models.CASCADE) 

    def __str__ (self):
        'return the image url'
        return self.image_url 



