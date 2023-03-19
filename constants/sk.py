from holiday import Holiday


SASKATCHEWAN = [
    Holiday(
        "Family Day", month=2, nth_day=(3, "mon"), province="Saskatchewan"
    ),  # 3rd Monday in February
    Holiday(
        "Good Friday",
        month=4,
        preceding_date=("fri", "Easter Sunday"),
        province="Saskatchewan",
    ),  # Friday before Easter Sunday
    Holiday(
        "Victoria Day", month=5, preceding_date=("mon", 25), province="Saskatchewan"
    ),  # Monday before May 25th
    Holiday(
        "Thanksgiving Day", month=10, nth_day=(2, "mon"), province="Saskatchewan"
    ),  # 2nd Monday in October
]