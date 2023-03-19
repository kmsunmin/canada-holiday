from holiday import Holiday


ONTARIO = [
    Holiday(
        "Family Day", month=2, nth_day=(3, "mon"), province="Ontario"
    ),  # 3rd Monday in February
    Holiday(
        "Good Friday",
        month=4,
        preceding_date=("fri", "Easter Sunday"),
        province="Ontario",
    ),  # Friday before Easter Sunday
    Holiday(
        "Victoria Day", month=5, preceding_date=("mon", 25), province="Ontario"
    ),  # Monday before May 25th
    Holiday(
        "Civic Holiday", month=8, nth_day=(1, "mon"), province="Ontario"
    ),  # 1st Monday in August
    Holiday(
        "Thanksgiving Day", month=10, nth_day=(2, "mon"), province="Ontario"
    ),  # 2nd Monday in October
    Holiday("Boxing Day", month=12, day=26, province="Ontario"),
]
