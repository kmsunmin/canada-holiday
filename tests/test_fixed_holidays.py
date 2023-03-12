from holidays import get_fixed_date_holidays
from tests.test_utils import convert_fixture_data_to_holidays_list, load_test_fixture_data


class TestFixedDateHolidays:
    def test_all_fixed_date_holidays_are_returned(self):
        """
        For fixed date holidays, year may not matter much, but it is helpful
        for returning a calendar date for the specific year
        """
        year = 2023
        expected_data_raw: dict = load_test_fixture_data("fixtures/fixed_date_holidays.json")
        expected_fixed_holidays = convert_fixture_data_to_holidays_list(expected_data_raw)

        actual_fixed_date_holidays = get_fixed_date_holidays(year)

        assert actual_fixed_date_holidays == expected_fixed_holidays
