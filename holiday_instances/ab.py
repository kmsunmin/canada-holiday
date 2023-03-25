from holiday import CanadaHoliday


ALBERTA = [
    CanadaHoliday(
        "Family Day", month=2, nth_day=("mon", 3), province="Alberta"
    ),  # 3rd Monday in February
    CanadaHoliday(
        "Good Friday",
        month=4,
        preceding_date=("fri", "Easter Sunday"),
        province="Alberta",
    ),  # Friday before Easter Sunday
    CanadaHoliday(
        "Victoria Day", month=5, preceding_date=("mon", 25), province="Alberta"
    ),  # Monday before May 25th
    CanadaHoliday("Heritage Day", month=8, nth_day=("mon", 1), province="Alberta"),
    CanadaHoliday(
        "Thanksgiving Day", month=10, nth_day=("mon", 2), province="Alberta"
    ),  # 2nd Monday in October
]
