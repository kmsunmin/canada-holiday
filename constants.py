from holiday import Holiday


NATIONAL_HOLIDAYS = [
    Holiday("New Year's Day", month=1, day=1, province="all"),
    Holiday(
        "Victoria Day", month=5, preceding_date=("mon", 25), province="all"
    ),  # Monday before May 25th
    Holiday("Canada Day", month=7, day=1, province="all"),
    Holiday(
        "Labour Day", month=9, nth_day=(1, "mon"), province="all"
    ),  # 1st Monday in September
    Holiday(
        "National Day for Truth and Reconciliation", month=9, day=30, province="Ontario"
    ),
    Holiday(
        "Thanksgiving Day", month=10, nth_day=(2, "mon"), province="all"
    ),  # 2nd Monday in October
    Holiday("Christmas Day", month=12, day=25, province="all"),
    Holiday("Boxing Day", month=12, day=26, province="all"),
]

ALBERTA = []
BRITISH_COLUMBIA = []
MANITOBA = []
NEW_BRUNSWICK = []
NEWFOUNDLAND_AND_LABRADOR = []
NORTHWEST_TERRITORIES = []
NOVA_SCOTIA = []
NUNAVUT = []
ONTARIO = [
    Holiday(
        "Family Day", month=2, nth_day=(3, "mon"), province="Ontario"
    ),  # 3rd Monday in February
    Holiday(
        "Good Friday",
        month=4,
        preceding_date=("fri", "Easter Sunday"),
        province="Ontario",
    ),  # Friday before Easter Sunday
    Holiday(
        "Easter Monday",
        month=4,
        succeeding_date=("mon", "Easter Sunday"),
        province="Ontario",
    ),  # Monday after Easter Sunday
    Holiday(
        "Civic Holiday", month=8, nth_day=(1, "mon"), province="Ontario"
    ),  # 1st Monday in August
]
PRINCE_EDWARD_ISLAND = []
QUEBEC = []
SASKATCHEWAN = []
YUKON = []
