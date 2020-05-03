from django.db import models


# Create your models here.

class Model(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.FloatField()
    image_url = models.CharField(max_length=2083)


class Offer(models.Model):
    code = models.CharField(max_length=255)
    discount = models.FloatField()
    description = models.CharField(max_length=2083)
