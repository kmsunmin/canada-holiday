from holiday import Holiday


NORTHWEST_TERRITORIES = [
    Holiday(
        "Good Friday",
        month=4,
        preceding_date=("fri", "Easter Sunday"),
        province="Northwest Territories",
    ),  # Friday before Easter Sunday
    Holiday(
        "National Aboriginal Day",
        month=6,
        day=21,
        province="Northwest Territories",
    ),
    Holiday(
        "Victoria Day", month=5, preceding_date=("mon", 25), province="Northwest Territories"
    ),  # Monday before May 25th
    Holiday(
        "Thanksgiving Day", month=10, nth_day=(2, "mon"), province="Northwest Territories"
    ),  # 2nd Monday in October
]