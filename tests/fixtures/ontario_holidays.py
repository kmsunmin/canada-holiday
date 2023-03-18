import datetime

from holiday import Holiday


CANADA_EASTER_DAY_2023 = datetime.date(2023, 4, 9)

ONTARIO_2023 = [
    Holiday(
        "New Year's Day",
        month=1,
        year=2023,
        day=1,
        date=datetime.date(2023, 1, 1),
        province="all",
    ),
    Holiday(
        "Family Day",
        month=2,
        year=2023,
        day=20,
        date=datetime.date(2023, 2, 20),
        nth_day=(3, "mon"),
        province="Ontario",
    ),  # 3rd Monday in February
    Holiday(
        "Good Friday",
        month=4,
        year=2023,
        day=7,
        date=datetime.date(2023, 4, 7),
        preceding_date=("fri", "Easter Sunday"),
        province="Ontario",
    ),  # Friday before Easter Sunday
    Holiday(
        "Easter Monday",
        month=4,
        year=2023,
        day=10,
        date=datetime.date(2023, 4, 10),
        succeeding_date=("mon", "Easter Sunday"),
        province="Ontario",
    ),  # Monday after Easter Sunday
    Holiday(
        "Victoria Day",
        month=5,
        year=2023,
        day=22,
        date=datetime.date(2023, 5, 22),
        preceding_date=("mon", 25),
        province="all",
    ),  # Monday before May 25th
    Holiday(
        "Canada Day",
        month=7,
        year=2023,
        day=1,
        date=datetime.date(2023, 7, 1),
        province="all",
    ),
    Holiday(
        "Civic Holiday",
        month=8,
        year=2023,
        day=7,
        date=datetime.date(2023, 8, 7),
        nth_day=(1, "mon"),
        province="Ontario",
    ),  # 1st Monday in August
    Holiday(
        "Labour Day",
        month=9,
        year=2023,
        day=4,
        date=datetime.date(2023, 9, 4),
        nth_day=(1, "mon"),
        province="all",
    ),  # 1st Monday in September
    Holiday(
        "National Day for Truth and Reconciliation",
        month=9,
        year=2023,
        day=30,
        date=datetime.date(2023, 9, 30),
        province="Ontario",
    ),
    Holiday(
        "Thanksgiving Day",
        month=10,
        year=2023,
        day=9,
        date=datetime.date(2023, 10, 9),
        nth_day=(2, "mon"),
        province="all",
    ),  # 2nd Monday in October
    Holiday(
        "Christmas Day",
        month=12,
        year=2023,
        day=25,
        date=datetime.date(2023, 12, 25),
        province="all",
    ),
    Holiday(
        "Boxing Day",
        month=12,
        year=2023,
        day=26,
        date=datetime.date(2023, 12, 26),
        province="all",
    ),
]

UNSORTED_ONTARIO_2023 = [
    Holiday(
        "Good Friday",
        month=4,
        year=2023,
        day=7,
        date=datetime.date(2023, 4, 7),
        preceding_date=("fri", "Easter Sunday"),
        province="Ontario",
    ),  # Friday before Easter Sunday
    Holiday(
        "Easter Monday",
        month=4,
        year=2023,
        day=10,
        date=datetime.date(2023, 4, 10),
        succeeding_date=("mon", "Easter Sunday"),
        province="Ontario",
    ),  # Monday after Easter Sunday
    Holiday(
        "Victoria Day",
        month=5,
        year=2023,
        day=22,
        date=datetime.date(2023, 5, 22),
        preceding_date=("mon", 25),
        province="all",
    ),  # Monday before May 25th
    Holiday(
        "Thanksgiving Day",
        month=10,
        year=2023,
        day=9,
        date=datetime.date(2023, 10, 9),
        nth_day=(2, "mon"),
        province="all",
    ),  # 2nd Monday in October
    Holiday(
        "Christmas Day",
        month=12,
        year=2023,
        day=25,
        date=datetime.date(2023, 12, 25),
        province="all",
    ),
    Holiday(
        "New Year's Day",
        month=1,
        year=2023,
        day=1,
        date=datetime.date(2023, 1, 1),
        province="all",
    ),
    Holiday(
        "Family Day",
        month=2,
        year=2023,
        day=20,
        date=datetime.date(2023, 2, 20),
        nth_day=(3, "mon"),
        province="Ontario",
    ),  # 3rd Monday in February
    Holiday(
        "Boxing Day",
        month=12,
        year=2023,
        day=26,
        date=datetime.date(2023, 12, 26),
        province="all",
    ),
    Holiday(
        "Canada Day",
        month=7,
        year=2023,
        day=1,
        date=datetime.date(2023, 7, 1),
        province="all",
    ),
    Holiday(
        "Civic Holiday",
        month=8,
        year=2023,
        day=7,
        date=datetime.date(2023, 8, 7),
        nth_day=(1, "mon"),
        province="Ontario",
    ),  # 1st Monday in August
    Holiday(
        "Labour Day",
        month=9,
        year=2023,
        day=4,
        date=datetime.date(2023, 9, 4),
        nth_day=(1, "mon"),
        province="all",
    ),  # 1st Monday in September
    Holiday(
        "National Day for Truth and Reconciliation",
        month=9,
        year=2023,
        day=30,
        date=datetime.date(2023, 9, 30),
        province="Ontario",
    ),
]

ONTARIO_2023_APRIL = [
    Holiday(
        "Good Friday",
        month=4,
        year=2023,
        day=7,
        date=datetime.date(2023, 4, 7),
        preceding_date=("fri", "Easter Sunday"),
        province="Ontario",
    ),  # Friday before Easter Sunday
    Holiday(
        "Easter Monday",
        month=4,
        year=2023,
        day=10,
        date=datetime.date(2023, 4, 10),
        succeeding_date=("mon", "Easter Sunday"),
        province="Ontario",
    ),  # Monday after Easter Sunday
]

ONTARIO_ONLY_HOLIDAYS_2023 = [
    Holiday(
        "Family Day",
        month=2,
        year=2023,
        day=20,
        date=datetime.date(2023, 2, 20),
        nth_day=(3, "mon"),
        province="Ontario",
    ),  # 3rd Monday in February
    Holiday(
        "Good Friday",
        month=4,
        year=2023,
        day=7,
        date=datetime.date(2023, 4, 7),
        preceding_date=("fri", "Easter Sunday"),
        province="Ontario",
    ),  # Friday before Easter Sunday
    Holiday(
        "Easter Monday",
        month=4,
        year=2023,
        day=10,
        date=datetime.date(2023, 4, 10),
        succeeding_date=("mon", "Easter Sunday"),
        province="Ontario",
    ),  # Monday after Easter Sunday
    Holiday(
        "Civic Holiday",
        month=8,
        year=2023,
        day=7,
        date=datetime.date(2023, 8, 7),
        nth_day=(1, "mon"),
        province="Ontario",
    ),  # 1st Monday in August
]
