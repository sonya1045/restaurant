from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
import sys
# Create your models here.

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=64, blank=False, null=False)
    last_name = models.CharField(max_length=64, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    
    avatar = models.ImageField(upload_to='images/avatars/', default='images/avatars/default.jpg')
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.username

    def save(self, *args, **kwargs):
        # Якщо є нова аватарка
        if self.avatar:
            # Відкриваємо зображення
            img = Image.open(self.avatar)
            
            # Конвертуємо в RGB якщо потрібно
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Зберігаємо в буфер
            output = BytesIO()
            img.save(output, format='JPEG', quality=90)
            output.seek(0)
            
            # Замінюємо оригінальний файл на оброблений
            self.avatar = InMemoryUploadedFile(
                output,
                'ImageField',
                f"{self.avatar.name.split('.')[0]}.jpg",
                'image/jpeg',
                sys.getsizeof(output),
                None
            )
            
        super().save(*args, **kwargs)

class SavedAccount(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='saved_accounts')
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128)  # Зберігаємо незашифрований пароль
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'username')