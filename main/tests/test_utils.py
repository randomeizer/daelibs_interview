"""Tests for the main app."""

import unittest
from main.utils import aware_datetime
from main.utils import calculate_day_counts


class CalculateDayCountsTests(unittest.TestCase):
    """Tests for the calculate_day_counts function in the utils module."""

    def test_single_day_range(self):
        """Test a range of only one day."""

        start_date = aware_datetime(2023, 5, 15)  # Monday
        end_date = aware_datetime(2023, 5, 15)    # Monday
        expected = {1: 0, 2: 1, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
        self.assertEqual(calculate_day_counts(start_date, end_date), expected)

    def test_full_week_range(self):
        """Test a range of exactly one week."""

        start_date = aware_datetime(2023, 5, 15)  # Monday
        end_date = aware_datetime(2023, 5, 21)    # Sunday
        expected = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1}
        self.assertEqual(calculate_day_counts(start_date, end_date), expected)

    def test_more_than_full_week_range(self):
        """Test a range of more than one week."""

        start_date = aware_datetime(2023, 5, 15)  # Monday
        end_date = aware_datetime(2023, 5, 22)    # Next Monday
        expected = {1: 1, 2: 2, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1}
        self.assertEqual(calculate_day_counts(start_date, end_date), expected)

    def test_partial_week_range(self):
        """Test a range that spans part of a week."""

        start_date = aware_datetime(2023, 5, 17)  # Wednesday
        end_date = aware_datetime(2023, 5, 19)    # Friday
        expected = {1: 0, 2: 0, 3: 0, 4: 1, 5: 1, 6: 1, 7: 0}
        self.assertEqual(calculate_day_counts(start_date, end_date), expected)

    def test_spanning_multiple_weeks(self):
        """Test a range that spans multiple weeks."""

        start_date = aware_datetime(2023, 5, 15)  # Monday
        end_date = aware_datetime(2023, 5, 28)    # Next Sunday
        expected = {1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2}
        self.assertEqual(calculate_day_counts(start_date, end_date), expected)

    def test_range_with_month_change(self):
        """Test a range that spans a month change."""

        start_date = aware_datetime(2023, 4, 28)  # Friday
        end_date = aware_datetime(2023, 5, 4)     # Next Thursday
        expected = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1}
        self.assertEqual(calculate_day_counts(start_date, end_date), expected)

    def test_range_with_year_change(self):
        """Test a range that spans a year change."""

        start_date = aware_datetime(2023, 12, 29)  # Friday
        end_date = aware_datetime(2024, 1, 4)      # Next Thursday
        expected = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1}
        self.assertEqual(calculate_day_counts(start_date, end_date), expected)

    def test_range_with_leap_year(self):
        """Test a range that spans a leap year."""

        start_date = aware_datetime(2024, 2, 27)
        end_date = aware_datetime(2024, 3, 2)
        expected = {1: 0, 2: 0, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1}
        self.assertEqual(calculate_day_counts(start_date, end_date), expected)

    def test_spanning_multiple_years(self):
        """Test a range that spans multiple years."""

        start_date = aware_datetime(2022, 12, 29)
        end_date = aware_datetime(2024, 1, 3)
        expected = {1: 53, 2: 53, 3: 53, 4: 53, 5: 53, 6: 53, 7: 53}
        self.assertEqual(calculate_day_counts(start_date, end_date), expected)

    def test_invalid_date_format(self):
        """Test invalid date format."""

        start_date = '2023-05-15'
        end_date = '2023-05-15'
        with self.assertRaises(TypeError):
            calculate_day_counts(start_date, end_date)
    
    def test_invalid_date_range(self):
        """Test invalid date range."""

        start_date = aware_datetime(2023, 5, 15)
        end_date = aware_datetime(2023, 5, 14)
        with self.assertRaises(ValueError):
            calculate_day_counts(start_date, end_date)


if __name__ == '__main__':
    unittest.main()
