from holiday import CanadaHoliday


NEWFOUNDLAND_AND_LABRADOR = [
    CanadaHoliday(
        "St. Patrick's Day", month=3, day=17, province="Newfoundland and Labrador"
    ),
    CanadaHoliday(
        "Good Friday",
        month=4,
        preceding_date=("fri", "Easter Sunday"),
        province="Newfoundland and Labrador",
    ),  # Friday before Easter Sunday
    CanadaHoliday(
        "St. George's Day",
        month=4,
        nearest_day=("mon", 23),
        province="Newfoundland and Labrador",
    ),
    CanadaHoliday(
        "Discovery Day",
        month=6,
        nearest_day=("mon", 24),
        province="Newfoundland and Labrador",
    ),
]
