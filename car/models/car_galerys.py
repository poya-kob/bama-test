from django.db import models

from .model_utils import upload_image_path
from .cars import Cars


class CarGallery(models.Model):
    image = models.ImageField(upload_to=upload_image_path, blank=True, null=True)
    car = models.ForeignKey(Cars, related_name="car_image", on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'car_gallery'

    def __str__(self):
        return self.car
