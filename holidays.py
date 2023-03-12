from calendar import Calendar
import datetime

from constants import (
    FIXED_HOLIDAYS_ALL,
    NTH_DAY_OF_MONTH_HOLIDAYS,
    HOLIDAYS_BEFORE_A_CERTAIN_DAY,
    DAY_TO_INDEX,
)
from utils import find_easter_day, read_holidays_tuple


cal = Calendar()


def get_fixed_date_holidays(year: int, month: int = None, province: str = None) -> list:
    fixed_date_holidays = []

    if not month:
        if not province:
            # If no month is given, return all fixed holidays in the given year
            for month_key in FIXED_HOLIDAYS_ALL:
                read_holidays_tuple(fixed_date_holidays, FIXED_HOLIDAYS_ALL, year, month_key)
    else:
        if not province:
            # return fixed holidays in the given month in the given year
            read_holidays_tuple(fixed_date_holidays, FIXED_HOLIDAYS_ALL, year, month)
    return sorted(fixed_date_holidays)


def get_nth_day_of_month_holidays(year: int, prov: str) -> list:
    """
    Striding holidays are the ones nth day of a month
    ex: first Monday of the month

    Index of the array represents a week day
    ex: 0 - Monday, 1 - Tuesday, 2 - Wednesday, 3 - Thursday
        4 - Friday, 5 - Saturday, 6 - Sunday
    """
    nth_day_holidays = []
    province = get_province(prov)
    for month_key in NTH_DAY_OF_MONTH_HOLIDAYS[province]:
        for holiday_tuple in NTH_DAY_OF_MONTH_HOLIDAYS[province][month_key]:
            week_num, day, holiday_name = holiday_tuple
            day_index = DAY_TO_INDEX[day]
            hol = (
                cal.monthdatescalendar(year, month_key)[week_num][day_index],
                holiday_name,
            )
            nth_day_holidays.append(hol)
    return nth_day_holidays


def get_holidays_before_certain_dates(year: int, prov: str) -> list:
    """
    Holidays that precede a certain date or day
    ex: Victoria Day is Monday before May 25th
    """
    holidays_before_a_certain_date = []
    province = get_province(prov)

    for month in HOLIDAYS_BEFORE_A_CERTAIN_DAY[province]:
        for holiday_tuple in HOLIDAYS_BEFORE_A_CERTAIN_DAY[province][month]:
            day, preceding_day, holiday_name = holiday_tuple
            day_idx = DAY_TO_INDEX[day]
            if preceding_day == "Easter Sunday":
                preceding_datetime = find_easter_day(year)
            else:
                preceding_datetime = datetime.date(year, month, preceding_day)

            # Find the day before the preceding day
            days_in_month = cal.monthdatescalendar(year, month)
            for week_idx, week in enumerate(days_in_month):
                if preceding_datetime in week:
                    # Check if preceding_day is on the day or after
                    preceding_day_idx = week.index(preceding_datetime)
                    if day_idx < preceding_day_idx:
                        # The holiday is in the same week
                        hol = week[day_idx]
                    else:
                        # The holiday is in the previous week
                        hol = days_in_month[week_idx - 1]
                    holidays_before_a_certain_date.append((hol, holiday_name))

    return holidays_before_a_certain_date


def get_province(prov: str):
    province = prov.lower()
    if province in ["british columbia", "bc"]:
        province = "British Columbia"
    elif province in ["manitoba", "mb"]:
        province = "Manitoba"
    elif province in ["new brunswick", "nb"]:
        province = "New Brunswick"
    elif province in ["newfoundland", "newfoundland and labrador", "nl"]:
        province = "Newfoundland and Labrador"
    elif province in ["nova scotia", "ns"]:
        province = "Nova Scotia"
    elif province in ["ontario", "on"]:
        province = "Ontario"
    elif province in ["prince edward island", "pei"]:
        province = "Prince Edward Island"
    elif province in ["quebec", "qc"]:
        province = "Quebec"
    elif province in ["saskatchewan", "sk"]:
        province = "Saskatchewan"
    else:
        raise Exception(
            f"Cannot find the given province: {prov}. Please check your input."
        )

    return province


def get_all_holidays_in_year(year: int, prov: str):
    province = get_province(prov)
    print(f"Getting holiday information of {province} province...")
    return sorted(
        get_fixed_date_holidays(year)
        + get_nth_day_of_month_holidays(year, province)
        + get_holidays_before_certain_dates(year, province)
    )


def get_holidays_in_year_month(year: int, month: int, prov: str):
    province = get_province(prov)
    all_holidays_year = get_all_holidays_in_year(year, province)
    holidays_in_month = []
    for hol in all_holidays_year:
        # hol[0] is datetime of the holiday
        if hol[0].month == month:
            holidays_in_month.append(hol)
    return holidays_in_month


def is_holiday(year: int, month: int, day: int, prov: str) -> bool:
    """
    Check if the given date in the combination of year, month, and day
    is a holiday for the given Canadian province
    """
    province = get_province(prov)
    print(f"Getting holiday information of {province} province...")
    given_datetime = datetime.day(year, month, day)
    all_holidays_year = get_all_holidays_in_year(year, province)
    return given_datetime in all_holidays_year


def is_holiday(given_datetime: datetime.date, prov: str) -> bool:
    """
    Check if the given date in the form of datetime.date is a holiday
    for the given Canadian province
    """
    province = get_province(prov)
    print(f"Getting holiday information of {province} province...")
    all_holidays_year = get_all_holidays_in_year(given_datetime.year, province)
    return given_datetime in all_holidays_year
