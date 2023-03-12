from holidays import get_nth_day_of_month_holidays
from tests.test_utils import convert_fixture_data_to_holidays_list, load_test_fixture_data

STRIDING_HOLIDAYS_ON = {
    2: [(3, "mon", "Family Day")],  # Family Day, 3rd Monday
    9: [(1, "mon", "Labour Day")],  # Labour Day, 1st Monday
    10: [(2, "mon", "Thanksgiving Day")],  # Thanksgiving Day, 2nd Monday
}


class TestNthDayOfMonthHolidays:
    # TODO: Test with other years as well
    def test_get_all_nth_day_of_month_holidays_in_year_ontario(self):
        year = 2023
        province = "on"
        expected_data_raw: dict = load_test_fixture_data(
            "fixtures/nth_day_of_month_holidays.json"
        )
        expected_striding_holidays = convert_fixture_data_to_holidays_list(expected_data_raw, province)

        actual_striding_holidays = get_nth_day_of_month_holidays(year, province)

        assert actual_striding_holidays == expected_striding_holidays
