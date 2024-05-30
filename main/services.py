"""Service functions for the main app."""

from datetime import timedelta
from django.db.models import Count
from .models import Sensor
from .utils import calculate_day_counts


def get_day_of_week_average_count(start_date, end_date):
    """
    Get the average event count for each day of the week in the date range.

    Args:
      start_date (datetime.date): The start date of the date range.
      end_date (datetime.date): The end date of the date range.

    Returns:
      list: A list of dictionaries containing the average event count for each day of the week for each sensor.
        Each dictionary contains the following keys:
          - 'sensor_id': The ID of the sensor.
          - 'sensor_name': The name of the sensor.
          - 'mon_avg_count': The average event count for Monday.
          - 'tue_avg_count': The average event count for Tuesday.
          - 'wed_avg_count': The average event count for Wednesday.
          - 'thu_avg_count': The average event count for Thursday.
          - 'fri_avg_count': The average event count for Friday.
          - 'sat_avg_count': The average event count for Saturday.
          - 'sun_avg_count': The average event count for Sunday.
    
    Raises:
      ValueError: If the start_date is after the end_date.
    
    Note:
      Will return an empty list if the date range is empty/invalid, or if no sensors are found.
    """

    # Calculate the number of occurrences of each day of the week in the date range
    day_counts = calculate_day_counts(start_date, end_date)

    response_data = []
    sensors = Sensor.objects.all()

    # Make end_date inclusive by adding one day to it
    end_date_inclusive = end_date + timedelta(days=1)

    for sensor in sensors:
        sensor_data = {
            'sensor_id': sensor.id,
            'sensor_name': sensor.name,
            'mon_avg_count': 0,
            'tue_avg_count': 0,
            'wed_avg_count': 0,
            'thu_avg_count': 0,
            'fri_avg_count': 0,
            'sat_avg_count': 0,
            'sun_avg_count': 0,
        }

        # Perform the aggregation in the database with inclusive end date
        day_of_week_counts = sensor.events.filter(event_datetime__range=[start_date, end_date_inclusive]).values(
            'event_datetime__week_day').annotate(event_count=Count('id'))

        for count in day_of_week_counts:
            day_of_week = count['event_datetime__week_day']
            event_count = count['event_count']
            if day_counts[day_of_week] > 0:  # Avoid division by zero
                avg_count = round(event_count / day_counts[day_of_week])
                if day_of_week == 2:
                    sensor_data['mon_avg_count'] = avg_count
                elif day_of_week == 3:
                    sensor_data['tue_avg_count'] = avg_count
                elif day_of_week == 4:
                    sensor_data['wed_avg_count'] = avg_count
                elif day_of_week == 5:
                    sensor_data['thu_avg_count'] = avg_count
                elif day_of_week == 6:
                    sensor_data['fri_avg_count'] = avg_count
                elif day_of_week == 7:
                    sensor_data['sat_avg_count'] = avg_count
                elif day_of_week == 1:
                    sensor_data['sun_avg_count'] = avg_count

        response_data.append(sensor_data)

    return response_data
