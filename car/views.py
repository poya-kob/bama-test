from django.shortcuts import render, redirect, reverse
from django.views import View
from django.views.generic import ListView, DetailView

from .forms import CarForm, CarPriceForm, CarGalleryForm
from .models import Cars, Brands, Colors, CarPrice
from .utils import keys_seprator, create_car_gallery


class CarRegistration(View):
    context = {
        'car_form': CarForm(use_required_attribute=False),
        'car_price': CarPriceForm(use_required_attribute=False),
        'upload_image': CarGalleryForm(use_required_attribute=False),
        'brands': Brands.objects.all(),
        'colors': Colors.objects.all(),
    }

    def get(self, request, *args, **kwargs):
        return render(request, 'car/create_Ad.html', self.context)

    def post(self, request, *args, **kwargs):
        self.context['car_form'] = CarForm(request.POST or None, use_required_attribute=False)
        self.context['car_price'] = CarPriceForm(request.POST or None, use_required_attribute=False)
        price_dict, car_dict = keys_seprator(request, CarPriceForm.Meta.fields)

        price_ins = CarPrice.objects.create(**price_dict)
        car_ins = Cars.objects.create(price_id=price_ins.id, user_id=request.user_obj.id,
                                      brand_model_id=car_dict.pop('brand_model'),
                                      body_color_type_id=car_dict.pop('body_color'),
                                      inside_color_type_id=car_dict.pop('inside_color'), **car_dict)
        done = create_car_gallery(self.request.POST.get('image'), self.request.FILES, car_ins)
        if done:
            return redirect(reverse('adlist'))
        return render(request, 'car/create_Ad.html', self.context)


class AdList(ListView):
    template_name = "car/Ad_list.html"
    queryset = Cars.objects.all()
    context_object_name = 'cars'
    paginate_by = 5


class AdDetail(DetailView):
    template_name = "car/Ad_detail.html"
    queryset = Cars.objects.all()
    context_object_name = 'car'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = context['car']
        context['related_ads'] = Cars.objects.filter(brand_model__brand=car.brand_model.brand).order_by('?')[:4]
        return context
