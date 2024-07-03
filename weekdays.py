from datetime import date


def count_weekdays(start_date: date, end_date: date) -> int:
  """ 
  Count the number of weekdays between two dates, inclusive of both start and end dates.

  Args:
    start_date (date): The starting date of the period to count.
    end_date (date):   The ending date of the period to count.

  Returns:
    int:               The number of weekdays (Monday through Friday) in the period.
  """  

  if not isinstance(start_date, date) or not isinstance(end_date, date):
    raise TypeError('Both start_date and end_date must be date objects')

  # revert start_date and end_date if start_date is after end_date
  if start_date > end_date:
    start_date, end_date = end_date, start_date
  
  # count the whole weeks
  days: int = (end_date - start_date).days + 1
  whole_weeks, remaining_days = divmod(days, 7)
  count: int = whole_weeks * 5

  # count the remaining days
  start_weekday = start_date.weekday()
  for i in range(remaining_days):
    if (start_weekday + i) % 7 < 5:
      count += 1

  return count
