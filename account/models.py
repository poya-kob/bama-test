from django.db import models
from django.contrib.auth.models import User


class Users(User):
    is_Auto_Expo = models.BooleanField(default=False)
