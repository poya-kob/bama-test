from .forms import CarGalleryForm
from .models import CarGallery


def create_car_gallery(image_form, image_files, car_instance_id):
    image = CarGalleryForm(image_form, image_files)
    images = image_files.getlist('image')
    if image.is_valid():
        for pic in images:
            CarGallery.objects.create(car_id=car_instance_id.id, image=pic)
        return True
    return False


def keys_seprator(request, car_price_fields: list):
    price_dict = {}
    car_dict = {}
    for key in request.POST:
        if request.POST.get(key):
            if key in car_price_fields and request.POST.get(key):
                price_dict[key] = request.POST.get(key or None)
            elif key not in ['csrfmiddlewaretoken', 'image', 'brand']:
                car_dict[key] = request.POST.get(key or None)
    return price_dict, car_dict
