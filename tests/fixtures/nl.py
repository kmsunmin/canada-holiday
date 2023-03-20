import datetime

from holiday import Holiday


NEWFOUNDLAND_AND_LABRADOR_2023 = [
    Holiday(
        "New Year's Day",
        month=1,
        year=2023,
        day=1,
        date=datetime.date(2023, 1, 1),
        province="all",
    ),
    # TODO: Check St.Patrick's day is nearest Monday
    Holiday(
        "St. Patrick's Day",
        month=3,
        year=2023,
        day=17,
        date=datetime.date(2023, 3, 17),
        province="Newfoundland and Labrador",
    ),
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
    Holiday(
        "Canada Day",
        month=7,
        year=2023,
        day=1,
        date=datetime.date(2023, 7, 1),
        province="all",
    ),
    Holiday(
        "Labour Day",
        month=9,
        year=2023,
        day=4,
        date=datetime.date(2023, 9, 4),
        nth_day=("mon", 1),
        province="all",
    ),  # 1st Monday in September
    Holiday(
        "National Day for Truth and Reconciliation",
        month=9,
        year=2023,
        day=30,
        date=datetime.date(2023, 9, 30),
        province="all",
    ),
    Holiday(
        "Christmas Day",
        month=12,
        year=2023,
        day=25,
        date=datetime.date(2023, 12, 25),
        province="all",
    ),
]
