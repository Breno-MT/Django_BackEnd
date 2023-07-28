import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Car(models.Model):
    car_name = models.CharField(max_length=70)
    created_date = models.DateTimeField("Date announced")

    def was_created_recently(self):
        return self.created_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.car_name


class CarModel(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    car_model = models.CharField(max_length=50)

    def __str__(self):
        return self.car_model
