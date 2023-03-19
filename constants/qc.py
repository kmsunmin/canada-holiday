from holiday import Holiday


QUEBEC = [
    Holiday(
        "Easter Monday",
        month=4,
        succeeding_date=("mon", "Easter Sunday"),
        province="Quebec",
    ),  # Monday after Easter Sunday
    Holiday(
        "National Patriots Day", month=5, preceding_date=("mon", 25), province="Quebec"
    ),  # Monday before May 25th
    Holiday(
        "Féte Nationale (St. Jean Baptiste Day)",
        month=6,
        day=24,
        province="Quebec"
    ),
    Holiday(
        "Thanksgiving Day", month=10, nth_day=("mon", 2), province="Quebec"
    ),  # 2nd Monday in October
]
