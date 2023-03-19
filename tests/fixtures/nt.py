import datetime

from holiday import Holiday


NORTHWEST_TERRITORIES = [
    Holiday(
        "Good Friday",
        month=4,
        year=2023,
        day=7,
        date=datetime.date(2023, 4, 7),
        preceding_date=("fri", "Easter Sunday"),
        province="Northwest Territories",
    ),  # Friday before Easter Sunday
    Holiday(
        "National Aboriginal Day",
        month=6,
        year=2023,
        day=21,
        date=datetime.date(2023, 6, 21),
        province="Northwest Territories",
    ),
    Holiday(
        "Victoria Day",
        month=5,
        year=2023,
        day=22,
        date=datetime.date(2023, 5, 22),
        preceding_date=("mon", 25),
        province="Northwest Territories",
    ),  # Monday before May 25th
    Holiday(
        "Thanksgiving Day",
        month=10,
        year=2023,
        day=9,
        date=datetime.date(2023, 10, 9),
        nth_day=("mon", 2),
        province="Northwest Territories",
    ),  # 2nd Monday in October
]
