from django.db import models
from django.contrib.postgres.fields import JSONField


class Event(models.Model):
    venue = models.ForeignKey('Venue', on_delete=models.CASCADE, related_name='events')
    timestamp = models.DateTimeField(auto_now=True)
    data = JSONField()
