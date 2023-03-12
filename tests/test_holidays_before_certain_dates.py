from holidays import get_holidays_before_certain_dates
from tests.test_utils import convert_fixture_data_to_holidays_list, load_test_fixture_data


HOLIDAYS_BEFORE_CERTAIN_DATES_ON = {
    4: [
        ("fri", "Easter Sunday", "Good Friday")
    ],  # Good Friday (Friday before Easter Sunday)
    5: [("mon", 25, "Victoria Day")],  # Victoria Day (Monday before May 25th)
}


class TestHolidaysBeforeACertainDate:
    def test_get_all_holidays_before_certain_dates(self):
        year = 2023
        province = "on"
        expected_data_raw: dict = load_test_fixture_data(
            "fixtures/holidays_before_certain_dates.json"
        )
        expected_preceding_holidays = convert_fixture_data_to_holidays_list(expected_data_raw, province)

        actual_preceding_holidays = get_holidays_before_certain_dates(year, province)

        assert actual_preceding_holidays == expected_preceding_holidays
