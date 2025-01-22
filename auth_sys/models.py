from django.db import models


class User(models.Model):
    name = models.TextField()
    surname = models.TextField()
    phone_num = models.CharField(max_length=11)
    avatar = models.ImageField(upload_to='images/', default='images/avatar.png')

    def __str__(self):
        return f" {self.name} {self.surname}"

    class Meta:
        verbose_name = 'User'