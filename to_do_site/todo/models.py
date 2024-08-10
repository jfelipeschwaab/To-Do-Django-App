from django.db import models
from datetime import datetime, time

def default_end_date():
    return datetime.combine(datetime.now().date(), time(23, 59))
# Create your models here.
class Note(models.Model):
    name_task = models.CharField(max_length=50)
    description = models.CharField(default=None,max_length= 300)
    created_date = models.DateField(auto_now=False, auto_now_add=True)
    end_date = models.DateTimeField(default=default_end_date)
    
    def __str__(self):
        return self.name_task
