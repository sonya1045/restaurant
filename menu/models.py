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
    photo = models.ImageField(upload_to='images/')
    category = models.CharField(max_length=20, choices=[
        ('all', "Усі страви"),
        ('first-dish', "Перші страви"),
        ('salad', "Салати"),
        ('dessert', "Десерти"),
        ('drinks', "Напої"),
    ], default='all')
    
