from holiday import Holiday


YUKON = [
    Holiday(
        "Heritage Day", month=2, nth_day=("fri", 3), province="Yukon"
    ),  # 3rd Monday in February
    Holiday(
        "Good Friday",
        month=4,
        preceding_date=("fri", "Easter Sunday"),
        province="Yukon",
    ),  # Friday before Easter Sunday
    Holiday(
        "Victoria Day", month=5, preceding_date=("mon", 25), province="Yukon"
    ),  # Monday before May 25th
    Holiday("Discovery Day", month=8, nth_day=("mon", 3), province="Yukon"),
    Holiday(
        "Thanksgiving Day", month=10, nth_day=("mon", 2), province="Yukon"
    ),  # 2nd Monday in October
]
