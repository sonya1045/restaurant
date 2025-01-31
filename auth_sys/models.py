from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.TextField()
    surname = models.TextField()
    phone_num = models.CharField(max_length=11, unique=True)
    avatar = models.ImageField(upload_to='images/', default='images/avatar.png')
    REQUIRED_FIELDS = ['surname', 'name']
    USERNAME_FIELD = 'phone_num'

    def __str__(self):
        return f" {self.name} {self.surname}"

    class Meta:
        verbose_name = 'User'