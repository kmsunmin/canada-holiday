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
from utils import convert_list_of_holidays_to_date


cal = Calendar()


def get_province_holidays(prov: str):
    province = prov.lower()

    if province in ["alberta", "ab"]:
        name = "Alberta"
        provincial_holidays = ALBERTA
    elif province in ["british columbia", "bc"]:
        name = "British Columbia"
        provincial_holidays = BRITISH_COLUMBIA
    elif province in ["manitoba", "mb"]:
        name = "Manitoba"
        provincial_holidays = MANITOBA
    elif province in ["new brunswick", "nb"]:
        name = "New Brunswick"
        provincial_holidays = NEW_BRUNSWICK
    elif province in ["newfoundland", "newfoundland and labrador", "nl"]:
        name = "Newfoundland and Labrador"
        provincial_holidays = NEWFOUNDLAND_AND_LABRADOR
    elif province in ["northwest territories", "nt"]:
        name = "Northwest Territories"
        provincial_holidays = NORTHWEST_TERRITORIES
    elif province in ["nova scotia", "ns"]:
        name = "Nova Scotia"
        provincial_holidays = NOVA_SCOTIA
    elif province in ["nunavut", "nu"]:
        name = "Nunavut"
        provincial_holidays = NUNAVUT
    elif province in ["ontario", "on"]:
        name = "Ontario"
        provincial_holidays = ONTARIO
    elif province in ["prince edward island", "pe"]:
        name = "Prince Edward Island"
        provincial_holidays = PRINCE_EDWARD_ISLAND
    elif province in ["quebec", "qc"]:
        name = "Quebec"
        provincial_holidays = QUEBEC
    elif province in ["saskatchewan", "sk"]:
        name = "Saskatchewan"
        provincial_holidays = SASKATCHEWAN
    elif province in ["yukon", "yt"]:
        name = "Yukon"
        provincial_holidays = YUKON
    else:
        raise Exception(
            f"Cannot find the given province: {prov}. Please check your input."
        )
    return name, provincial_holidays


def get_all_holidays(province: str, year: int):
    """
    Get all holidays of the given province in the given year.
    """
    all_holidays = []
    province_name, province_holidays = get_province_holidays(province)
    all_holidays.extend(province_holidays)
    print(f"Getting holiday information of {province_name} province...")

    # Combine with Canadian national holidays
    all_holidays.extend(NATIONAL_HOLIDAYS)

    # Convert holidays to date
    all_holidays_date = convert_list_of_holidays_to_date(all_holidays, year)
    return all_holidays_date


def get_all_holidays(province: str, year: int, month: int):
    """
    Get all holidays of the given province in the given year and month.
    """
    all_holidays = []
    province_name, province_holidays = get_province_holidays(province)
    all_holidays.extend(province_holidays)
    print(f"Getting holiday information of {province_name} province...")

    # Combine with Canadian national holidays
    all_holidays.extend(NATIONAL_HOLIDAYS)

    # Trim all_holidays to the ones in the given month
    for h in all_holidays:
        if h.month != month:
            all_holidays.remove(h)

    # Convert holidays to date
    all_holidays_date = convert_list_of_holidays_to_date(all_holidays, year)
    return all_holidays_date


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
