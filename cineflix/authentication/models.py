from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class RoleChoice(models.TextChoices):

    USER = 'User','User'

    ADMIN = 'Admin','Admin'

class profile(AbstractUser):

    role = models.CharField(max_length=10,choices=RoleChoice.choices)

    phone = models.CharField(null=True,blank=True)

    class Meta :

        verbose_name = 'Profiles'

        verbose_name_plural = 'Profiles'

    def __str__(self):
        return f'{self.username}'