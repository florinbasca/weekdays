import unittest
from datetime import date
from weekdays import count_weekdays

class TestWeekdays(unittest.TestCase):
  def test_same_day(self):
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
    self.assertEqual(count_weekdays(date(2024, 12, 30), date(2025, 1, 3)), 5)

  def test_invalid_input(self):
    with self.assertRaises(TypeError):
      count_weekdays("abc", 123)

if __name__ == '__main__':
  unittest.main()