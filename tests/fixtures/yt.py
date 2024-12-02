from canada_holiday.holiday import CanadaHoliday


YUKON_2030 = [
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
        day=22,
        preceding_date=("fri", "Last Sunday"),
        province="Yukon",
    ),  # 3rd Monday in February
    CanadaHoliday(
        "Good Friday",
        month=4,
        year=2030,
        day=19,
        preceding_date=("fri", "Easter Sunday"),
        province="Yukon",
    ),  # Friday before Easter Sunday
    CanadaHoliday(
        "Victoria Day",
        month=5,
        year=2030,
        day=20,
        preceding_date=("mon", 25),
        province="Yukon",
    ),  # Monday before May 25th
    CanadaHoliday(
        "Canada Day",
        month=7,
        year=2030,
        day=1,
        province="all",
    ),
    CanadaHoliday(
        "Discovery Day",
        month=8,
        year=2030,
        day=19,
        nth_day=("mon", 3),
        province="Yukon",
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
        "Thanksgiving Day",
        month=10,
        year=2030,
        day=14,
        nth_day=("mon", 2),
        province="Yukon",
    ),  # 2nd Monday in October
    CanadaHoliday(
        "Christmas Day",
        month=12,
        year=2030,
        day=25,
        province="all",
    ),
]
