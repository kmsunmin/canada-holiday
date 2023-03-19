import datetime

from holiday import Holiday


YUKON = [
    Holiday(
        "Heritage Day",
        month=2,
        year=2023,
        day=24,
        date=datetime.date(2023, 2, 24),
        nth_day=("fri", 3),
        province="Yukon",
    ),  # 3rd Monday in February
    Holiday(
        "Good Friday",
        month=4,
        year=2023,
        day=7,
        date=datetime.date(2023, 4, 7),
        preceding_date=("fri", "Easter Sunday"),
        province="Yukon",
    ),  # Friday before Easter Sunday
    Holiday(
        "Victoria Day",
        month=5,
        year=2023,
        day=22,
        date=datetime.date(2023, 5, 22),
        preceding_date=("mon", 25),
        province="Yukon",
    ),  # Monday before May 25th
    Holiday(
        "Discovery Day",
        month=8,
        year=2023,
        day=21,
        date=datetime.date(2023, 8, 21),
        nth_day=("mon", 3),
        province="Yukon",
    ),
    Holiday(
        "Thanksgiving Day",
        month=10,
        year=2023,
        day=9,
        date=datetime.date(2023, 10, 9),
        nth_day=("mon", 2),
        province="Yukon",
    ),  # 2nd Monday in October
]
