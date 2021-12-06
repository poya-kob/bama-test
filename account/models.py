from django.db import models
from django.contrib.auth.models import User


class Customer(User):
    is_Auto_Expo = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'customer'
