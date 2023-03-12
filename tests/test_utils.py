import datetime
import json


def load_test_fixture_data(file_path: str):
    with open(file_path, "r") as f:
        data = json.load(f)
    return data["results"]


def convert_fixture_data_to_holidays_list(fixture: dict, province: str = None) -> list:
    holidays = []
    fixture_data = fixture[province] if province is not None else fixture
    for expected_hol in fixture_data:
        year, month, day, holiday_name = expected_hol
        hol_datetime = datetime.date(year, month, day)
        holidays.append((hol_datetime, holiday_name))
    return holidays
