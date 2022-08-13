import datetime

FIXED_DATE_HOLIDAYS = {
    "jan": "1",   # New Year's Day
    "jul": "1",   # Canada Day
    "dec": "25",  # Christmas Day
    "dec": "26",  # Boxing Day
}

# ex: first Monday of the month
STRIDING_HOLIDAYS = {
    "feb": "3/Mon",  # Family Day, 3rd Monday
    "sep": "1/Mon",  # Labour Day, 1st Monday
    "oct": "2/Mon",  # Thanksgiving Day, 2nd Monday
}

# ex: last Monday preceding a certain date/holiday
PRECEDING_HOLIDAYS = {
    "apr": "Fri/Easter Sunday",  # Good Friday (Friday before Easter Sunday)
    "may": "Mon/25"  # Victoria Day (Monday before May 25th)
}


def get_fixed_date_holidays(year: int, province: str):

    pass


def get_striding_holidays(year: int, province: str):
    pass


def get_preceding_holidays(year: int, province: str):
    pass


def find_all_holidays_in_year(year: int, province: str):
    province = province.lower()
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

    return get_fixed_date_holidays(year, province) + get_striding_holidays(year, province) + get_preceding_holidays(year, province)


def find_holidays_in_a_month(year: int, month: int, province: str):
    pass


def is_holiday(year: int, month: int, day: int, province: str):
    pass