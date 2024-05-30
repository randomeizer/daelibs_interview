"""Configuration of the admin interface for the main app."""

from django.contrib import admin
from .models import Sensor, SensorEvent

# Register your models here.


class SensorAdmin(admin.ModelAdmin):
    """Configuration for the Sensor model in the admin interface."""
    list_display = ('name',)
    search_fields = ('name',)


class SensorEventAdmin(admin.ModelAdmin):
    """Configuration for the SensorEvent model in the admin interface."""
    list_display = ('sensor', 'event_datetime')
    list_filter = ('sensor', 'event_datetime')
    search_fields = ('sensor__name', 'event_datetime')


admin.site.register(Sensor, SensorAdmin)
admin.site.register(SensorEvent, SensorEventAdmin)
