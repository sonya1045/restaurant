from django.db import models

class Dish(models.Model):
    date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=20)
    discriptions = models.CharField(max_length=100)
    size = models.CharField(max_length=20, choices=[
        ('small', "Small"),
        ('medium', "Medium"),
        ('large', "Large"),
    ], default='small')
    
