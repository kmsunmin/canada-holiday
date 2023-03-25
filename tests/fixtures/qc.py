import datetime

from holiday import CanadaHoliday


QUEBEC_2023 = [
    CanadaHoliday(
        "New Year's Day",
        month=1,
        year=2023,
        day=1,
        date=datetime.date(2023, 1, 1),
        province="all",
    ),
    CanadaHoliday(
        "Easter Monday",
        month=4,
        year=2023,
        day=10,
        date=datetime.date(2023, 4, 10),
        succeeding_date=("mon", "Easter Sunday"),
        province="Quebec",
    ),  # Monday after Easter Sunday
    CanadaHoliday(
        "National Patriots Day",
        month=5,
        year=2023,
        day=22,
        date=datetime.date(2023, 5, 22),
        preceding_date=("mon", 25),
        province="Quebec",
    ),  # Monday before May 25th
    CanadaHoliday(
        "Féte Nationale (St. Jean Baptiste Day)",
        month=6,
        year=2023,
        day=24,
        date=datetime.date(2023, 6, 24),
        province="Quebec",
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
        "Thanksgiving Day",
        month=10,
        year=2023,
        day=9,
        date=datetime.date(2023, 10, 9),
        nth_day=("mon", 2),
        province="Quebec",
    ),  # 2nd Monday in October
    CanadaHoliday(
        "Christmas Day",
        month=12,
        year=2023,
        day=25,
        date=datetime.date(2023, 12, 25),
        province="all",
    ),
]
