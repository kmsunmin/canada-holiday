from holiday import CanadaHoliday


NEW_BRUNSWICK = [
    CanadaHoliday(
        "Family Day", month=2, nth_day=("mon", 3), province="New Brunswick"
    ),  # 3rd Monday in February
    CanadaHoliday(
        "Good Friday",
        month=4,
        preceding_date=("fri", "Easter Sunday"),
        province="New Brunswick",
    ),  # Friday before Easter Sunday
    CanadaHoliday(
        "Thanksgiving Day", month=10, nth_day=("mon", 2), province="New Brunswick"
    ),  # 2nd Monday in October
]
