import datetime

from django.db import models

from account.models import Customer
from .model_utils import create_year_choices


class Cars(models.Model):
    FUEL_CHOICES = [
        ('P', "Petrol"),
        ('C', "CNG"),
        ('H', "Hybrid"),
        ('D', "Diesel"),
    ]
    USED_TYPE_CHOICES = [
        ('N', "Never used"),  # صفر
        ('W', "worked"),  # کارکرده
        ('P', "Pre cell"),  # پیش فروش
        ('C', "Cortex"),  # کارتکس
        ('R', "Referred"),  # حواله
    ]
    HEALTH_TYPE = [
        ('G', 'Good'),
        ('D', 'Damaged'),
        ('U', 'Useless'),
    ]
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    brand_model = models.ForeignKey('BrandModels', on_delete=models.SET_NULL, null=True)
    year_of_create = models.IntegerField(choices=create_year_choices(1980), default=datetime.datetime.now().year)
    fuel_type = models.CharField(max_length=50, choices=FUEL_CHOICES, default='P')
    used_type = models.CharField(max_length=50, choices=USED_TYPE_CHOICES, default='N')
    kilometer_of_move = models.CharField(max_length=50, default='0', null=True, blank=True)
    body_health_type = models.CharField(max_length=50, choices=HEALTH_TYPE, default='G')
    descriptions = models.TextField()
    is_free_zone = models.BooleanField(default=False)
    body_color_type = models.ForeignKey('Colors', on_delete=models.SET_NULL, null=True,
                                        related_name="car_body_color")
    inside_color_type = models.ForeignKey('Colors', on_delete=models.SET_NULL, null=True,
                                          related_name="car_inside_color")
    price = models.OneToOneField('CarPrice', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'cars'

    def __str__(self):
        return f"{self.brand_model.brand.name} - {self.brand_model}"

    @property
    def car_name(self):
        return self.__str__()
