# models.py
from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=45, null=False, blank=False)


class SensorEvent(models.Model):
    sensor = models.ForeignKey(
        Sensor, on_delete=models.CASCADE, related_name='events')
    event_datetime = models.DateTimeField(null=False, blank=False)
