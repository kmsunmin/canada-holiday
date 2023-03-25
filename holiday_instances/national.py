from holiday import CanadaHoliday


HOLIDAYS = [
    CanadaHoliday("New Year's Day", month=1, day=1, province="all"),
    CanadaHoliday("Canada Day", month=7, day=1, province="all"),
    CanadaHoliday(
        "Labour Day", month=9, nth_day=("mon", 1), province="all"
    ),  # 1st Monday in September
    CanadaHoliday(
        "National Day for Truth and Reconciliation", month=9, day=30, province="all"
    ),
    CanadaHoliday("Christmas Day", month=12, day=25, province="all"),
]
