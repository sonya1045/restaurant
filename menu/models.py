from django.db import models
from django.contrib import admin

class Dish(models.Model):
    date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50)
    discriptions = models.CharField(max_length=1000)
    size = models.CharField(max_length=20, choices=[
        ('small', "Small"),
        ('medium', "Medium"),
        ('large', "Large"),
    ], default='small')
    photo = models.ImageField(upload_to='media/')
    category = models.CharField(max_length=20, choices=[
        ('all', "Усі страви"),
        ('first-dish', "Перші страви"),
        ('salad', "Салати"),
        ('dessert', "Десерти"),
        ('drinks', "Напої"),
    ], default='all')
    price = models.IntegerField(verbose_name='price')

    def __str__(self):
       return f"{self.title}"
     
    class Meta:
        verbose_name = 'Dishes'

    
