from django.db import models


class Colors(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    class Meta:
        managed = False
        db_table = 'colors'

    def __str__(self):
        return self.name
