from holiday import Holiday


NATIONAL = [
    Holiday("New Year's Day", month=1, day=1, province="all"),
    Holiday("Canada Day", month=7, day=1, province="all"),
    Holiday(
        "Labour Day", month=9, nth_day=("mon", 1), province="all"
    ),  # 1st Monday in September
    Holiday(
        "National Day for Truth and Reconciliation", month=9, day=30, province="all"
    ),
    Holiday("Christmas Day", month=12, day=25, province="all"),
]
