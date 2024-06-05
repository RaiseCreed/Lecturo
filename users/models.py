from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    mobile = models.CharField(max_length=50,blank=True)
    location = models.CharField(max_length=50,blank=True)
    department = models.CharField(max_length=50,blank=True)
    lecturer_id = models.CharField(max_length=50,blank=True)
    working_hours = models.CharField(max_length=50,blank=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"