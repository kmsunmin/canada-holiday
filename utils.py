import datetime
import math

from holiday import cal, DAY_TO_INDEX


def check_province_name(prov: str):
    province = prov.lower()

    if province in ["alberta", "ab"]:
        provincial_name = "Alberta"
    elif province in ["british columbia", "bc"]:
        provincial_name = "British Columbia"
    elif province in ["manitoba", "mb"]:
        provincial_name = "Manitoba"
    elif province in ["new brunswick", "nb"]:
        provincial_name = "New Brunswick"
    elif province in ["newfoundland", "newfoundland and labrador", "nl"]:
        provincial_name = "Newfoundland and Labrador"
    elif province in ["northwest territories", "nt"]:
        provincial_name = "Northwest Territories"
    elif province in ["nova scotia", "ns"]:
        provincial_name = "Nova Scotia"
    elif province in ["nunavut", "nu"]:
        provincial_name = "Nunavut"
    elif province in ["ontario", "on"]:
        provincial_name = "Ontario"
    elif province in ["prince edward island", "pe"]:
        provincial_name = "Prince Edward Island"
    elif province in ["quebec", "qc"]:
        provincial_name = "Quebec"
    elif province in ["saskatchewan", "sk"]:
        provincial_name = "Saskatchewan"
    elif province in ["yukon", "yt"]:
        provincial_name = "Yukon"
    else:
        raise Exception(
            f"Cannot find the given province: {prov}. Please check your input."
        )
    return provincial_name


def find_easter_day(year: int) -> datetime.date:
    """
    # Use algorithm to find the date of Easter day
    # Reference: https://www.geeksforgeeks.org/how-to-calculate-the-easter-date-for-a-given-year-using-gauss-algorithm/
    """
    A = year % 19
    B = year % 4
    C = year % 7
    P = math.floor(year / 100)
    Q = math.floor((13 + 8 * P) / 25)
    M = 15 - Q + P - (P // 4) % 30
    N = 4 + P - (P // 4) % 7
    D = (19 * A + M) % 30
    E = (N + 2 * B + 4 * C + 6 * D) % 7
    days = 22 + D + E

    # A corner case: when D is 29
    if (D == 29) and (E == 6):
        easter_day = datetime.date(year, 4, 19)
        return easter_day
    # Another corner case: when D is 28
    elif (D == 28) and (E == 6):
        easter_day = datetime.date(year, 4, 18)
        return easter_day
    else:
        # If days > 31, move to April
        if days > 31:
            easter_day = datetime.date(year, 4, days - 31)
            return easter_day
        else:
            # Otherwise, stay on March
            easter_day = datetime.date(year, 3, days)
            return easter_day


def update_list_of_holidays_to_date(holidays: list, year: int) -> list:
    updated_holidays_list = holidays.copy()
    for h in updated_holidays_list:
        h.year = year
        h.date = h.to_date(year)
        h.day = h.date.day
    return updated_holidays_list


def sort_list_of_holidays_by_date(holidays: list) -> list:
    """
    Sort the given list of Holidays bt their date.
    """
    return sorted(holidays, key=lambda h: h.date)


def filter_list_of_holidays_by_month(holidays: list, month: int) -> list:
    return [h for h in holidays if h.month == month]


def get_last_day_str_of_month(self, year, month, day_str) -> datetime.date:
    """
    Find the last day string of the month.
    ex: last Sunday of the given month
    """
    day_idx = DAY_TO_INDEX[day_str]
    weeks = cal.monthdatescalendar(year, month)
    if weeks[-1][day_idx].month == month:
        return weeks[-1][day_idx]
    else:
        return weeks[-2][day_idx]
