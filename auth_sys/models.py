from django.db import models


class User(models.Model):
    name = models.TextField()
    surname = models.TextField()
    phone_num = models.IntegerField()
    avatar = models.ImageField(upload_to='images/', default='images/avatar.png')