from canada_holiday.holiday import CanadaHoliday


NOVA_SCOTIA_2030 = [
    CanadaHoliday(
        "New Year's Day",
        month=1,
        year=2030,
        day=1,
        province="all",
    ),
    CanadaHoliday(
        "Heritage Day",
        month=2,
        year=2030,
        day=18,
        nth_day=("mon", 3),
        province="Nova Scotia",
    ),  # 3rd Monday in February
    CanadaHoliday(
        "Good Friday",
        month=4,
        year=2030,
        day=19,
        preceding_date=("fri", "Easter Sunday"),
        province="Nova Scotia",
    ),  # Friday before Easter Sunday
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
