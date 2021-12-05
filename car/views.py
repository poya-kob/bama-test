from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from .forms import CarForm, CarPriceForm, CarGalleryForm
from .models import Cars, Brands, Colors, CarPrice


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
        # self.context['car_form'] = CarForm(request.POST or None, use_required_attribute=False)
        # self.context['car_price'] = CarPriceForm(request.POST or None, use_required_attribute=False)
        price_dict = {}
        car_dict = {}
        for key in request.POST:
            if request.POST.get(key):
                if key in CarPriceForm.Meta.fields and request.POST.get(key):
                    price_dict[key] = request.POST.get(key or None)
                elif key not in ['csrfmiddlewaretoken', 'image', 'brand']:
                    car_dict[key] = request.POST.get(key or None)

        price_ins = CarPrice.objects.create(**price_dict)
        car_ins = Cars.objects.create(price_id=price_ins.id, user_id=request.user_obj.id,
                                      brand_model_id=car_dict.pop('brand_model'),
                                      body_color_type_id=car_dict.pop('body_color'),
                                      inside_color_type_id=car_dict.pop('inside_color'), **car_dict)
        print(car_ins)
        image = CarGalleryForm(self.request.POST.get('image'), self.request.FILES)
        images = self.request.FILES.getlist('image')
        if image.is_valid():
            for image in images:
                pass
        return render(request, 'car/create_Ad.html', self.context)


class AdList(ListView):
    template_name = "car/Ad_list.html"
    queryset = Cars.objects.all()
