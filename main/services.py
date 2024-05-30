from django.db.models import Count
from datetime import timedelta
from .models import Sensor
from .utils import calculate_day_counts


def get_day_of_week_average_count(start_date, end_date):
    # Make end_date inclusive by adding one day to it
    end_date_inclusive = end_date + timedelta(days=1)

    # Calculate the number of occurrences of each day of the week in the date range
    day_counts = {i: 0 for i in range(1, 8)}
    current_date = start_date
    while current_date < end_date_inclusive:
        # Convert to 1-based index where Monday is 2
        day_of_week = current_date.isoweekday() % 7 + 1
        day_counts[day_of_week] += 1
        current_date += timedelta(days=1)

    response_data = []
    sensors = Sensor.objects.all()

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
