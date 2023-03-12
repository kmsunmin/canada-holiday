import datetime

from holidays import get_nth_day_of_month_holidays
from tests.test_utils import load_test_fixture_data

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

        expected_data_raw = load_test_fixture_data("fixtures/nth_day_of_month_holidays.json")
        expected_striding_holidays = []
        for expected_hol in expected_data_raw[province]:
            year, month, day, holiday_name = expected_hol
            hol_datetime = datetime.date(year, month, day)
            expected_striding_holidays.append((hol_datetime, holiday_name))

        actual_striding_holidays = get_nth_day_of_month_holidays(year, province)

        assert actual_striding_holidays == expected_striding_holidays
