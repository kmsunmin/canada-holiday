import datetime
import json
from typing import List

from main import get_striding_holidays


# ex: first Monday of the month
STRIDING_HOLIDAYS_ON = {
    2: [(3, "mon", "Family Day")],  # Family Day, 3rd Monday
    9: [(1, "mon", "Labour Day")],  # Labour Day, 1st Monday
    10: [(2, "mon", "Thanksgiving Day")],  # Thanksgiving Day, 2nd Monday
}


def load_test_fixture_data(file_path: str):
    with open(file_path, "r") as f:
        data = json.load(f)
    return data["results"]


class TestStridingHolidaysON:
    def test_all_striding_holidays_in_year_ontario(self):
        year = 2023
        province = "on"

        expected_data_raw = load_test_fixture_data("./fixtures/striding_holidays_2023.json")
        expected_striding_holidays = []
        for expected_hol in expected_data_raw:
            year, month, day, holiday_name = expected_hol
            str_hol_datetime = datetime.date(year, month, day)
            expected_striding_holidays.append((str_hol_datetime, holiday_name))

        actual_striding_holidays = get_striding_holidays(year, province)

        assert actual_striding_holidays == expected_striding_holidays
