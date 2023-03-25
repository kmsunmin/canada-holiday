from holiday import CanadaHoliday


QUEBEC = [
    CanadaHoliday(
        "Easter Monday",
        month=4,
        succeeding_date=("mon", "Easter Sunday"),
        province="Quebec",
    ),  # Monday after Easter Sunday
    CanadaHoliday(
        "National Patriots Day", month=5, preceding_date=("mon", 25), province="Quebec"
    ),  # Monday before May 25th
    CanadaHoliday(
        "Féte Nationale (St. Jean Baptiste Day)", month=6, day=24, province="Quebec"
    ),
    CanadaHoliday(
        "Thanksgiving Day", month=10, nth_day=("mon", 2), province="Quebec"
    ),  # 2nd Monday in October
]
