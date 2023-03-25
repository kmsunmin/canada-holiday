from holiday import CanadaHoliday


SASKATCHEWAN = [
    CanadaHoliday(
        "Family Day", month=2, nth_day=("mon", 3), province="Saskatchewan"
    ),  # 3rd Monday in February
    CanadaHoliday(
        "Good Friday",
        month=4,
        preceding_date=("fri", "Easter Sunday"),
        province="Saskatchewan",
    ),  # Friday before Easter Sunday
    CanadaHoliday(
        "Victoria Day", month=5, preceding_date=("mon", 25), province="Saskatchewan"
    ),  # Monday before May 25th
    CanadaHoliday(
        "Thanksgiving Day", month=10, nth_day=("mon", 2), province="Saskatchewan"
    ),  # 2nd Monday in October
]
