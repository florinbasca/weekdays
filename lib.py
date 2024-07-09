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
  days: int = calendar_days(start_date, end_date)
  whole_weeks, remaining_days = divmod(days, 7)
  count: int = whole_weeks * 5

  # count the remaining days
  start_weekday = start_date.weekday()
  for i in range(remaining_days):
    if (start_weekday + i) % 7 < 5:
      count += 1

  return count


def calendar_days(start_date: date, end_date: date) -> int:
  """
  Calculates the total number of days between two dates (inclusive).

  Args:
    start_date (date): The starting date.
    end_date (date):   The ending date.

  Returns:
    int:               The number of days between start_date and end_date (inclusive).
  """

  # define days count by month - regular non-leap year
  days_in_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

  # step 1. intra year difference, assume both dates are in the same year, can have a positive or negative difference
  days: int = end_date.day - start_date.day
  if (start_date.month, start_date.day) <= (end_date.month, end_date.day):
    # start is before end - positive difference
    for month in range(start_date.month - 1, end_date.month - 1):
      days += days_in_month[month]

    # adjust for leap year of start date
    if is_leap_year(start_date.year) and start_date.month <= 2 < end_date.month:
      days += 1
    # adjust for leap year of end date
    if is_leap_year(end_date.year) and 2 < end_date.month and start_date.year != end_date.year:
      days += 1

  else:
    # start is after end - negative difference
    for month in range(end_date.month - 1, start_date.month - 1):
      days -= days_in_month[month]
    
    # adjust for leap year of start date
    if is_leap_year(start_date.year) and start_date.month <= 2:
      days += 1
    # adjust for leap year of end date
    if is_leap_year(end_date.year) and 2 < end_date.month:
      days += 1

  # step 2. difference in years to days
  days += (end_date.year - start_date.year) * 365

  # adjust for leap years, exclude start and end years already accounted for
  if end_date.year - start_date.year >= 2:
    days += (end_date.year -1) //   4 - (start_date.year +1) //   4
    days -= (end_date.year -1) // 100 - (start_date.year +1) // 100
    days += (end_date.year -1) // 400 - (start_date.year +1) // 400

  return days+1 # inclusive of start and end


def is_leap_year(year: int) -> bool:
  return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
