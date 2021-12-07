from django.db import models

from .brands import Brands


class BrandModels(models.Model):
    name = models.CharField(max_length=50)
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE, related_name="brand_models")

    class Meta:
        managed = False
        db_table = 'brand_models'

    def __str__(self):
        return self.name
