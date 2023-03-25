from holiday import CanadaHoliday


NORTHWEST_TERRITORIES = [
    CanadaHoliday(
        "Good Friday",
        month=4,
        preceding_date=("fri", "Easter Sunday"),
        province="Northwest Territories",
    ),  # Friday before Easter Sunday
    CanadaHoliday(
        "National Aboriginal Day",
        month=6,
        day=21,
        province="Northwest Territories",
    ),
    CanadaHoliday(
        "Victoria Day",
        month=5,
        preceding_date=("mon", 25),
        province="Northwest Territories",
    ),  # Monday before May 25th
    CanadaHoliday(
        "Thanksgiving Day",
        month=10,
        nth_day=("mon", 2),
        province="Northwest Territories",
    ),  # 2nd Monday in October
]
