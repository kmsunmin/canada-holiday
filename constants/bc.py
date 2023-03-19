from holiday import Holiday


BRITISH_COLUMBIA = [
    Holiday(
        "Family Day", month=2, nth_day=(3, "mon"), province="British Columbia"
    ),  # 3rd Monday in February
    Holiday(
        "Good Friday",
        month=4,
        preceding_date=("fri", "Easter Sunday"),
        province="British Columbia",
    ),  # Friday before Easter Sunday
    Holiday(
        "Victoria Day", month=5, preceding_date=("mon", 25), province="British Columbia"
    ),  # Monday before May 25th
    Holiday("B.C. Day", month=8, nth_day=(1, "mon"), province="British Columbia"),
    Holiday(
        "Thanksgiving Day", month=10, nth_day=(2, "mon"), province="British Columbia"
    ),  # 2nd Monday in October
]