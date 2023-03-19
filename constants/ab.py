from holiday import Holiday


ALBERTA = [
    Holiday(
        "Family Day", month=2, nth_day=(3, "mon"), province="Alberta"
    ),  # 3rd Monday in February
    Holiday(
        "Good Friday",
        month=4,
        preceding_date=("fri", "Easter Sunday"),
        province="Alberta",
    ),  # Friday before Easter Sunday
    Holiday(
        "Victoria Day", month=5, preceding_date=("mon", 25), province="Alberta"
    ),  # Monday before May 25th
    Holiday("Heritage Day", month=8, nth_day=(1, "mon"), province="Alberta"),
    Holiday(
        "Thanksgiving Day", month=10, nth_day=(2, "mon"), province="Alberta"
    ),  # 2nd Monday in October
]