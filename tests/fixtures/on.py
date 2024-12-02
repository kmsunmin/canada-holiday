from canada_holiday.holiday import CanadaHoliday


ONTARIO_2030 = [
    CanadaHoliday(
        "New Year's Day",
        month=1,
        year=2030,
        day=1,
        province="all",
    ),
    CanadaHoliday(
        "Family Day",
        month=2,
        year=2030,
        day=18,
        nth_day=("mon", 3),
        province="Ontario",
    ),  # 3rd Monday in February
    CanadaHoliday(
        "Good Friday",
        month=4,
        year=2030,
        day=19,
        preceding_date=("fri", "Easter Sunday"),
        province="Ontario",
    ),  # Friday before Easter Sunday
    CanadaHoliday(
        "Victoria Day",
        month=5,
        year=2030,
        day=20,
        preceding_date=("mon", 25),
        province="Ontario",
    ),  # Monday before May 25th
    CanadaHoliday(
        "Canada Day",
        month=7,
        year=2030,
        day=1,
        province="all",
    ),
    CanadaHoliday(
        "Civic Holiday",
        month=8,
        year=2030,
        day=5,
        nth_day=("mon", 1),
        province="Ontario",
    ),  # 1st Monday in August
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
        province="Ontario",
    ),  # 2nd Monday in October
    CanadaHoliday(
        "Christmas Day",
        month=12,
        year=2030,
        day=25,
        province="all",
    ),
    CanadaHoliday(
        "Boxing Day",
        month=12,
        year=2030,
        day=26,
        province="Ontario",
    ),
]

ONTARIO_2030_APRIL = [
    CanadaHoliday(
        "Good Friday",
        month=4,
        year=2030,
        day=19,
        preceding_date=("fri", "Easter Sunday"),
        province="Ontario",
    ),  # Friday before Easter Sunday
]
