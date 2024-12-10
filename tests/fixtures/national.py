import datetime

from canada_holiday.holiday import CanadaHoliday


NATIONAL_2023 = [
    CanadaHoliday(
        "New Year's Day",
        month=1,
        year=2023,
        day=1,
        province="all",
    ),
    CanadaHoliday(
        "Canada Day",
        month=7,
        year=2023,
        day=1,
        province="all",
    ),
    CanadaHoliday(
        "Labour Day",
        month=9,
        year=2023,
        day=4,
        nth_day=("mon", 1),
        province="all",
    ),  # 1st Monday in September
    CanadaHoliday(
        "National Day for Truth and Reconciliation",
        month=9,
        year=2023,
        day=30,
        province="all",
    ),
    CanadaHoliday(
        "Christmas Day",
        month=12,
        year=2023,
        day=25,
        province="all",
    ),
]
