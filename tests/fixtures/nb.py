import datetime

from holiday import Holiday


NEW_BRUNSWICK = [
    Holiday(
        "Family Day", month=2, year=2023, day=20, date=datetime.date(2023, 2, 20), nth_day=("mon", 3), province="New Brunswick"
    ),  # 3rd Monday in February
    Holiday(
        "Good Friday",
        month=4,
        year=2023,
        day=7,
        date=datetime.date(2023, 4, 7),
        preceding_date=("fri", "Easter Sunday"),
        province="New Brunswick",
    ),  # Friday before Easter Sunday
    Holiday(
        "Thanksgiving Day", month=10, year=2023, day=9, date=datetime.date(2023, 10, 9), nth_day=("mon", 2), province="New Brunswick"
    ),  # 2nd Monday in October
]
