from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib import admin

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email must be")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)
    
    
    
class CustomUser(AbstractUser):
    username = models.TextField()
    surname = models.TextField()
    phone_num = models.CharField(max_length=11, unique=True)
    avatar = models.ImageField(upload_to='media/', default='media/avatar.png')
    REQUIRED_FIELDS = ['surname', 'username']
    USERNAME_FIELD = 'phone_num'

    def __str__(self):
        return f" {self.username} {self.surname}"

    class Meta:
        verbose_name = 'User'


