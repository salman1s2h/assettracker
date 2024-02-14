from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    ROLE_CHOICES = [
        ('SA', 'System Admin'),
        ('OT', 'Gernal User'),
    ]

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=120)
    role = models.CharField(max_length=2, choices=ROLE_CHOICES,blank=True,null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"] ## when we want user and email both fields

    def __str__(self):
        return f"{self.name} {self.email}"
