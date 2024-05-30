"""Views for the main app."""

from datetime import datetime
from django.http import JsonResponse
from django.utils import timezone
from .services import get_day_of_week_average_count


def traffic_day_of_week_average_count(request):
    """Get the average event count for each day of the week in the date range."""

    start_date_str = request.GET.get('start_date')
    end_date_str = request.GET.get('end_date')

    # Validate date format
    try:
        start_date = timezone.make_aware(
            datetime.strptime(start_date_str, '%Y-%m-%d'))
        end_date = timezone.make_aware(
            datetime.strptime(end_date_str, '%Y-%m-%d'))
    except (ValueError, TypeError):
        return JsonResponse({'error': 'Invalid date format. Use YYYY-MM-DD'}, status=400)

    try:
        response_data = get_day_of_week_average_count(start_date, end_date)
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'results': response_data})
