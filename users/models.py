from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    college = models.CharField(max_length=100)
    student_id = models.CharField(max_length=100)
    tel = models.CharField(max_length=11)

    class Meta(AbstractUser.Meta):
        pass