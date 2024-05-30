from django.test import TestCase
from main.utils import aware_datetime
from main.models import Sensor, SensorEvent
from main.services import get_day_of_week_average_count


class GetDayOfWeekAverageCountTests(TestCase):
    """Tests for the get_day_of_week_average_count function in the services module."""

    def setUp(self):
        """Set up test data."""
        Sensor.objects.all().delete()
        SensorEvent.objects.all().delete()

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

    def test_get_day_of_week_average_count(self):
        """Test the get_day_of_week_average_count function."""
        start_date = aware_datetime(2023, 5, 15).date()
        end_date = aware_datetime(2023, 5, 21).date()

        expected = [
            {
                'sensor_id': self.sensor1.id,
                'sensor_name': self.sensor1.name,
                'mon_avg_count': 1,
                'tue_avg_count': 1,
                'wed_avg_count': 2,
                'thu_avg_count': 0,
                'fri_avg_count': 0,
                'sat_avg_count': 0,
                'sun_avg_count': 0,
            },
            {
                'sensor_id': self.sensor2.id,
                'sensor_name': self.sensor2.name,
                'mon_avg_count': 0,
                'tue_avg_count': 0,
                'wed_avg_count': 1,
                'thu_avg_count': 1,
                'fri_avg_count': 0,
                'sat_avg_count': 0,
                'sun_avg_count': 0,
            }
        ]

        result = get_day_of_week_average_count(start_date, end_date)
        self.assertEqual(result, expected)

    def test_get_day_of_week_average_count_invalid_range(self):
        """Test the get_day_of_week_average_count function with an invalid date range."""
        start_date = aware_datetime(2023, 5, 21).date()
        end_date = aware_datetime(2023, 5, 20).date()

        with self.assertRaises(ValueError):
            get_day_of_week_average_count(start_date, end_date)
    
    def test_get_day_of_week_average_count_no_sensors(self):
        """Test the get_day_of_week_average_count function with no sensors."""
        Sensor.objects.all().delete()

        start_date = aware_datetime(2023, 5, 15).date()
        end_date = aware_datetime(2023, 5, 21).date()

        result = get_day_of_week_average_count(start_date, end_date)
        self.assertEqual(result, [])

    def test_get_day_of_week_average_count_no_events(self):
        """Test the get_day_of_week_average_count function with no events."""
        SensorEvent.objects.all().delete()

        start_date = aware_datetime(2023, 5, 15).date()
        end_date = aware_datetime(2023, 5, 21).date()

        result = get_day_of_week_average_count(start_date, end_date)

        expected = [
            {
                'sensor_id': self.sensor1.id,
                'sensor_name': self.sensor1.name,
                'mon_avg_count': 0,
                'tue_avg_count': 0,
                'wed_avg_count': 0,
                'thu_avg_count': 0,
                'fri_avg_count': 0,
                'sat_avg_count': 0,
                'sun_avg_count': 0,
            },
            {
                'sensor_id': self.sensor2.id,
                'sensor_name': self.sensor2.name,
                'mon_avg_count': 0,
                'tue_avg_count': 0,
                'wed_avg_count': 0,
                'thu_avg_count': 0,
                'fri_avg_count': 0,
                'sat_avg_count': 0,
                'sun_avg_count': 0,
            }
        ]

        self.assertEqual(result, expected)

    def test_get_day_of_week_average_count_single_day(self):
        """Test the get_day_of_week_average_count function with a single day range."""
        start_date = aware_datetime(2023, 5, 15).date()
        end_date = aware_datetime(2023, 5, 15).date()

        expected = [
            {
                'sensor_id': self.sensor1.id,
                'sensor_name': self.sensor1.name,
                'mon_avg_count': 1,
                'tue_avg_count': 0,
                'wed_avg_count': 0,
                'thu_avg_count': 0,
                'fri_avg_count': 0,
                'sat_avg_count': 0,
                'sun_avg_count': 0,
            },
            {
                'sensor_id': self.sensor2.id,
                'sensor_name': self.sensor2.name,
                'mon_avg_count': 0,
                'tue_avg_count': 0,
                'wed_avg_count': 0,
                'thu_avg_count': 0,
                'fri_avg_count': 0,
                'sat_avg_count': 0,
                'sun_avg_count': 0,
            }
        ]

        result = get_day_of_week_average_count(start_date, end_date)
        self.assertEqual(result, expected)
