from calendar import Calendar
import datetime
import math
from typing import List

from constants import (
    FIXED_DATE_HOLIDAYS,
    STRIDING_HOLIDAYS_ON,
    PRECEDING_HOLIDAYS_ON,
    DAY_TO_INDEX,
)
from utils import read_holidays_tuple


cal = Calendar()


def get_fixed_date_holidays(year: int, month: int = None) -> List[(datetime.date, str)]:
    fixed_date_holidays = []

    if not month:
        # If no month is given, return all fixed holidays in the given year
        for month_key in FIXED_DATE_HOLIDAYS:
            read_holidays_tuple(
                fixed_date_holidays, FIXED_DATE_HOLIDAYS, year, month_key
            )
    else:
        # return fixed holidays in the given month in the given year
        read_holidays_tuple(fixed_date_holidays, FIXED_DATE_HOLIDAYS, year, month)

    return sorted(fixed_date_holidays)


def get_striding_holidays(year: int, province: str) -> List[(datetime.date, str)]:
    """
    Striding holidays are the ones nth day of a month
    ex: first Monday of the month

    Index of the array represents a week day
    ex: 0 - Monday, 1 - Tuesday, 2 - Wednesday, 3 - Thursday
        4 - Friday, 5 - Saturday, 6 - Sunday
    """
    striding_holidays = []
    if province.lower() == "on":
        for month_key in STRIDING_HOLIDAYS_ON:
            for holiday_tuple in STRIDING_HOLIDAYS_ON[month_key]:
                week_num, day, holiday_name = holiday_tuple
                day_index = DAY_TO_INDEX[day]
                str_hol = (
                    cal.monthdatescalendar(year, month_key)[week_num][day_index],
                    holiday_name,
                )
                striding_holidays.append(str_hol)
    return striding_holidays


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


def get_preceding_holidays(year: int, province: str) -> List[(datetime.date, str)]:
    """
    Preceding holidays are the ones before a certain date or day
    ex: Victoria Day is Monday before May 25th
    """
    preceding_holidays = []
    if province.lower() == "on":
        for month_key in PRECEDING_HOLIDAYS_ON:
            for holiday_tuple in PRECEDING_HOLIDAYS_ON[month_key]:
                day, preceding_date, holiday_name = holiday_tuple
                day_idx = DAY_TO_INDEX[day]
                if preceding_date == "Easter Sunday":
                    preceding_datetime = find_easter_day(year)
                else:
                    preceding_datetime = datetime.date(year, month_key, preceding_date)

                # Find the day before the preceding date
                month_dates = cal.monthdatescalendar(year, month_key)
                for week_idx, week in enumerate(month_dates):
                    if preceding_datetime in week:
                        # Check if preceding_date is the day or after
                        preceding_day_idx = week.index(preceding_datetime)
                        if day_idx < preceding_day_idx:
                            # The holiday is in the same week
                            pre_hol = week[day_idx]
                        else:
                            # The holiday is in the previous week
                            pre_hol = month_dates[week_idx - 1]
                        preceding_holidays.append((pre_hol, holiday_name))

    return preceding_holidays


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
    return sorted(
        get_fixed_date_holidays(year)
        + get_striding_holidays(year, province)
        + get_preceding_holidays(year, province)
    )


def find_holidays_in_year_month(year: int, month: int, province: str):
    all_holidays_year = find_all_holidays_in_year(year, province)
    holidays_in_month = []
    for hol in all_holidays_year:
        # hol[0] is datetime of the holiday
        if hol[0].month == month:
            holidays_in_month.append(hol)
    return holidays_in_month


def is_holiday(year: int, month: int, day: int, province: str) -> bool:
    given_datetime = datetime.day(year, month, day)
    all_holidays_year = find_all_holidays_in_year(year, province)
    return given_datetime in all_holidays_year
