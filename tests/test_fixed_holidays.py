import datetime

from holidays import get_fixed_date_holidays


EXPECTED_FIXED_DATE_HOLIDAYS = {
    # Month : Day
    1: [(1, "New Year's Day")],
    7: [(1, "Canada Day")],
    9: [(30, "Truth and Reconciliation")],
    12: [(25, "Christmas Day"), (26, "Boxing Day")],
}


def convert_fixed_holiday_to_datetime(holidays: dict, year) -> list:
    """
    Helper function to convert the dictionary of holidays to a tuple of (datetime.date, holiday name)
    """
    holidays_datetime = []
    for expected_fh_month in holidays:
        for expected_fh_day in holidays[expected_fh_month]:
            day, holiday_name = expected_fh_day
            expected_hol_datetime = datetime.date(year, expected_fh_month, day)
            holidays_datetime.append((expected_hol_datetime, holiday_name))
    return holidays_datetime


class TestFixedDateHolidays:
    def test_all_fixed_date_holidays_are_returned(self):
        """
        For fixed date holidays, year may not matter much, but it is helpful
        for returning a calendar date for the specific year
        """
        year = 2023

        expected_fixed_holidays_datetime = convert_fixed_holiday_to_datetime(
            EXPECTED_FIXED_DATE_HOLIDAYS, year
        )
        actual_fixed_date_holidays = get_fixed_date_holidays(year)

        assert actual_fixed_date_holidays == expected_fixed_holidays_datetime
