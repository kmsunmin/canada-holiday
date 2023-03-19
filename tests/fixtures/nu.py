import datetime

from holiday import Holiday


NUNAVUT = [
    Holiday(
        "Good Friday",
        month=4,
        year=2023,
        day=7,
        date=datetime.date(2023, 4, 7),
        preceding_date=("fri", "Easter Sunday"),
        province="Nunavut",
    ),  # Friday before Easter Sunday
    Holiday(
        "Victoria Day", month=5, year=2023, day=22, date=datetime.date(2023, 5, 22), preceding_date=("mon", 25), province="Nunavut"
    ),  # Monday before May 25th
    Holiday("Nunavut Day", month=7, year=2023, day=9, date=datetime.date(2023, 7, 9), province="Nunavut"),
    Holiday(
        "Thanksgiving Day", month=10, year=2023, day=9, date=datetime.date(2023, 10, 9), nth_day=("mon", 2), province="Nunavut"
    ),  # 2nd Monday in October
]
