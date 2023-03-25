import datetime

from constants import ONTARIO
from holidays import get_all_holidays, get_province_holidays, is_holiday
from utils import (
    find_easter_day,
    update_list_of_holidays_to_date,
    sort_list_of_holidays_by_date,
    filter_list_of_holidays_by_month,
)
from tests.fixtures.on import (
    CANADA_EASTER_DAY_2023,
    ONTARIO_2023,
    ONTARIO_2023_APRIL,
    UNSORTED_ONTARIO_2023,
    ONTARIO_ONLY_HOLIDAYS_2023,
)
from tests.utils.utils import compare_holidays_list


class TestCanadaHolidays:
    def test_get_provincial_holidays_ontario(self):
        expected_holidays = ONTARIO
        actual_holidays = get_province_holidays("ontario")
        assert expected_holidays == actual_holidays

    def test_update_list_of_holidays_to_date_given_year(self):
        year = 2023
        expected_holidays_list_with_date = ONTARIO_ONLY_HOLIDAYS_2023

        ontario_holidays_without_date = ONTARIO
        actual_holidays_with_date = update_list_of_holidays_to_date(
            ontario_holidays_without_date, year
        )
        diff = compare_holidays_list(
            expected_holidays_list_with_date, actual_holidays_with_date
        )

        assert diff == []

    def test_sort_list_of_holidays_by_date(self):
        expected_sorted_holidays = ONTARIO_2023

        actual_sorted_holidays = sort_list_of_holidays_by_date(UNSORTED_ONTARIO_2023)
        diff = compare_holidays_list(expected_sorted_holidays, actual_sorted_holidays)

        assert diff == []

    def test_filter_list_holidays_by_month(self):
        month = 4
        all_ontario_holidays = ONTARIO_2023
        expected_holidays_list_in_month = ONTARIO_2023_APRIL

        actual_holidays_in_month = filter_list_of_holidays_by_month(
            all_ontario_holidays, month
        )
        diff = compare_holidays_list(
            expected_holidays_list_in_month, actual_holidays_in_month
        )

        assert diff == []

    def test_get_all_holidays_in_given_year_ontario(self):
        year = 2023
        expected_holidays = ONTARIO_2023

        actual_holidays = get_all_holidays("Ontario", year)
        diff = compare_holidays_list(expected_holidays, actual_holidays)

        assert diff == []

    def test_get_all_holidays_in_given_year_and_month_ontario(self):
        year = 2023
        month = 4
        expected_holidays = ONTARIO_2023_APRIL
        actual_holidays = get_all_holidays("Ontario", year, month)
        diff = compare_holidays_list(expected_holidays, actual_holidays)

        assert diff == []

    def test_find_easter_day(self):
        year = 2023
        expected_easter_day = find_easter_day(year)
        assert expected_easter_day == CANADA_EASTER_DAY_2023

    def test_is_holiday_returns_false_to_non_holiday(self):
        # September 9th 2023 is not a holiday in Ontario
        test_date = datetime.date(2023, 9, 9)
        assert (
            is_holiday(test_date.year, test_date.month, test_date.day, "Ontario")
            is False
        )

    def test_is_holiday_returns_true_to_valid_holiday(self):
        # May 22nd 2023 is Victoria Day in Ontario
        test_date = datetime.date(2023, 5, 22)
        assert (
            is_holiday(test_date.year, test_date.month, test_date.day, "Ontario")
            is True
        )
