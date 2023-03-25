import datetime

from holiday_info.on import ONTARIO
from holidays import get_holidays, get_province_holidays, is_holiday
from tests.fixtures.on import (
    ONTARIO_2023,
    ONTARIO_2023_APRIL,
)
from tests.utils import compare_holidays_list


class TestCanadaHolidays:
    def test_get_provincial_holidays_ontario(self):
        expected_holidays = ONTARIO
        actual_holidays = get_province_holidays("ontario")
        assert expected_holidays == actual_holidays

    def test_get_all_holidays_in_given_year_ontario(self):
        year = 2023
        expected_holidays = ONTARIO_2023

        actual_holidays = get_holidays("Ontario", year)
        diff = compare_holidays_list(expected_holidays, actual_holidays)

        assert diff == []

    def test_get_all_holidays_in_given_year_and_month_ontario(self):
        year = 2023
        month = 4
        expected_holidays = ONTARIO_2023_APRIL
        actual_holidays = get_holidays("Ontario", year, month)
        diff = compare_holidays_list(expected_holidays, actual_holidays)

        assert diff == []

    def test_is_holiday_returns_false_to_non_holiday(self):
        # September 9th 2023 is not a holiday in Ontario
        test_date = datetime.date(2023, 9, 9)
        assert is_holiday(test_date, "Ontario") is False

    def test_is_holiday_returns_true_to_valid_holiday(self):
        # May 22nd 2023 is Victoria Day in Ontario
        test_date = datetime.date(2023, 5, 22)
        assert is_holiday(test_date, "Ontario") is True
