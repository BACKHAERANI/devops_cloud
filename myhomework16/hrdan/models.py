from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    photo = models.ImageField(blank=True)
    description = models.TextField()
    address = models.CharField(max_length=100)
    latitude = models.FloatField(verbose_name="위도")
    longitude = models.FloatField(verbose_name="경도")
    telephone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
