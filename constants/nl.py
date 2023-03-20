from holiday import Holiday


NEWFOUNDLAND_AND_LABRADOR = [
    Holiday("St. Patrick's Day", month=3, day=17, province="Newfoundland and Labrador"),
    Holiday(
        "Good Friday",
        month=4,
        preceding_date=("fri", "Easter Sunday"),
        province="Newfoundland and Labrador",
    ),  # Friday before Easter Sunday
    Holiday(
        "St. George's Day",
        month=4,
        nearest_day=("mon", 23),
        province="Newfoundland and Labrador",
    ),
    Holiday(
        "Discovery Day",
        month=6,
        nearest_day=("mon", 24),
        province="Newfoundland and Labrador",
    ),
]
