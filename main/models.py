from django.db import models


class Sensor(models.Model):
    """A sensor model."""

    name = models.CharField(max_length=45, null=False, blank=False)
    """str: The name of the sensor."""

    def __str__(self):
        return self.name


class SensorEvent(models.Model):
    """A sensor event model."""

    sensor = models.ForeignKey(
        Sensor, on_delete=models.CASCADE, related_name='events')
    """Sensor: The sensor that generated the event."""

    event_datetime = models.DateTimeField(null=False, blank=False)
    """datetime: The date and time the event occurred."""

    def __str__(self):
        return f"{self.sensor.name} event at {self.event_datetime}"
