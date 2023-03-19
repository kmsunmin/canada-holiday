import datetime

from holiday import Holiday


QUEBEC = [
    Holiday(
        "Easter Monday",
        month=4,
        year=2023,
        day=10,
        date=datetime.date(2023, 4, 10),
        succeeding_date=("mon", "Easter Sunday"),
        province="Quebec",
    ),  # Monday after Easter Sunday
    Holiday(
        "National Patriots Day", month=5, year=2023, day=22, date=datetime.date(2023, 5, 22), preceding_date=("mon", 25), province="Quebec"
    ),  # Monday before May 25th
    Holiday(
        "Féte Nationale (St. Jean Baptiste Day)", month=6, year=2023,
        day=24,
        date=datetime.date(2023, 6, 24), province="Quebec"
    ),
    Holiday(
        "Thanksgiving Day", month=10, year=2023, day=9, date=datetime.date(2023, 10, 9), nth_day=("mon", 2), province="Quebec"
    ),  # 2nd Monday in October
]
