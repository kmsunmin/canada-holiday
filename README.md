# canada-holiday

a Python package for Canadian holidays.

# Installation

### With pip
```bash
$ pip install canada-holiday
```

### With poetry
```bash
$ poetry add canada-holiday
```

# Usage
```python
import datetime
import canada_holidays

ontario_holidays_2023 = canada_holidays.get_holidays("Ontario", 2023)
# prints "Getting holiday information of Ontario province..."
print(ontario_holidays_2023)
# [CanadaHoliday(New Year's Day, 2023-01-01, Sunday, all), CanadaHoliday(Family Day, 2023-02-20, Monday, Ontario), ...]
print(ontario_holidays_2023[0].name)
# New Year's Day
print(ontario_holidays_2023[0].date)  # from datetime.date object
# 2023-01-01
print(ontario_holidays_2023[0].year)
# 2023
print(ontario_holidays_2023[0].province)
# all
print(ontario_holidays_2023[0].day_of_the_week)
# Sunday

manitoba_holidays_2023_june = canada_holidays.get_holidays("MB", 2023, 2)
# prints "Getting holiday information of Manitoba province..."
print(manitoba_holidays_2023_june)
# [CanadaHoliday(Louis Riel Day, 2023-02-20, Monday, Manitoba)]
louis_riel_day = manitoba_holidays_2023_june[0]
print(louis_riel_day.name)
# Louis Riel Day
print(louis_riel_day.month)
# 2
print(louis_riel_day.day)
# 20
print(louis_riel_day.date)
# 2023-02-20
print(louis_riel_day.province)
# Manitoba

date = datetime.date(2023, 8, 7)
result = canada_holidays.is_holiday(date, "British Columbia")
# prints "2023-08-07 is a holiday, B.C. Day in British Columbia province(s) in Canada"
print(result)
# True
date = datetime.date(2023, 4, 5)
result = canada_holidays.is_holiday(date, "Nova Scotia")
# prints "2023-04-05 is not a holiday in Nova Scotia province."
print(result)
# False
```
