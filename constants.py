from holiday import Holiday


FIXED_HOLIDAYS_ALL = {
    # Month : Day
    1: [(1, "New Year's Day")],
    7: [(1, "Canada Day")],
    9: [(30, "National Day for Truth and Reconciliation")],
    12: [(25, "Christmas Day"), (26, "Boxing Day")],
}

FIXED_HOLIDAYS_PROVINCIAL = {
    "Alberta": {},
    "British Columbia": {},
    "Manitoba": {},
    "New Brunswick": {},
    "Newfoundland and Labrador": {},
    "Northwest Territories": {},
    "Nova Scotia": {},
    "Nunavut": {},
    "Ontario": {},
    "Prince Edward Island": {},
    "Quebec": {
        6: [(24, "Saint-Jean-Baptiste Day (Quebec only)")]
    },
    "Saskatchewan": {},
    "Yukon": {},
}

NATIONAL_HOLIDAYS = [
    Holiday("New Year's Day", 1, 1),
    Holiday("Victoria Day", 5, preceding_date=("mon", 25)),  # Monday before May 25th
    Holiday("Canada Day", 7, 1),
    Holiday("Labour Day", 9, nth_day=(1, "mon")),  # 1st Monday in September
    Holiday("Thanksgiving Day", 10, nth_day=(2, "mon")),  # 2nd Monday in October
    Holiday("Christmas Day", 12, 25),
    Holiday("Boxing Day", 12, 26),
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
    Holiday("Family Day", 2, nth_day=(3, "mon")),  # 3rd Monday in February
    Holiday("Good Friday", 4, preceding_date=("fri", "Easter Sunday")),  # Friday before Easter Sunday
    Holiday("Easter Monday", 4, succeeding_date=("mon", "Easter Sunday")),  # Monday after Easter Sunday
    Holiday("Civic Holiday", 8, nth_day=(1, "mon")),  # 1st Monday in August
    Holiday("National Day for Truth and Reconciliation", 9, 30),
]
PRINCE_EDWARD_ISLAND = []
QUEBEC = []
SASKATCHEWAN = []
YUKON = []

# ex: first Monday of the month
NTH_DAY_OF_MONTH_HOLIDAYS = {
    "Alberta": {},
    "British Columbia": {},
    "Manitoba": {},
    "New Brunswick": {},
    "Newfoundland and Labrador": {},
    "Northwest Territories": {},
    "Nova Scotia": {},
    "Nunavut": {},
    "Ontario": {
        2: [(3, "mon", "Family Day")],  # Family Day, 3rd Monday
        9: [(1, "mon", "Labour Day")],  # Labour Day, 1st Monday
        10: [(2, "mon", "Thanksgiving Day")],  # Thanksgiving Day, 2nd Monday
    },
    "Prince Edward Island": {},
    "Quebec": {},
    "Saskatchewan": {},
    "Yukon": {},
}

# ex: last Monday preceding a certain date/holiday
HOLIDAYS_BEFORE_A_CERTAIN_DAY = {
    "Alberta": {},
    "British Columbia": {},
    "Manitoba": {},
    "New Brunswick": {},
    "Newfoundland and Labrador": {},
    "Northwest Territories": {},
    "Nova Scotia": {},
    "Nunavut": {},
    "Ontario": {
        4: [
            ("fri", "Easter Sunday", "Good Friday")
        ],  # Good Friday (Friday before Easter Sunday)
        5: [("mon", 25, "Victoria Day")],  # Victoria Day (Monday before May 25th)
    },
    "Prince Edward Island": {},
    "Quebec": {},
    "Saskatchewan": {},
    "Yukon": {},
}

HOLIDAYS_AFTER_A_CERTAIN_DAY = {}

