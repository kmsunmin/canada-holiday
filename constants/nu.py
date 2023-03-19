from holiday import Holiday


NUNAVUT = [
    Holiday(
        "Good Friday",
        month=4,
        preceding_date=("fri", "Easter Sunday"),
        province="Nunavut",
    ),  # Friday before Easter Sunday
    Holiday(
        "Victoria Day", month=5, preceding_date=("mon", 25), province="Nunavut"
    ),  # Monday before May 25th
    Holiday(
        "Nunavut Day",
        month=7,
        day=9,
        province="Nunavut"
    ),
    Holiday(
        "Thanksgiving Day", month=10, nth_day=("mon", 2), province="Nunavut"
    ),  # 2nd Monday in October
]
