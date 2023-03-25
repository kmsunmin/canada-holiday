from holiday import CanadaHoliday


MANITOBA = [
    CanadaHoliday(
        "Louis Riel Day", month=2, nth_day=("mon", 3), province="Manitoba"
    ),  # 3rd Monday in February
    CanadaHoliday(
        "Good Friday",
        month=4,
        preceding_date=("fri", "Easter Sunday"),
        province="Manitoba",
    ),  # Friday before Easter Sunday
    CanadaHoliday(
        "Victoria Day", month=5, preceding_date=("mon", 25), province="Manitoba"
    ),  # Monday before May 25th
    CanadaHoliday(
        "Thanksgiving Day", month=10, nth_day=("mon", 2), province="Manitoba"
    ),  # 2nd Monday in October
]
