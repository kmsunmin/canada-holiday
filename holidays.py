from calendar import Calendar
import datetime

from holiday_instances import national, all
from utils import (
    check_province_name,
    filter_list_of_holidays_by_month,
    sort_list_of_holidays,
    update_list_of_holidays,
)


cal = Calendar()


def get_province_holidays(prov: str) -> list:
    """
    Returns holidays that are specific to the given province.
    """
    province = check_province_name(prov)
    all_holidays_in_province = all.HOLIDAYS_DICT[province]
    print(f"Getting holiday information of {province} province...")

    # Combine with Canadian national holidays
    all_holidays_in_province.extend(national.HOLIDAYS)
    return all_holidays_in_province


def get_provincial_holiday_info(province: str) -> list:
    provincial_holidays = []
    province_name = check_province_name(province)
    province_holidays = get_province_holidays(province_name)
    provincial_holidays.extend(province_holidays)
    print(f"Getting holiday information of {province_name} province...")

    # Combine with Canadian national holidays
    provincial_holidays.extend(NATIONAL)
    return provincial_holidays


def get_holidays(province: str, year: int, month: int = None) -> list:
    """
    Get all holidays of the given province in the given year.
    """
    holidays = get_province_holidays(province)
    all_holidays = []

    # If month presents, filter all_holidays for the given month
    if month and isinstance(month, int):
        all_holidays = filter_list_of_holidays_by_month(holidays, month)

    # Update holiday objects to have date
    updated_all_holidays = update_list_of_holidays(all_holidays, year)
    sorted_all_holidays = sort_list_of_holidays(updated_all_holidays)
    return sorted_all_holidays


def is_holiday(date: datetime.date, prov: str) -> bool:
    """
    Check if the given datetime.date is a holiday for the given Canadian province.
    """
    province_name = check_province_name(prov)
    holidays_for_province = get_holidays(province_name, date.year, date.month)

    for h in holidays_for_province:
        if h.date == date:
            print(
                f"{date.month}-{date.day}-{date.year} is a holiday, {h.name} in {h.province} province(s) in Canada"
            )
            return True
        print(
            f"{date.month}-{date.day}-{date.year} is not a holiday in {province_name} province."
        )
        return False


if __name__ == "__main__":
    results = get_holidays("Ontario", 2023)
    print(results)
