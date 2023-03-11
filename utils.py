import datetime


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