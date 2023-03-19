import datetime

from holiday import Holiday


SASKATCHEWAN = [
    Holiday(
        "Family Day",
        month=2,
        year=2023,
        day=20,
        date=datetime.date(2023, 2, 20),
        nth_day=("mon", 3),
        province="Saskatchewan",
    ),  # 3rd Monday in February
    Holiday(
        "Good Friday",
        month=4,
        day=7,
        date=datetime.date(2023, 4, 7),
        preceding_date=("fri", "Easter Sunday"),
        province="Saskatchewan",
    ),  # Friday before Easter Sunday
    Holiday(
        "Victoria Day",
        month=5,
        year=2023,
        day=22,
        date=datetime.date(2023, 5, 22),
        preceding_date=("mon", 25),
        province="Saskatchewan",
    ),  # Monday before May 25th
    Holiday(
        "Thanksgiving Day",
        month=10,
        year=2023,
        day=9,
        date=datetime.date(2023, 10, 9),
        nth_day=("mon", 2),
        province="Saskatchewan",
    ),  # 2nd Monday in October
]
