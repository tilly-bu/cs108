from django.db import models
import datetime
from django.urls import reverse

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

    def  get_absolute_url(self): 
        'provide a URL to show the desired object' 

        return 'workouts'

class Program(models.Model):
    "represents the excercies that a user has completed and the date of completion" 

    user = models.ForeignKey('User', on_delete=models.CASCADE) 
    excercises = models.ForeignKey(Workout, on_delete=models.CASCADE)
    reps = models.IntegerField (blank=True)
    sets = models.IntegerField (blank=True) #is there a way to add numeric feilds ?
    date = models.DateField (blank=True,default=datetime.date.today)

    # def get_program_data(self): 
    #     "return all the data from to Programs model associated with this person"

    #     # use object manager to filter program data objects associated with the Users PK

    #     return Program.objects.filter(user=reverse(kwargs={'pk':self.pk})) 

    def  get_absolute_url(self): 
        'provide a URL to show the desired object' 

        #'program/<int:pk>'

        return reverse('program', kwargs={'pk':self.pk})

    
    def __str__ (self): 
        return f'Today we did: {self.excercises}'

class User(models.Model): 
    "represents a single users information, and the relationship between the user and the program"

    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    user_name = models.TextField(blank=True)

    def __str__ (self): 
        "return a string representation of the first name"

        return f'{self.user_name}'

    def get_program_data(self): 
        "return all the data from to Programs model associated with this person"

        # use object manager to filter program data objects associated with the Users PK

        return Program.objects.filter(user=self) 

    def  get_absolute_url(self): 
        'provide a URL to show the desired object' 

        return 'home'

    

