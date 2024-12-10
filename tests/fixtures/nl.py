from canada_holiday.holiday import CanadaHoliday


NEWFOUNDLAND_AND_LABRADOR_2030 = [
    CanadaHoliday(
        "New Year's Day",
        month=1,
        year=2030,
        day=1,
        province="all",
    ),
    # TODO: Check St.Patrick's day is nearest Monday
    CanadaHoliday(
        "St. Patrick's Day",
        month=3,
        year=2030,
        day=17,
        province="Newfoundland and Labrador",
    ),
    CanadaHoliday(
        "Good Friday",
        month=4,
        year=2030,
        day=19,
        preceding_date=("fri", "Easter Sunday"),
        province="Newfoundland and Labrador",
    ),  # Friday before Easter Sunday
    CanadaHoliday(
        "St. George's Day",
        month=4,
        year=2030,
        day=22,
        nearest_day=("mon", 23),
        province="Newfoundland and Labrador",
    ),
    CanadaHoliday(
        "Discovery Day",
        month=6,
        year=2030,
        day=24,
        nearest_day=("mon", 24),
        province="Newfoundland and Labrador",
    ),
    CanadaHoliday(
        "Canada Day",
        month=7,
        year=2030,
        day=1,
        province="all",
    ),
    CanadaHoliday(
        "Labour Day",
        month=9,
        year=2030,
        day=2,
        nth_day=("mon", 1),
        province="all",
    ),  # 1st Monday in September
    CanadaHoliday(
        "National Day for Truth and Reconciliation",
        month=9,
        year=2030,
        day=30,
        province="all",
    ),
    CanadaHoliday(
        "Christmas Day",
        month=12,
        year=2030,
        day=25,
        province="all",
    ),
]
