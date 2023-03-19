import datetime

from holiday import Holiday


NEWFOUNDLAND_AND_LABRADOR = [
    # TODO: Check St.Patrick's day is nearest Monday
    Holiday("St. Patrick's Day", month=3, year=2023, day=17, date=datetime.date(2023, 3, 17), province="Newfoundland and Labrador"),
    Holiday(
        "Good Friday",
        month=4,
        year=2023,
        day=7,
        date=datetime.date(2023, 4, 7),
        preceding_date=("fri", "Easter Sunday"),
        province="Newfoundland and Labrador",
    ),  # Friday before Easter Sunday
    Holiday(
        "St. George's Day",
        month=4,
        year=2023,
        day=24,
        date=datetime.date(2023, 4, 24),
        nearest_day=("mon", 23),
        province="Newfoundland and Labrador",
    ),
    Holiday(
        "Discovery Day",
        month=6,
        year=2023,
        day=26,
        # TODO: Look into Discovery/June Day for 2023
        date=datetime.date(2023, 6, 26),
        nearest_day=("mon", 24),
        province="Newfoundland and Labrador",
    ),
]
