from calendar import Calendar
import datetime

from utils import find_easter_day

cal = Calendar()
DAY_TO_INDEX = {"mon": 0, "tue": 1, "wed": 2, "thr": 3, "fri": 4, "sat": 5, "sun": 6}


class CanadaHoliday:
    def __init__(
        self,
        name: str,
        month: int,
        *,
        year: int = None,
        day: int = None,
        date: datetime.date = None,
        nearest_day: (str, int) = None,
        nth_day: (str, int) = None,
        preceding_date: (str, int) = None,
        province: str = None,
        succeeding_date: (str, int) = None,
    ):
        self.name = name
        self.month = month
        self.year = year
        self.day = day  # ex: Monday, Tuesday
        self.date = date  # ex: datetime.date(2023, 12, 25)
        self.nearest_day = nearest_day
        self.nth_day = nth_day
        self.preceding_date = preceding_date
        self.province = province
        self.succeeding_date = succeeding_date

    def get_nth_day_holiday(self, year: int) -> datetime.date:
        if self.preceding_date or self.succeeding_date or self.nearest_day:
            raise Exception(f"Please check the Holiday: {self.name}.")
        day_str, n = self.nth_day
        day_idx = DAY_TO_INDEX[day_str]
        # TODO: edge case for n is not necessarily same as week index
        day_in_first_week = cal.monthdatescalendar(year, self.month)[0][day_idx]
        if day_in_first_week.month == self.month and day_in_first_week.day > 7:
            return cal.monthdatescalendar(year, self.month)[n - 1][day_idx]
        else:
            return cal.monthdatescalendar(year, self.month)[n][day_idx]

    def get_preceding_day_holiday(self, year: int) -> datetime.date:
        if self.nth_day or self.succeeding_date or self.nearest_day:
            raise Exception(f"Please check the Holiday: {self.name}.")

        day_str, preceding_day = self.preceding_date  # ex: Monday before May 25th
        day_str_idx = DAY_TO_INDEX[day_str]

        if preceding_day == "Easter Sunday":
            precede_date = find_easter_day(year)
        else:
            precede_date = datetime.date(year, self.month, preceding_day)
        precede_day_idx = precede_date.weekday()
        delta_days = abs(precede_day_idx - day_str_idx)
        # Find 'day_str' before easter_day
        return precede_date - datetime.timedelta(days=delta_days)

    def get_succeeding_day_holiday(self, year: int) -> datetime.date:
        if self.nth_day or self.preceding_date or self.nearest_day:
            raise Exception(f"Please check the Holiday: {self.name}.")

        (
            day_str,
            succeeding_day,
        ) = self.succeeding_date  # ex: Monday after Easter Sunday
        day_str_idx = DAY_TO_INDEX[day_str]

        if succeeding_day == "Easter Sunday":
            succeed_date = find_easter_day(year)
        else:
            succeed_date = datetime.date(year, self.month, succeeding_day)
        succeed_day_idx = succeed_date.weekday()
        delta_days = abs(succeed_day_idx - day_str_idx)
        # Find 'day_str' after succeed_date
        return succeed_date + datetime.timedelta(days=(7 - delta_days))

    def get_nearest_day_holiday(self, year: int) -> datetime.date:
        if self.nth_day or self.preceding_date or self.succeeding_date:
            raise Exception(f"Please check the Holiday: {self.name}.")

        day_str, nearest_day = self.nearest_day
        day_str_idx = DAY_TO_INDEX[day_str]
        """
        Example of calculating nearest Monday:
        if 23 is Sunday (6)    Monday (0) day + (7 - delta:6)
        if 23 is Tuesday (1)   Monday (0) day - delta:1
        if 23 is Wednesday (2) Monday (0) day - delta:2
        if 23 is Thursday (3)  Monday (0) day - delta:3
        if 23 is Friday (4)    Monday (0) day + (7 - delta:4)
        if 23 is Saturday (5)  Monday (0) day + (7 - delta:5)
        """
        nearest_date = datetime.date(year, self.month, self.nearest_day[1])
        nearest_day_str_idx = nearest_date.weekday()
        delta_days = abs(day_str_idx - nearest_day_str_idx)

        if delta_days < 4:
            return nearest_date - datetime.timedelta(delta_days)
        else:
            return nearest_date + datetime.timedelta(7 - delta_days)

    def to_date(self, year: int):
        if (
            not self.nth_day
            and not self.preceding_date
            and not self.succeeding_date
            and not self.nearest_day
        ):
            return datetime.date(year, self.month, self.day)

        date = None
        if self.nth_day:
            date = self.get_nth_day_holiday(year)
        elif self.preceding_date:
            date = self.get_preceding_day_holiday(year)
        elif self.succeeding_date:
            date = self.get_succeeding_day_holiday(year)
        elif self.nearest_day:
            date = self.get_nearest_day_holiday(year)

        return date
