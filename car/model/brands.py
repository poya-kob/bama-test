from django.db import models


class Brands(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = "brands"

    def __str__(self):
        return self.name
