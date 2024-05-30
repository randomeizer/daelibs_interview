from datetime import datetime
from django.http import JsonResponse
from .services import get_day_of_week_average_count

def traffic_day_of_week_average_count(request):
    start_date_str = request.GET.get('start_date')
    end_date_str = request.GET.get('end_date')

    # Validate date format
    try:
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
    except (ValueError, TypeError):
        return None, JsonResponse({'error': 'Invalid date format. Use YYYY-MM-DD'}, status=400)

    response_data = get_day_of_week_average_count(start_date, end_date)

    return JsonResponse({'results': response_data})
