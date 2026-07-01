from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.CharField(max_length=200, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True)

    class Meta:
        verbose_name='Пользователь'
        verbose_name_plural = 'Пользоавтели'
        indexes = [
            models.Index(fields=['username']),
            models.Index(fields=['email'])
        ]