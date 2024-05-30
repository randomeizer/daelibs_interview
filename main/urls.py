"""Defines URL patterns for main."""

from django.urls import path
from . import views

urlpatterns = [
    path('dayOfWeekAverageCount/', views.traffic_day_of_week_average_count,
         name='traffic_day_of_week_average_count'),
]
