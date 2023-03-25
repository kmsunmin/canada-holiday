import datetime
from holiday import CanadaHoliday


NATIONAL_2023 = [
    CanadaHoliday(
        "New Year's Day",
        month=1,
        year=2023,
        day=1,
        date=datetime.date(2023, 1, 1),
        province="all",
    ),
    CanadaHoliday(
        "Canada Day",
        month=7,
        year=2023,
        day=1,
        date=datetime.date(2023, 7, 1),
        province="all",
    ),
    CanadaHoliday(
        "Labour Day",
        month=9,
        year=2023,
        day=4,
        date=datetime.date(2023, 9, 4),
        nth_day=("mon", 1),
        province="all",
    ),  # 1st Monday in September
    CanadaHoliday(
        "National Day for Truth and Reconciliation",
        month=9,
        year=2023,
        day=30,
        date=datetime.date(2023, 9, 30),
        province="all",
    ),
    CanadaHoliday(
        "Christmas Day",
        month=12,
        year=2023,
        day=25,
        date=datetime.date(2023, 12, 25),
        province="all",
    ),
]
