import datetime

from canada_holiday.holiday_class import CanadaHoliday


YUKON_2023 = [
    CanadaHoliday(
        "New Year's Day",
        month=1,
        year=2023,
        day=1,
        date=datetime.date(2023, 1, 1),
        province="all",
    ),
    CanadaHoliday(
        "Heritage Day",
        month=2,
        year=2023,
        day=24,
        date=datetime.date(2023, 2, 24),
        preceding_date=("fri", "Last Sunday"),
        province="Yukon",
    ),  # 3rd Monday in February
    CanadaHoliday(
        "Good Friday",
        month=4,
        year=2023,
        day=7,
        date=datetime.date(2023, 4, 7),
        preceding_date=("fri", "Easter Sunday"),
        province="Yukon",
    ),  # Friday before Easter Sunday
    CanadaHoliday(
        "Victoria Day",
        month=5,
        year=2023,
        day=22,
        date=datetime.date(2023, 5, 22),
        preceding_date=("mon", 25),
        province="Yukon",
    ),  # Monday before May 25th
    CanadaHoliday(
        "Canada Day",
        month=7,
        year=2023,
        day=1,
        date=datetime.date(2023, 7, 1),
        province="all",
    ),
    CanadaHoliday(
        "Discovery Day",
        month=8,
        year=2023,
        day=21,
        date=datetime.date(2023, 8, 21),
        nth_day=("mon", 3),
        province="Yukon",
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
        province="Yukon",
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

YUKON_2030 = [
    CanadaHoliday(
        "New Year's Day",
        month=1,
        year=2030,
        day=1,
        date=datetime.date(2030, 1, 1),
        province="all",
    ),
    CanadaHoliday(
        "Heritage Day",
        month=2,
        year=2030,
        day=22,
        date=datetime.date(2030, 2, 22),
        preceding_date=("fri", "Last Sunday"),
        province="Yukon",
    ),  # 3rd Monday in February
    CanadaHoliday(
        "Good Friday",
        month=4,
        year=2030,
        day=19,
        date=datetime.date(2030, 4, 19),
        preceding_date=("fri", "Easter Sunday"),
        province="Yukon",
    ),  # Friday before Easter Sunday
    CanadaHoliday(
        "Victoria Day",
        month=5,
        year=2030,
        day=20,
        date=datetime.date(2030, 5, 20),
        preceding_date=("mon", 25),
        province="Yukon",
    ),  # Monday before May 25th
    CanadaHoliday(
        "Canada Day",
        month=7,
        year=2030,
        day=1,
        date=datetime.date(2030, 7, 1),
        province="all",
    ),
    CanadaHoliday(
        "Discovery Day",
        month=8,
        year=2030,
        day=19,
        date=datetime.date(2030, 8, 19),
        nth_day=("mon", 3),
        province="Yukon",
    ),
    CanadaHoliday(
        "Labour Day",
        month=9,
        year=2030,
        day=2,
        date=datetime.date(2030, 9, 2),
        nth_day=("mon", 1),
        province="all",
    ),  # 1st Monday in September
    CanadaHoliday(
        "National Day for Truth and Reconciliation",
        month=9,
        year=2030,
        day=30,
        date=datetime.date(2030, 9, 30),
        province="all",
    ),
    CanadaHoliday(
        "Thanksgiving Day",
        month=10,
        year=2030,
        day=14,
        date=datetime.date(2030, 10, 14),
        nth_day=("mon", 2),
        province="Yukon",
    ),  # 2nd Monday in October
    CanadaHoliday(
        "Christmas Day",
        month=12,
        year=2030,
        day=25,
        date=datetime.date(2030, 12, 25),
        province="all",
    ),
]
