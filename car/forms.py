from django.forms import ModelForm
from .models import Cars, CarPrice


class CarForm(ModelForm):
    class Meta:
        model = Cars
        fields = ['year_of_create', 'fuel_type', 'used_type', 'kilometer_of_move', 'body_health_type', 'descriptions',
                  'is_free_zone']


class CarPriceForm(ModelForm):
    class Meta:
        model = CarPrice
        fields = ['type', 'price', 'prepayment', 'Amount_per_payment', 'second_prepayment', 'number_of_payments',
                  'delivery_time', 'payment_period']
