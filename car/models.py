from django.db import models

from .utils import create_year_choices, create_number_of_payments, upload_image_path
from account.models import Users


class Brands(models.Model):
    name = models.CharField(max_length=50)


class BrandModels(models.Model):
    name = models.CharField(max_length=50)
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE, related_name="brand_models")


class Colors(models.Model):
    name = models.CharField(max_length=50)


class CarPrice(models.Model):
    DELIVERY_CHOICES = [
        (1, "1 day"),
        (7, "7 day"),
        (12, "12 day"),
        (20, "20 day"),
        (30, "30 day"),
        (45, "45 day"),
    ]
    PAYMENT_PERIOD_CHOICES = [
        (0, 'every month '),
        (2, 'every 2 month '),
        (3, 'every 3 month '),
        (4, 'every 4 month '),
    ]
    TYPE_CHOICES = [
        ("F", "Fixed"),  # مقطوع
        ("A", "Agreement"),  # توافقی
        ("I", "Installments"),  # اقساطی
    ]
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    price = models.PositiveBigIntegerField()
    prepayment = models.PositiveBigIntegerField()
    Amount_per_payment = models.PositiveBigIntegerField()
    second_prepayment = models.PositiveBigIntegerField()
    number_of_payments = models.CharField(max_length=50, choices=create_number_of_payments(10))
    delivery_time = models.IntegerField(choices=DELIVERY_CHOICES)
    payment_period = models.IntegerField(choices=PAYMENT_PERIOD_CHOICES)

    def save(self, *args, **kwargs):
        if self.type == 'F' and not self.price:
            raise Exception("price is necessary for Fixed type")
        if self.type == "A":
            self.price = 0
        super().save(*args, **kwargs)


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
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    brand_model = models.ForeignKey(Brands, on_delete=models.SET_NULL, null=True)
    year_of_create = models.IntegerField(choices=create_year_choices(1980))
    fuel_type = models.CharField(max_length=50, choices=FUEL_CHOICES)
    used_type = models.CharField(max_length=50, choices=USED_TYPE_CHOICES)
    kilometer_of_move = models.CharField(max_length=50, default='0', null=True, blank=True)
    body_health_type = models.CharField(max_length=50, choices=HEALTH_TYPE)
    descriptions = models.TextField()
    is_free_zone = models.BooleanField(default=False)
    body_color_type = models.ForeignKey(Colors, on_delete=models.SET_NULL, null=True, related_name="car_body_color")
    inside_color_type = models.ForeignKey(Colors, on_delete=models.SET_NULL, null=True, related_name="car_inside_color")
    price = models.OneToOneField(CarPrice, on_delete=models.CASCADE)


class CarGallery(models.Model):
    image = models.ImageField(upload_to=upload_image_path, blank=True, null=True)
    car = models.OneToOneField(Cars, related_name="car_image", on_delete=models.CASCADE)
