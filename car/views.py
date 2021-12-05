from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from .forms import CarForm, CarPriceForm, CarGalleryForm
from .models import Cars, Brands, Colors


class CarRegistration(View):
    context = {
        'car_form': CarForm(use_required_attribute=False),
        'car_price': CarPriceForm(use_required_attribute=False),
        'upload_image': CarGalleryForm(use_required_attribute=False),
        'brands': Brands.objects.all().prefetch_related("brand_models"),
        'colors': Colors.objects.all(),
    }

    def get(self, request, *args, **kwargs):
        return render(request, 'car/create_Ad.html', self.context)

    def post(self, request, *args, **kwargs):
        self.context['car_form'] = CarForm(request.POST or None, use_required_attribute=False)
        self.context['car_price'] = CarPriceForm(request.POST or None, use_required_attribute=False)
        print(self.request.POST.get('image'))
        print(self.request.FILES.getlist('image'))
        image = CarGalleryForm(self.request.POST.get('image'), self.request.FILES)
        if image.is_valid():
            print('hello')
        return render(request, 'car/create_Ad.html', self.context)


class AdList(ListView):
    template_name = "car/Ad_list.html"
    queryset = Cars.objects.all()
