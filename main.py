import datetime

FIXED_DATE_HOLIDAYS = {
    # Month : Day
    1: (1,),       # New Year's Day
    7: (1,),       # Canada Day
    12: (25, 26)  # Christmas Day, Boxing Day
}

# ex: first Monday of the month
STRIDING_HOLIDAYS = {
    2: (3, "Mon"),  # Family Day, 3rd Monday
    9: (1, "Mon"),  # Labour Day, 1st Monday
    10: (2, "Mon")  # Thanksgiving Day, 2nd Monday
}

# ex: last Monday preceding a certain date/holiday
PRECEDING_HOLIDAYS = {
    "apr": "Fri/Easter Sunday",  # Good Friday (Friday before Easter Sunday)
    "may": "Mon/25"  # Victoria Day (Monday before May 25th)
}


def get_fixed_date_holidays(year: int, month: int = None):
    fixed_date_holidays = []
    for month_key in FIXED_DATE_HOLIDAYS:
        for day in FIXED_DATE_HOLIDAYS[month_key]:
            holiday = datetime.date(year, month_key, day)
            fixed_date_holidays.append(holiday)

    return sorted(fixed_date_holidays)


def get_striding_holidays(year: int, province: str):
    pass


def get_preceding_holidays(year: int, province: str):
    pass


def get_province(prov: str):
    province = prov.lower()
    if province in ["british columbia", "bc"]:
        province = "bc"
    elif province in ["manitoba", "mb"]:
        province = "mb"
    elif province in ["new brunswick", "nb"]:
        province = "nb"
    elif province in ["newfoundland", "newfoundland and labrador", "nl"]:
        province = "nl"
    elif province in ["nova scotia", "ns"]:
        province = "ns"
    elif province in ["ontario", "on"]:
        province = "on"
    elif province in ["prince edward island", "pe"]:
        province = "pe"
    elif province in ["quebec", "qc"]:
        province = "qc"
    elif province in ["saskatchewan", "sk"]:
        province = "sk"

    return province


def find_all_holidays_in_year(year: int, prov: str):
    province = get_province(prov)
    return get_fixed_date_holidays(year) + get_striding_holidays(year, province) + get_preceding_holidays(year, province)


def find_holidays_in_a_month(year: int, month: int, province: str):
    # get_fixed_date_holidays(year)
    pass


def is_holiday(year: int, month: int, day: int, province: str):
    pass
