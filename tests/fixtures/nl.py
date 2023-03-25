import datetime

from canada_holiday.holiday_class import CanadaHoliday


NEWFOUNDLAND_AND_LABRADOR_2023 = [
    CanadaHoliday(
        "New Year's Day",
        month=1,
        year=2023,
        day=1,
        date=datetime.date(2023, 1, 1),
        province="all",
    ),
    # TODO: Check St.Patrick's day is nearest Monday
    CanadaHoliday(
        "St. Patrick's Day",
        month=3,
        year=2023,
        day=17,
        date=datetime.date(2023, 3, 17),
        province="Newfoundland and Labrador",
    ),
    CanadaHoliday(
        "Good Friday",
        month=4,
        year=2023,
        day=7,
        date=datetime.date(2023, 4, 7),
        preceding_date=("fri", "Easter Sunday"),
        province="Newfoundland and Labrador",
    ),  # Friday before Easter Sunday
    CanadaHoliday(
        "St. George's Day",
        month=4,
        year=2023,
        day=24,
        date=datetime.date(2023, 4, 24),
        nearest_day=("mon", 23),
        province="Newfoundland and Labrador",
    ),
    CanadaHoliday(
        "Discovery Day",
        month=6,
        year=2023,
        day=26,
        date=datetime.date(2023, 6, 26),
        nearest_day=("mon", 24),
        province="Newfoundland and Labrador",
    ),
    CanadaHoliday(
        "Canada Day",
        month=7,
        year=2023,
        day=1,
        date=datetime.date(2023, 7, 1),
        province="all",
    ),
    CanadaHoliday(
        "Labour Day",
        month=9,
        year=2023,
        day=4,
        date=datetime.date(2023, 9, 4),
        nth_day=("mon", 1),
        province="all",
    ),  # 1st Monday in September
    CanadaHoliday(
        "National Day for Truth and Reconciliation",
        month=9,
        year=2023,
        day=30,
        date=datetime.date(2023, 9, 30),
        province="all",
    ),
    CanadaHoliday(
        "Christmas Day",
        month=12,
        year=2023,
        day=25,
        date=datetime.date(2023, 12, 25),
        province="all",
    ),
]

NEWFOUNDLAND_AND_LABRADOR_2030 = [
    CanadaHoliday(
        "New Year's Day",
        month=1,
        year=2030,
        day=1,
        date=datetime.date(2030, 1, 1),
        province="all",
    ),
    # TODO: Check St.Patrick's day is nearest Monday
    CanadaHoliday(
        "St. Patrick's Day",
        month=3,
        year=2030,
        day=17,
        date=datetime.date(2030, 3, 17),
        province="Newfoundland and Labrador",
    ),
    CanadaHoliday(
        "Good Friday",
        month=4,
        year=2030,
        day=19,
        date=datetime.date(2030, 4, 19),
        preceding_date=("fri", "Easter Sunday"),
        province="Newfoundland and Labrador",
    ),  # Friday before Easter Sunday
    CanadaHoliday(
        "St. George's Day",
        month=4,
        year=2030,
        day=22,
        date=datetime.date(2030, 4, 22),
        nearest_day=("mon", 23),
        province="Newfoundland and Labrador",
    ),
    CanadaHoliday(
        "Discovery Day",
        month=6,
        year=2030,
        day=24,
        date=datetime.date(2030, 6, 24),
        nearest_day=("mon", 24),
        province="Newfoundland and Labrador",
    ),
    CanadaHoliday(
        "Canada Day",
        month=7,
        year=2030,
        day=1,
        date=datetime.date(2030, 7, 1),
        province="all",
    ),
    CanadaHoliday(
        "Labour Day",
        month=9,
        year=2030,
        day=2,
        date=datetime.date(2030, 9, 2),
        nth_day=("mon", 1),
        province="all",
    ),  # 1st Monday in September
    CanadaHoliday(
        "National Day for Truth and Reconciliation",
        month=9,
        year=2030,
        day=30,
        date=datetime.date(2030, 9, 30),
        province="all",
    ),
    CanadaHoliday(
        "Christmas Day",
        month=12,
        year=2030,
        day=25,
        date=datetime.date(2030, 12, 25),
        province="all",
    ),
]
