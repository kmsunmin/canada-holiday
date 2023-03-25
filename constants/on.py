from holiday import CanadaHoliday


ONTARIO = [
    CanadaHoliday(
        "Family Day", month=2, nth_day=("mon", 3), province="Ontario"
    ),  # 3rd Monday in February
    CanadaHoliday(
        "Good Friday",
        month=4,
        preceding_date=("fri", "Easter Sunday"),
        province="Ontario",
    ),  # Friday before Easter Sunday
    CanadaHoliday(
        "Victoria Day", month=5, preceding_date=("mon", 25), province="Ontario"
    ),  # Monday before May 25th
    CanadaHoliday(
        "Civic Holiday", month=8, nth_day=("mon", 1), province="Ontario"
    ),  # 1st Monday in August
    CanadaHoliday(
        "Thanksgiving Day", month=10, nth_day=("mon", 2), province="Ontario"
    ),  # 2nd Monday in October
    CanadaHoliday("Boxing Day", month=12, day=26, province="Ontario"),
]
