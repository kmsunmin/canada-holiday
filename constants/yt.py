from holiday import CanadaHoliday


YUKON = [
    CanadaHoliday(
        "Heritage Day", month=2, nth_day=("fri", 3), province="Yukon"
    ),  # 3rd Monday in February
    CanadaHoliday(
        "Good Friday",
        month=4,
        preceding_date=("fri", "Easter Sunday"),
        province="Yukon",
    ),  # Friday before Easter Sunday
    CanadaHoliday(
        "Victoria Day", month=5, preceding_date=("mon", 25), province="Yukon"
    ),  # Monday before May 25th
    CanadaHoliday("Discovery Day", month=8, nth_day=("mon", 3), province="Yukon"),
    CanadaHoliday(
        "Thanksgiving Day", month=10, nth_day=("mon", 2), province="Yukon"
    ),  # 2nd Monday in October
]
