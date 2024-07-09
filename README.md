# TRS assessment - Weekday Counter
Given two dates (inclusive), determine the number of weekdays between the two.

## Features
- Counts weekdays (Monday through Friday) between two dates
- Handles reversed date inputs automatically
- Raises appropriate errors for invalid inputs

## Installation
No additional installation is required. This module uses only Python standard libraries.

## Usage
> check `run.py`

```python
from datetime import date
from lib import count_weekdays

start_date = date(2023, 1, 1)
end_date   = date(2023, 12, 31)
weekdays   = count_weekdays(start_date, end_date)

print(f'start_date:  {start_date}')
print(f'end_date:    {end_date}')
print(f"Number of weekdays: {weekdays}")
```

## How to run
```
python run.py
```

## How to run unit tests
```
python test.py
```

## Potential improvements
- use non standard libraries such as `dateutil` or `pandas` for more robust date handling
- add option to include/exclude holidays
- use `functools.lru_cache` for memoization
- return `timedelta` instead of `int` if more flexibility is desired

## Contact
- Florin Basca florin.basca@yahoo.com
- Github repo: https://github.com/florinbasca/weekdays
