import datetime
import math


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