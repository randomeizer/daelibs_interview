"""Tests for the views in the main app."""

import unittest
from unittest.mock import patch
from django.test import TestCase, Client
from django.urls import reverse
from main.utils import aware_datetime
from main.models import Sensor, SensorEvent


class TrafficDayOfWeekAverageCountTests(TestCase):
    """Tests for the traffic_day_of_week_average_count view."""

    def setUp(self):
        """Set up test data."""
        self.client = Client()
        # Ensure this matches the URL name in your urls.py
        self.url = reverse('traffic_day_of_week_average_count')

        self.sensor1 = Sensor.objects.create(name="Sensor 1")
        self.sensor2 = Sensor.objects.create(name="Sensor 2")

        SensorEvent.objects.create(
            sensor=self.sensor1, event_datetime=aware_datetime(2023, 5, 15, 12, 0))  # Monday
        SensorEvent.objects.create(
            sensor=self.sensor1, event_datetime=aware_datetime(2023, 5, 16, 12, 0))  # Tuesday
        SensorEvent.objects.create(
            sensor=self.sensor1, event_datetime=aware_datetime(2023, 5, 17, 12, 0))  # Wednesday
        SensorEvent.objects.create(
            sensor=self.sensor1, event_datetime=aware_datetime(2023, 5, 17, 14, 0))  # Wednesday
        SensorEvent.objects.create(
            sensor=self.sensor2, event_datetime=aware_datetime(2023, 5, 17, 12, 0))  # Wednesday
        SensorEvent.objects.create(
            sensor=self.sensor2, event_datetime=aware_datetime(2023, 5, 18, 12, 0))  # Thursday

    def test_valid_date_range(self):
        """Test the view with a valid date range."""
        response = self.client.get(
            self.url, {'start_date': '2023-05-15', 'end_date': '2023-05-21'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('results', response.json())

    def test_invalid_date_format(self):
        """Test the view with an invalid date format."""
        response = self.client.get(
            self.url, {'start_date': 'invalid-date', 'end_date': '2023-05-21'})
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())
        self.assertEqual(response.json()['error'],
                         'Invalid date format. Use YYYY-MM-DD')

    @patch('main.views.get_day_of_week_average_count')
    def test_service_error_handling(self, mock_get_day_of_week_average_count):
        """Test the view with a valid date range that triggers a service error."""
        mock_get_day_of_week_average_count.side_effect = ValueError(
            "Service error")

        response = self.client.get(
            self.url, {'start_date': '2023-05-15', 'end_date': '2023-05-21'})
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())
        self.assertEqual(response.json()['error'], 'Service error')


if __name__ == '__main__':
    unittest.main()
