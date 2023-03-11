FIXED_DATE_HOLIDAYS = {
    # Month : Day
    1: [(1, "New Year's Day")],
    7: [(1, "Canada Day")],
    12: [(25, "Christmas Day"), (26, "Boxing Day")],
}

# ex: first Monday of the month
STRIDING_HOLIDAYS_ON = {
    2: [(3, "mon", "Family Day")],  # Family Day, 3rd Monday
    9: [(1, "mon", "Labour Day")],  # Labour Day, 1st Monday
    10: [(2, "mon", "Thanksgiving Day")],  # Thanksgiving Day, 2nd Monday
}

# ex: last Monday preceding a certain date/holiday
PRECEDING_HOLIDAYS_ON = {
    4: [
        ("fri", "Easter Sunday", "Good Friday")
    ],  # Good Friday (Friday before Easter Sunday)
    5: [("mon", 25, "Victoria Day")],  # Victoria Day (Monday before May 25th)
}

DAY_TO_INDEX = {"mon": 0, "tue": 1, "wed": 2, "thr": 3, "fri": 4, "sat": 5, "sun": 6}