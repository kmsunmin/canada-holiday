from holiday import Holiday


NOVA_SCOTIA = [
    Holiday(
        "Heritage Day", month=2, nth_day=("mon", 3), province="Nova Scotia"
    ),  # 3rd Monday in February
    Holiday(
        "Good Friday",
        month=4,
        preceding_date=("fri", "Easter Sunday"),
        province="Nova Scotia",
    ),  # Friday before Easter Sunday
]
