import click
import datetime

FIXED_DATE_HOLIDAYS = {
    # Month : Day
    1: [(1, "New Year's Day")],
    7: [(1, "Canada Day")],
    12: [(25, "Christmas Day"), (26, "Boxing Day")],
}

# ex: first Monday of the month
STRIDING_HOLIDAYS = {
    2: (3, "Mon"),  # Family Day, 3rd Monday
    9: (1, "Mon"),  # Labour Day, 1st Monday
    10: (2, "Mon"),  # Thanksgiving Day, 2nd Monday
}

# ex: last Monday preceding a certain date/holiday
PRECEDING_HOLIDAYS = {
    "apr": "Fri/Easter Sunday",  # Good Friday (Friday before Easter Sunday)
    "may": "Mon/25",  # Victoria Day (Monday before May 25th)
}


def read_holidays_tuple(
    holidays_result: list,
    holidays_tuple: tuple,
    year: int = None,
    month: int = None,
) -> None:
    for day_tuple in holidays_tuple[month]:
        day, name = day_tuple
        holiday = datetime.date(year, month, day)
        holidays_result.append((holiday, name))


def get_fixed_date_holidays(year: int, month: int = None) -> list:
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
    return (
        get_fixed_date_holidays(year)
        + get_striding_holidays(year, province)
        + get_preceding_holidays(year, province)
    )


def find_holidays_in_year_month(year: int, month: int, province: str):
    pass


def is_holiday(year: int, month: int, day: int, province: str):
    pass


@click.command()
@click.option("-y", "--year", "year", type=int, help="Year to search")
@click.option("-m", "--month", "month", type=int, help="Month to search")
@click.option("-d", "--day", "day", type=int, help="Day to search")
@click.option("-p", "--province", "province", default="ON", help="Province to search")
def main(year, month, day, province):
    print(f"year: {year}, month: {month}, day: {day}, province: {province}")
    fixed_holidays = get_fixed_date_holidays(year, month)
    print(fixed_holidays)


if __name__ == "__main__":
    main()
