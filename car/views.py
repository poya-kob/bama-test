from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from .forms import CarForm, CarPriceForm
from .models import Cars


class CarRegistration(View):

    def get(self, request, *args, **kwargs):
        car_form = CarForm()
        car_price = CarPriceForm()
        context = {
            'car_form': car_form,
            'car_price': car_price

        }
        return render(request, 'car/create_Ad.html', context)


class AdList(ListView):
    template_name = "car/Ad_list.html"
    queryset = Cars.objects.all()
