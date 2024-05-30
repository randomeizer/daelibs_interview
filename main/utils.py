"""Utility functions for the main app."""

from datetime import datetime as dt
from django.utils import timezone


def aware_datetime(*args, **kwargs) -> dt:
    """Create a timezone-aware datetime object.

    Args:
        *args: Positional arguments for datetime.datetime.
        **kwargs: Keyword arguments for datetime.datetime.

    Returns:
        datetime: A timezone-aware datetime object.
    """
    naive_dt = dt(*args, **kwargs)
    return timezone.make_aware(naive_dt)


def calculate_day_counts(start_date, end_date):
    """Calculate the number of each day of the week in a date range.

    Args:
      start_date (datetime.date): The start date of the range (inclusive).
      end_date (datetime.date): The end date of the range (inclusive).

    Returns:
      dict: A dictionary containing the count of each day of the week in the range.
          The keys represent the day of the week (1 for Monday, 2 for Tuesday, etc.)
          and the values represent the count of that day in the range.
    """

    # If the range is empty, throw a ValueError
    if start_date > end_date:
        raise ValueError("Start date must be before or equal to end date.")

    day_counts = {i: 0 for i in range(1, 8)}

    # Total number of days in the range
    total_days = (end_date - start_date).days + 1

    # First day of the week in the range
    # Convert to 1-based index where Monday is 2
    start_day = start_date.isoweekday() % 7 + 1

    # Full weeks in the range
    full_weeks = total_days // 7

    # Remaining days
    remaining_days = total_days % 7

    # Add full weeks count to each day
    for day in day_counts:
        day_counts[day] = full_weeks

    # Distribute the remaining days
    current_day = start_day
    for _ in range(remaining_days):
        day_counts[current_day] += 1
        current_day = current_day % 7 + 1  # Move to the next day

    return day_counts
