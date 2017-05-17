from django.db import models


class Venue(models.Model):
    name = models.CharField(max_length=30)
    lat = models.FloatField()
    lng = models.FloatField()
    device_id = models.CharField(max_length=30)
