from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    profile = models.CharField(max_length=1500)

# Create your models here.
