import unittest
from datetime import date
from lib import count_weekdays, calendar_days, is_leap_year


def ref(start_date, end_date):
  ''' Reference implementation for calendar days '''
  return (end_date - start_date).days +1


class TestWeekdays(unittest.TestCase):

  def test_same_date(self):
    self.assertEqual(count_weekdays(date(2024, 7, 1), date(2024, 7, 1)), 1)

  def test_one_week(self):
    self.assertEqual(count_weekdays(date(2024, 7, 1), date(2024, 7, 7)), 5)

  def test_partial_week(self):
    self.assertEqual(count_weekdays(date(2024, 7, 1), date(2024, 7, 4)), 4)

  def test_multiple_weeks(self):
    self.assertEqual(count_weekdays(date(2024, 7, 1), date(2024, 7, 31)), 23)

  def test_reversed_dates(self):
    self.assertEqual(count_weekdays(date(2024, 7, 31), date(2024, 7, 1)), 23)

  def test_weekend_to_weekend(self):
    self.assertEqual(count_weekdays(date(2024, 7, 6), date(2024, 7, 14)), 5)

  def test_leap_year(self):
    self.assertEqual(count_weekdays(date(2024, 2, 28), date(2024, 3, 1)), 3)

  def test_year_boundary(self):
    self.assertEqual(count_weekdays(date(2023, 12, 31), date(2024, 1, 1)), 1)
    self.assertEqual(count_weekdays(date(2024, 12, 30), date(2025, 1, 3)), 5)

  def test_one_year(self):
    self.assertEqual(count_weekdays(date(2024, 1, 1), date(2024, 12, 31)), 262)

  def test_large_date_range(self):
    self.assertEqual(count_weekdays(date(2000, 1, 1), date(2030, 12, 31)), 8087)

  def test_invalid_input(self):
    with self.assertRaises(TypeError):
      count_weekdays('abc', 123)
      count_weekdays('2024-07-01', '2024-07-01')


class TestCalendarDays(unittest.TestCase):

  def test_same_date(self):
    start_date = date(2023, 7, 1)
    end_date   = date(2023, 7, 1)
    self.assertEqual(calendar_days(start_date, end_date), ref(start_date, end_date))

  def test_same_month(self):
    start_date = date(2023, 7, 1)
    end_date   = date(2023, 7, 15)
    self.assertEqual(calendar_days(start_date, end_date), ref(start_date, end_date))

  def test_across_months_same_year(self):
    start_date = date(2023, 6, 15)
    end_date   = date(2023, 7, 1)
    self.assertEqual(calendar_days(start_date, end_date), ref(start_date, end_date))

  def test_across_years(self):
    start_date = date(2022, 12, 20)
    end_date   = date(2023, 1, 10)
    self.assertEqual(calendar_days(start_date, end_date), ref(start_date, end_date))

  def test_across_leap_year(self):
    start_date = date(2023, 2, 20)
    end_date   = date(2024, 3, 10)
    self.assertEqual(calendar_days(start_date, end_date), ref(start_date, end_date))

  def test_start_after_end(self):
    start_date = date(2023, 7, 15)
    end_date   = date(2023, 7, 1)
    self.assertEqual(calendar_days(start_date, end_date), ref(start_date, end_date))

  def test_start_before_end_leap_year(self):
    start_date = date(2024, 2, 28)
    end_date   = date(2024, 3, 1)
    self.assertEqual(calendar_days(start_date, end_date), ref(start_date, end_date))

  def test_start_before_end_non_leap_year(self):
    start_date = date(2023, 2, 28)
    end_date   = date(2023, 3, 1)
    self.assertEqual(calendar_days(start_date, end_date), ref(start_date, end_date))

  def test_end_of_february_leap_year(self):
    start_date = date(2020, 2, 28)
    end_date   = date(2020, 2, 29)
    self.assertEqual(calendar_days(start_date, end_date), ref(start_date, end_date))

  def test_end_of_february_non_leap_year(self):
    start_date = date(2021, 2, 28)
    end_date   = date(2021, 3, 1)
    self.assertEqual(calendar_days(start_date, end_date), ref(start_date, end_date))

  def test_spanning_century(self):
    start_date = date(1999, 12, 31)
    end_date   = date(2000, 1, 1)
    self.assertEqual(calendar_days(start_date, end_date), ref(start_date, end_date))

  def test_min_max_dates(self):
    start_date = date(1, 1, 1)
    end_date   = date(9999, 12, 31)
    self.assertEqual(calendar_days(start_date, end_date), ref(start_date, end_date))

  def test_start_date_before_min_date(self):
    with self.assertRaises(ValueError):
      calendar_days(date(0, 1, 1), date(2023, 7, 1))

  def test_end_date_after_max_date(self):
    with self.assertRaises(ValueError):
      calendar_days(date(2023, 7, 1), date(10000, 1, 1))


class TestLeapYear(unittest.TestCase):
 
  def test_leap_year(self):
    self.assertTrue(is_leap_year(2020))
    self.assertFalse(is_leap_year(2021))
    self.assertTrue(is_leap_year(2000))
    self.assertFalse(is_leap_year(1900))


if __name__ == '__main__':
  unittest.main()
