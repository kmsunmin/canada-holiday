from holiday import CanadaHoliday


BRITISH_COLUMBIA = [
    CanadaHoliday(
        "Family Day", month=2, nth_day=("mon", 3), province="British Columbia"
    ),  # 3rd Monday in February
    CanadaHoliday(
        "Good Friday",
        month=4,
        preceding_date=("fri", "Easter Sunday"),
        province="British Columbia",
    ),  # Friday before Easter Sunday
    CanadaHoliday(
        "Victoria Day", month=5, preceding_date=("mon", 25), province="British Columbia"
    ),  # Monday before May 25th
    CanadaHoliday("B.C. Day", month=8, nth_day=("mon", 1), province="British Columbia"),
    CanadaHoliday(
        "Thanksgiving Day", month=10, nth_day=("mon", 2), province="British Columbia"
    ),  # 2nd Monday in October
]
