from holiday import CanadaHoliday


PRINCE_EDWARD_ISLAND = [
    CanadaHoliday(
        "Islander Day", month=2, nth_day=("mon", 3), province="Prince Edward Island"
    ),  # 3rd Monday in February
    CanadaHoliday(
        "Good Friday",
        month=4,
        preceding_date=("fri", "Easter Sunday"),
        province="Prince Edward Island",
    ),  # Friday before Easter Sunday
]
