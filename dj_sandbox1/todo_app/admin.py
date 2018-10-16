from django.contrib import admin

from .models import Task

admin.site.register(Task) #register the Task class to be accessible from admin panel

