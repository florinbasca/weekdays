from datetime import date
from lib import count_weekdays

start_date = date(2023, 1, 1)
end_date   = date(2023, 12, 31)
weekdays   = count_weekdays(start_date, end_date)

print(f'start_date:  {start_date}')
print(f'end_date:    {end_date}')
print(f"Number of weekdays: {weekdays}")
