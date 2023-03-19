import datetime

from holiday import Holiday


ALBERTA = [
    Holiday(
        "Family Day", month=2, year=2023, day=20, date=datetime.date(2023, 2, 20), nth_day=("mon", 3), province="Alberta"
    ),  # 3rd Monday in February
    Holiday(
        "Good Friday",
        month=4,
        year=2023,
        day=7,
        date=datetime.date(2023, 4, 7),
        preceding_date=("fri", "Easter Sunday"),
        province="Alberta",
    ),  # Friday before Easter Sunday
    Holiday(
        "Victoria Day", month=5, year=2023, day=22, date=datetime.date(2023, 5, 22), preceding_date=("mon", 25), province="Alberta"
    ),  # Monday before May 25th
    Holiday("Heritage Day", month=8, year=2023, day=7, date=datetime.date(2023, 8, 7), nth_day=("mon", 1), province="Alberta"),
    Holiday(
        "Thanksgiving Day", month=10, year=2023, day=9, date=datetime.date(2023, 10, 9), nth_day=("mon", 2), province="Alberta"
    ),  # 2nd Monday in October
]
