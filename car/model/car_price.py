from django.db import models

from car.utils import create_number_of_payments


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
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='A')
    price = models.PositiveBigIntegerField(null=True)
    prepayment = models.PositiveBigIntegerField(null=True)
    Amount_per_payment = models.PositiveBigIntegerField(null=True)
    second_prepayment = models.PositiveBigIntegerField(null=True)
    number_of_payments = models.CharField(max_length=50, choices=create_number_of_payments(10), null=True)
    delivery_time = models.IntegerField(choices=DELIVERY_CHOICES, default=1, null=True)
    payment_period = models.IntegerField(choices=PAYMENT_PERIOD_CHOICES, default=0, null=True)

    class Meta:
        managed = False
        db_table = 'car_price'

    def save(self, *args, **kwargs):
        if self.type == 'F' and not self.price:
            raise Exception("price is necessary for Fixed type")
        elif self.type == "A":
            self.price = 0

        super().save(*args, **kwargs)
