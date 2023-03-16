from calendar import Calendar
import datetime

from constants import (
    ALBERTA,
    BRITISH_COLUMBIA,
    MANITOBA,
    NEW_BRUNSWICK,
    NEWFOUNDLAND_AND_LABRADOR,
    NORTHWEST_TERRITORIES,
    NOVA_SCOTIA,
    NUNAVUT,
    ONTARIO,
    PRINCE_EDWARD_ISLAND,
    QUEBEC,
    SASKATCHEWAN,
    YUKON,
    NATIONAL_HOLIDAYS
)
cal = Calendar()


def get_province_holidays(prov: str):
    province = prov.lower()
    provincial_holidays = ()
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
    province_holidays = get_province_holidays(prov)
    print(f"Getting holiday information of {province} province...")
    return


def get_holidays_in_year_month(year: int, month: int, prov: str):
    province_holidays = get_province_holidays(prov)
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
    province = get_province_holidays(prov)
    print(f"Getting holiday information of {province} province...")
    given_datetime = datetime.day(year, month, day)
    all_holidays_year = get_all_holidays_in_year(year, province)
    return given_datetime in all_holidays_year


def is_holiday(given_datetime: datetime.date, prov: str) -> bool:
    """
    Check if the given date in the form of datetime.date is a holiday
    for the given Canadian province
    """
    province = get_province_holidays(prov)
    print(f"Getting holiday information of {province} province...")
    all_holidays_year = get_all_holidays_in_year(given_datetime.year, province)
    return given_datetime in all_holidays_year
