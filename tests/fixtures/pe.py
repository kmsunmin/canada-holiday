import datetime

from holiday import Holiday


PRINCE_EDWARD_ISLAND = [
    Holiday(
        "Islander Day", month=2, year=2023, day=20, date=datetime.date(2023, 2, 20), nth_day=("mon", 3), province="Prince Edward Island"
    ),  # 3rd Monday in February
    Holiday(
        "Good Friday",
        month=4,
        year=2023,
        day=7,
        date=datetime.date(2023, 4, 7),
        preceding_date=("fri", "Easter Sunday"),
        province="Prince Edward Island",
    ),  # Friday before Easter Sunday
]
