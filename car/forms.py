from django.forms import ModelForm
from django import forms

from .models import Cars, CarPrice


class CarForm(ModelForm):
    class Meta:
        model = Cars
        fields = ['year_of_create', 'fuel_type', 'used_type', 'kilometer_of_move', 'body_health_type', 'descriptions',
                  'is_free_zone']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name == 'is_free_zone':
                visible.field.widget.attrs['class'] = 'class="form-group checkbox accessories_list"'
            else:
                visible.field.widget.attrs['class'] = 'form-control white_bg'


class CarPriceForm(ModelForm):
    class Meta:
        model = CarPrice
        fields = ['type', 'price', 'prepayment', 'Amount_per_payment', 'second_prepayment', 'number_of_payments',
                  'delivery_time', 'payment_period']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            # visible.field.widget = forms.HiddenInput()
            visible.field.widget.attrs['class'] = 'form-control white_bg'
            # visible.field.widget.attrs['style'] = "display: none;"


class CarGalleryForm(forms.Form):
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
