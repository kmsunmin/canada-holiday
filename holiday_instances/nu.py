from holiday import CanadaHoliday


NUNAVUT = [
    CanadaHoliday(
        "Good Friday",
        month=4,
        preceding_date=("fri", "Easter Sunday"),
        province="Nunavut",
    ),  # Friday before Easter Sunday
    CanadaHoliday(
        "Victoria Day", month=5, preceding_date=("mon", 25), province="Nunavut"
    ),  # Monday before May 25th
    CanadaHoliday("Nunavut Day", month=7, day=9, province="Nunavut"),
    CanadaHoliday(
        "Thanksgiving Day", month=10, nth_day=("mon", 2), province="Nunavut"
    ),  # 2nd Monday in October
]
