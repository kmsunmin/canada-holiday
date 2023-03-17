from calendar import Calendar
import datetime

from utils import find_easter_day

cal = Calendar()
DAY_TO_INDEX = {"mon": 0, "tue": 1, "wed": 2, "thr": 3, "fri": 4, "sat": 5, "sun": 6}


class Holiday:
    def __init__(
        self,
        name: str,
        month: int,
        day: int = None,
        *,
        date: datetime.date = None,
        nth_day: (int, str) = None,
        preceding_date: (str, int) = None,
        province: str = None,
        succeeding_date: (str, int) = None,
    ):
        self.name = name
        self.month = month
        self.day = day  # ex: Monday, Tuesday
        self.date = date  # ex: datetime.date(2023, 12, 25)
        self.nth_day = nth_day
        self.preceding_date = preceding_date
        self.province = province
        self.succeeding_date = succeeding_date

    def to_date(self, year: int):
        if not self.nth_day and not self.preceding_date and not self.succeeding_date:
            return datetime.date(year, self.month, self.day)

        if self.nth_day:
            if self.preceding_date or self.succeeding_date:
                raise Exception(f"Please check the Holiday: {self.name}.")
            n, day_str = self.nth_day
            day_idx = DAY_TO_INDEX[day_str]
            # TODO: edge case for n is not necessarily same as week index
            return cal.monthdatescalendar(year, self.month)[n][day_idx]
        elif self.preceding_date:
            if self.nth_day and self.succeeding_date:
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
        elif self.succeeding_date:
            if self.nth_day and self.preceding_date:
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
            delta_days = 7 - abs(succeed_day_idx - day_str_idx)
            # Find 'day_str' after succeed_date
            return succeed_date + datetime.timedelta(days=delta_days)
