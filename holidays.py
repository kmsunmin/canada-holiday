from calendar import Calendar

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
    NATIONAL_HOLIDAYS,
)
from utils import (
    check_province_name,
    filter_list_of_holidays_by_month,
    sort_list_of_holidays_by_date,
    update_list_of_holidays_to_date,
)


cal = Calendar()


def get_province_holidays(prov: str) -> list:
    """
    Returns holidays that are specific to the given province.
    """
    province = prov.lower()

    if province in ["alberta", "ab"]:
        provincial_holidays = ALBERTA
    elif province in ["british columbia", "bc"]:
        provincial_holidays = BRITISH_COLUMBIA
    elif province in ["manitoba", "mb"]:
        provincial_holidays = MANITOBA
    elif province in ["new brunswick", "nb"]:
        provincial_holidays = NEW_BRUNSWICK
    elif province in ["newfoundland", "newfoundland and labrador", "nl"]:
        provincial_holidays = NEWFOUNDLAND_AND_LABRADOR
    elif province in ["northwest territories", "nt"]:
        provincial_holidays = NORTHWEST_TERRITORIES
    elif province in ["nova scotia", "ns"]:
        provincial_holidays = NOVA_SCOTIA
    elif province in ["nunavut", "nu"]:
        provincial_holidays = NUNAVUT
    elif province in ["ontario", "on"]:
        provincial_holidays = ONTARIO
    elif province in ["prince edward island", "pe"]:
        provincial_holidays = PRINCE_EDWARD_ISLAND
    elif province in ["quebec", "qc"]:
        provincial_holidays = QUEBEC
    elif province in ["saskatchewan", "sk"]:
        provincial_holidays = SASKATCHEWAN
    elif province in ["yukon", "yt"]:
        provincial_holidays = YUKON
    else:
        raise Exception(
            f"Cannot find the given province: {prov}. Please check your input."
        )
    return provincial_holidays


def get_all_holidays(province: str, year: int, month: int = None) -> list:
    """
    Get all holidays of the given province in the given year.
    """
    all_holidays = []
    province_name = check_province_name(province)
    province_holidays = get_province_holidays(province_name)
    all_holidays.extend(province_holidays)
    print(f"Getting holiday information of {province_name} province...")

    # Combine with Canadian national holidays
    all_holidays.extend(NATIONAL_HOLIDAYS)

    # If month presents, filter all_holidays for the given month
    if month and isinstance(month, int):
        all_holidays = filter_list_of_holidays_by_month(all_holidays, month)

    # Convert holidays to date
    updated_all_holidays = update_list_of_holidays_to_date(all_holidays, year)
    all_holidays_in_order = sort_list_of_holidays_by_date(updated_all_holidays)
    return all_holidays_in_order


def is_holiday(year: int, month: int, day: int, prov: str) -> bool:
    """
    Check if the given date in the combination of year, month, and day
    is a holiday for the given Canadian province
    """
    province_name = check_province_name(prov)
    holidays_for_province = get_all_holidays(province_name, year, month)

    for h in holidays_for_province:
        if h.year == year and h.month == month and h.day == day:
            print(
                f"{month}-{day}-{year} is a holiday, {h.name} in {h.province} province(s) in Canada"
            )
            return True

    print(f"{month}-{day}-{year} is not a holiday in {province_name} province.")
    return False


if __name__ == "__main__":
    results = get_all_holidays("Ontario", 2023)
    print(results)
