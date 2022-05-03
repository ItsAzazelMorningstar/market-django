from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):


    email = models.EmailField('email address', unique=True)
    user_name = models. CharField(max_length=150, unique=True)
    first_name = models. CharField(max_length=150)
    start_date = models.DateTimeField(default=timezone.now)
    about = models. TextField('about', max_length=500, blank=True)
    is_staff = models. BooleanField(default=False)
    is_active = models. BooleanField(default=False)
