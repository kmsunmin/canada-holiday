from holiday import Holiday


NEW_BRUNSWICK = [
    Holiday(
        "Family Day", month=2, nth_day=(3, "mon"), province="New Brunswick"
    ),  # 3rd Monday in February
    Holiday(
        "Good Friday",
        month=4,
        preceding_date=("fri", "Easter Sunday"),
        province="New Brunswick",
    ),  # Friday before Easter Sunday
    Holiday(
        "Thanksgiving Day", month=10, nth_day=(2, "mon"), province="New Brunswick"
    ),  # 2nd Monday in October
]