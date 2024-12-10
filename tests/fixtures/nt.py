from canada_holiday.holiday import CanadaHoliday


NORTHWEST_TERRITORIES_2030 = [
    CanadaHoliday(
        "New Year's Day",
        month=1,
        year=2030,
        day=1,
        province="all",
    ),
    CanadaHoliday(
        "Good Friday",
        month=4,
        year=2030,
        day=19,
        preceding_date=("fri", "Easter Sunday"),
        province="Northwest Territories",
    ),  # Friday before Easter Sunday
    CanadaHoliday(
        "Victoria Day",
        month=5,
        year=2030,
        day=20,
        preceding_date=("mon", 25),
        province="Northwest Territories",
    ),  # Monday before May 25th
    CanadaHoliday(
        "National Aboriginal Day",
        month=6,
        year=2030,
        day=21,
        province="Northwest Territories",
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
        "Thanksgiving Day",
        month=10,
        year=2030,
        day=14,
        nth_day=("mon", 2),
        province="Northwest Territories",
    ),  # 2nd Monday in October
    CanadaHoliday(
        "Christmas Day",
        month=12,
        year=2030,
        day=25,
        province="all",
    ),
]
