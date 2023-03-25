import datetime

from holiday_instances import ONTARIO
from tests.fixtures.on import (
    ONTARIO_ONLY_HOLIDAYS_2023,
    ONTARIO_2023,
    UNSORTED_ONTARIO_2023,
    ONTARIO_2023_APRIL,
    CANADA_EASTER_DAY_2023,
)
from tests.utils.utils import compare_holidays_list
from utils import (
    check_province_name,
    update_list_of_holidays,
    sort_list_of_holidays,
    filter_list_of_holidays_by_month,
    find_easter_day,
    get_last_day_str_of_month,
)


class TestUtils:
    def test_check_province_name(self):
        assert check_province_name("ab") == "Alberta"
        assert check_province_name("bc") == "British Columbia"
        assert check_province_name("mb") == "Manitoba"
        assert check_province_name("nb") == "New Brunswick"
        assert check_province_name("nl") == "Newfoundland and Labrador"
        assert check_province_name("ns") == "Nova Scotia"
        assert check_province_name("nt") == "Northwest Territories"
        assert check_province_name("nu") == "Nunavut"
        assert check_province_name("on") == "Ontario"
        assert check_province_name("pe") == "Prince Edward Island"
        assert check_province_name("qc") == "Quebec"
        assert check_province_name("sk") == "Saskatchewan"
        assert check_province_name("yt") == "Yukon"

    def test_update_list_of_holidays_to_date_given_year(self):
        year = 2023
        expected_holidays_list_with_date = ONTARIO_ONLY_HOLIDAYS_2023

        ontario_holidays_without_date = ONTARIO
        actual_holidays_with_date = update_list_of_holidays(
            ontario_holidays_without_date, year
        )
        diff = compare_holidays_list(
            expected_holidays_list_with_date, actual_holidays_with_date
        )

        assert diff == []

    def test_sort_list_of_holidays_by_date(self):
        expected_sorted_holidays = ONTARIO_2023

        actual_sorted_holidays = sort_list_of_holidays(UNSORTED_ONTARIO_2023)
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

    def test_find_easter_day(self):
        year = 2023
        expected_easter_day = find_easter_day(year)
        assert expected_easter_day == CANADA_EASTER_DAY_2023

    def test_get_last_day_str_of_month(self):
        year = 2023
        month = 2
        actual_last_sunday_of_february = get_last_day_str_of_month(
            year, month, "sunday"
        )
        expected_last_sunday_of_february = datetime.date(2023, 2, 26)
        assert actual_last_sunday_of_february == expected_last_sunday_of_february
