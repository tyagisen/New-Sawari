from django.db import models
from .validators import validate_number


class Driver(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10, unique=True, validators=[validate_number])
    vehicle_type = models.CharField(max_length=100)

    def __str__(self):
        return self.name
