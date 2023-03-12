FIXED_HOLIDAYS_ALL = {
    # Month : Day
    1: [(1, "New Year's Day")],
    7: [(1, "Canada Day")],
    9: [(30, "National Day for Truth and Reconciliation")],
    12: [(25, "Christmas Day"), (26, "Boxing Day")],
}

FIXED_HOLIDAYS_PROVINCIAL = {
    "British Columbia": {},
    "Manitoba": {},
    "New Brunswick": {},
    "Newfoundland and Labrador": {},
    "Nova Scotia": {},
    "Ontario": {},
    "Prince Edward Island": {},
    "Quebec": {
        6: [(24, "Saint-Jean-Baptiste Day (Quebec only)")]
    },
    "Saskatchewan": {},
}

# ex: first Monday of the month
NTH_DAY_OF_MONTH_HOLIDAYS = {
    "British Columbia": {},
    "Manitoba": {},
    "New Brunswick": {},
    "Newfoundland and Labrador": {},
    "Nova Scotia": {},
    "Ontario": {
        2: [(3, "mon", "Family Day")],  # Family Day, 3rd Monday
        9: [(1, "mon", "Labour Day")],  # Labour Day, 1st Monday
        10: [(2, "mon", "Thanksgiving Day")],  # Thanksgiving Day, 2nd Monday
    },
    "Prince Edward Island": {},
    "Quebec": {},
    "Saskatchewan": {},
}

# ex: last Monday preceding a certain date/holiday
HOLIDAYS_BEFORE_A_CERTAIN_DAY = {
    "British Columbia": {},
    "Manitoba": {},
    "New Brunswick": {},
    "Newfoundland and Labrador": {},
    "Nova Scotia": {},
    "Ontario": {
        4: [
            ("fri", "Easter Sunday", "Good Friday")
        ],  # Good Friday (Friday before Easter Sunday)
        5: [("mon", 25, "Victoria Day")],  # Victoria Day (Monday before May 25th)
    },
    "Prince Edward Island": {},
    "Quebec": {},
    "Saskatchewan": {},
}

HOLIDAYS_AFTER_A_CERTAIN_DAY = {}

DAY_TO_INDEX = {"mon": 0, "tue": 1, "wed": 2, "thr": 3, "fri": 4, "sat": 5, "sun": 6}
