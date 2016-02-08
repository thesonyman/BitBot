# Main models module to represent in to database

from django.db import models

class Parameter(models.Model):
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name + " : " + self.value;