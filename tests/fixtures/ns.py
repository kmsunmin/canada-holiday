import datetime

from holiday import Holiday


NOVA_SCOTIA = [
    Holiday(
        "Heritage Day", month=2, year=2023, day=20, date=datetime.date(2023, 2, 20), nth_day=("mon", 3), province="Nova Scotia"
    ),  # 3rd Monday in February
    Holiday(
        "Good Friday",
        month=4,
        year=2023,
        day=7,
        date=datetime.date(2023, 4, 7),
        preceding_date=("fri", "Easter Sunday"),
        province="Nova Scotia",
    ),  # Friday before Easter Sunday
]
