from datetime import date


def count_weekdays(start: date, end: date) -> int:
  """ 
  Count the number of weekdays between two dates, inclusive of both start and end dates.

  Args:
    start (date): The starting date of the period to count.
    end   (date): The ending date of the period to count.

  Returns:
    int:          The number of weekdays (Monday through Friday) in the period.
  """  

  if not isinstance(start, date) or not isinstance(end, date):
    raise TypeError('Both start and end must be date objects')

  # revert start and end if start is after end
  if start > end:
    start, end = end, start
  
  # count the whole weeks
  days: int = calendar_days(start, end)
  whole_weeks, remaining_days = divmod(days, 7)
  count: int = whole_weeks * 5

  # count the remaining days
  start_weekday = start.weekday()
  for i in range(remaining_days):
    if (start_weekday + i) % 7 < 5:
      count += 1

  return count


def calendar_days(start: date, end: date) -> int:
  """
  Calculates the total number of days between two dates (inclusive).

  Args:
    start (date): The starting date.
    end   (date): The ending date.

  Returns:
    int:          The number of days between start and end (inclusive).
  """

  # define days count by month - regular non-leap year
  days_in_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

  # step 1. intra year difference, assume both dates are in the same year, can have a positive or negative difference
  days: int = end.day - start.day
  if (start.month, start.day) == (end.month, end.day):
    # start and end are the same day and month

    # adjust for leap year of start date
    if is_leap_year(start.year) and start.month <= 2 and start.year != end.year:
      days += 1
    # adjust for leap year of end date
    if is_leap_year(end.year) and 2 < end.month and start.year != end.year:
      days += 1

  elif (start.month, start.day) < (end.month, end.day):
    # start is before end - positive difference
    for month in range(start.month - 1, end.month - 1):
      days += days_in_month[month]

    # adjust for leap year of start date
    if is_leap_year(start.year) and start.month <= 2 and (start.year != end.year or end.month > 2):
      days += 1

    # adjust for leap year of end date
    if is_leap_year(end.year) and 2 < end.month and end.year != start.year:
      days += 1

  else:
    # start is after end - negative difference
    for month in range(end.month - 1, start.month - 1):
      days -= days_in_month[month]
    
    # adjust for leap year of start date
    if is_leap_year(start.year) and start.month <= 2:
      days += 1
    # adjust for leap year of end date
    if is_leap_year(end.year) and 2 < end.month:
      days += 1

  # step 2. difference in years to days
  days += (end.year - start.year) * 365

  # adjust for leap years, exclude start and end years already accounted for
  if end.year - start.year >= 2:
    days += (end.year -1) //   4 - (start.year) //   4
    days -= (end.year -1) // 100 - (start.year) // 100
    days += (end.year -1) // 400 - (start.year) // 400

  return days+1 # inclusive of start and end


def is_leap_year(year: int) -> bool:
  """ Checks if a given year is a leap year """
  return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
