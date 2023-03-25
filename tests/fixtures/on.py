import datetime

from holiday import CanadaHoliday


CANADA_EASTER_DAY_2023 = datetime.date(2023, 4, 9)

ONTARIO_2023 = [
    CanadaHoliday(
        "New Year's Day",
        month=1,
        year=2023,
        day=1,
        date=datetime.date(2023, 1, 1),
        province="all",
    ),
    CanadaHoliday(
        "Family Day",
        month=2,
        year=2023,
        day=20,
        date=datetime.date(2023, 2, 20),
        nth_day=("mon", 3),
        province="Ontario",
    ),  # 3rd Monday in February
    CanadaHoliday(
        "Good Friday",
        month=4,
        year=2023,
        day=7,
        date=datetime.date(2023, 4, 7),
        preceding_date=("fri", "Easter Sunday"),
        province="Ontario",
    ),  # Friday before Easter Sunday
    CanadaHoliday(
        "Victoria Day",
        month=5,
        year=2023,
        day=22,
        date=datetime.date(2023, 5, 22),
        preceding_date=("mon", 25),
        province="Ontario",
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
        "Civic Holiday",
        month=8,
        year=2023,
        day=7,
        date=datetime.date(2023, 8, 7),
        nth_day=("mon", 1),
        province="Ontario",
    ),  # 1st Monday in August
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
        province="Ontario",
    ),  # 2nd Monday in October
    CanadaHoliday(
        "Christmas Day",
        month=12,
        year=2023,
        day=25,
        date=datetime.date(2023, 12, 25),
        province="all",
    ),
    CanadaHoliday(
        "Boxing Day",
        month=12,
        year=2023,
        day=26,
        date=datetime.date(2023, 12, 26),
        province="Ontario",
    ),
]

UNSORTED_ONTARIO_2023 = [
    CanadaHoliday(
        "Good Friday",
        month=4,
        year=2023,
        day=7,
        date=datetime.date(2023, 4, 7),
        preceding_date=("fri", "Easter Sunday"),
        province="Ontario",
    ),  # Friday before Easter Sunday
    CanadaHoliday(
        "Victoria Day",
        month=5,
        year=2023,
        day=22,
        date=datetime.date(2023, 5, 22),
        preceding_date=("mon", 25),
        province="Ontario",
    ),  # Monday before May 25th
    CanadaHoliday(
        "Thanksgiving Day",
        month=10,
        year=2023,
        day=9,
        date=datetime.date(2023, 10, 9),
        nth_day=("mon", 2),
        province="Ontario",
    ),  # 2nd Monday in October
    CanadaHoliday(
        "Christmas Day",
        month=12,
        year=2023,
        day=25,
        date=datetime.date(2023, 12, 25),
        province="all",
    ),
    CanadaHoliday(
        "New Year's Day",
        month=1,
        year=2023,
        day=1,
        date=datetime.date(2023, 1, 1),
        province="all",
    ),
    CanadaHoliday(
        "Family Day",
        month=2,
        year=2023,
        day=20,
        date=datetime.date(2023, 2, 20),
        nth_day=("mon", 3),
        province="Ontario",
    ),  # 3rd Monday in February
    CanadaHoliday(
        "Boxing Day",
        month=12,
        year=2023,
        day=26,
        date=datetime.date(2023, 12, 26),
        province="Ontario",
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
        "Civic Holiday",
        month=8,
        year=2023,
        day=7,
        date=datetime.date(2023, 8, 7),
        nth_day=("mon", 1),
        province="Ontario",
    ),  # 1st Monday in August
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
]

ONTARIO_2023_APRIL = [
    CanadaHoliday(
        "Good Friday",
        month=4,
        year=2023,
        day=7,
        date=datetime.date(2023, 4, 7),
        preceding_date=("fri", "Easter Sunday"),
        province="Ontario",
    ),  # Friday before Easter Sunday
]

ONTARIO_ONLY_HOLIDAYS_2023 = [
    CanadaHoliday(
        "Family Day",
        month=2,
        year=2023,
        day=20,
        date=datetime.date(2023, 2, 20),
        nth_day=("mon", 3),
        province="Ontario",
    ),  # 3rd Monday in February
    CanadaHoliday(
        "Good Friday",
        month=4,
        year=2023,
        day=7,
        date=datetime.date(2023, 4, 7),
        preceding_date=("fri", "Easter Sunday"),
        province="Ontario",
    ),  # Friday before Easter Sunday
    CanadaHoliday(
        "Victoria Day",
        month=5,
        year=2023,
        day=22,
        date=datetime.date(2023, 5, 22),
        preceding_date=("mon", 25),
        province="Ontario",
    ),  # Monday before May 25th
    CanadaHoliday(
        "Civic Holiday",
        month=8,
        year=2023,
        day=7,
        date=datetime.date(2023, 8, 7),
        nth_day=("mon", 1),
        province="Ontario",
    ),  # 1st Monday in August
    CanadaHoliday(
        "Thanksgiving Day",
        month=10,
        year=2023,
        day=9,
        date=datetime.date(2023, 10, 9),
        nth_day=("mon", 2),
        province="Ontario",
    ),  # 2nd Monday in October
    CanadaHoliday(
        "Boxing Day",
        month=12,
        year=2023,
        day=26,
        date=datetime.date(2023, 12, 26),
        province="Ontario",
    ),
]
