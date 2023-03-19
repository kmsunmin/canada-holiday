from holiday import Holiday


MANITOBA = [
    Holiday(
        "Louis Riel Day", month=2, nth_day=(3, "mon"), province="Manitoba"
    ),  # 3rd Monday in February
    Holiday(
        "Good Friday",
        month=4,
        preceding_date=("fri", "Easter Sunday"),
        province="Manitoba",
    ),  # Friday before Easter Sunday
    Holiday(
        "Victoria Day", month=5, preceding_date=("mon", 25), province="Manitoba"
    ),  # Monday before May 25th
    Holiday(
        "Thanksgiving Day", month=10, nth_day=(2, "mon"), province="Manitoba"
    ),  # 2nd Monday in October
]