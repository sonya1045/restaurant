from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.TextField(unique=True)
    surname = models.TextField()
    phone_num = models.CharField(max_length=11)
    avatar = models.ImageField(upload_to='images/', default='images/avatar.png')
    REQUIRED_FIELDS = ['surname', 'phone_num']
    USERNAME_FIELD = 'name'

    def __str__(self):
        return f" {self.name} {self.surname}"

    class Meta:
        verbose_name = 'User'