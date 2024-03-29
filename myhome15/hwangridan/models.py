from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    photo = models.ImageField(blank=True)
    address = models.CharField(max_length=100)
    latitude = models.FloatField(verbose_name="위도")
    longitude = models.FloatField(verbose_name="경도")
    telephone = models.CharField(max_length=15)

