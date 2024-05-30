from django.db import models

# Create your models here.

class Sensor(models.Model):
    name = models.CharField(max_length=45, null=False, blank=False)


class SensorEvent(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    event_datetime = models.DateTimeField(null=False, blank=False)