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
        day=23,
        province="Newfoundland and Labrador"
    )
]