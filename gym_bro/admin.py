from django.contrib import admin

# Register your models here.
from .models import Workout, User , Program

admin.site.register(Workout) 
admin.site.register(User)
admin.site.register(Program)



