"""Tests for the models in the main app."""

from django.test import TestCase
from main.utils import aware_datetime
from main.models import Sensor, SensorEvent


class SensorModelTests(TestCase):
    """Tests for the Sensor model."""

    def test_create_sensor(self):
        """Test creating a new sensor."""
        sensor = Sensor.objects.create(name="Test Sensor")
        self.assertEqual(sensor.name, "Test Sensor")
        self.assertIsInstance(sensor, Sensor)

    def test_sensor_string_representation(self):
        """Test the string representation of the sensor."""
        sensor = Sensor.objects.create(name="Test Sensor")
        self.assertEqual(str(sensor), "Test Sensor")


class SensorEventModelTests(TestCase):
    """Tests for the SensorEvent model."""

    def setUp(self):
        """Set up test data."""
        self.sensor = Sensor.objects.create(name="Test Sensor")

    def test_create_sensor_event(self):
        """Test creating a new sensor event."""
        event = SensorEvent.objects.create(
            sensor=self.sensor,
            event_datetime=aware_datetime(2023, 5, 15, 12, 0)
        )
        self.assertEqual(event.sensor, self.sensor)
        self.assertEqual(event.event_datetime, aware_datetime(2023, 5, 15, 12, 0))
        self.assertIsInstance(event, SensorEvent)

    def test_sensor_event_string_representation(self):
        """Test the string representation of the sensor event."""
        event = SensorEvent.objects.create(
            sensor=self.sensor,
            event_datetime=aware_datetime(2023, 5, 15, 12, 0)
        )
        expected_string = f"{self.sensor.name} event at 2023-05-15 12:00:00+00:00"
        self.assertEqual(str(event), expected_string)

    def test_sensor_event_delete(self):
        """Test deleting a sensor event."""
        event = SensorEvent.objects.create(
            sensor=self.sensor,
            event_datetime=aware_datetime(2023, 5, 15, 12, 0)
        )
        event.delete()
        self.assertEqual(SensorEvent.objects.count(), 0)
        self.assertEqual(Sensor.objects.count(), 1)
        self.assertEqual(Sensor.objects.first(), self.sensor)
        self.assertEqual(Sensor.objects.first().events.count(), 0)

    def test_sensor_with_event_delete(self):
        """Test deleting a sensor with associated events."""
        _ = SensorEvent.objects.create(
            sensor=self.sensor,
            event_datetime=aware_datetime(2023, 5, 15, 12, 0)
        )
        self.sensor.delete()

        # test that the sensor and event are deleted
        self.assertEqual(Sensor.objects.count(), 0)
        self.assertEqual(SensorEvent.objects.count(), 0)

    def test_create_sensor_event_with_deleted_sensor(self):
        """Test creating a new sensor event with a deleted sensor."""
        
        # 1. Create a sensor
        sensor = Sensor.objects.create(name="Test Sensor")

        # 2. Delete the sensor
        sensor.delete()

        # 3. Attempt to create a sensor event with the deleted sensor
        with self.assertRaises(ValueError):
            SensorEvent.objects.create(
                sensor=sensor,
                event_datetime=aware_datetime(2023, 5, 15, 12, 0)
            )
