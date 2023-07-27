from django.db import models

# Create your models here.
class Car(models.Model):
    car_name = models.CharField(max_length=70)
    created_date = models.DateTimeField("Date announced")


class CarModel(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    car_model = models.CharField(max_length=50)
