import pytest

from canada_holiday.holiday_class import CanadaHoliday
from canada_holiday.holidays import convert_holiday_info_to_obj


class TestClassHoliday:
    def test_validate_holiday_condition_nth_day(self):
        nth_day_holiday_info = {
            "name": "Thanksgiving Day",
            "month": 10,
            "nth_day": ("mon", 2),
            "province": "Quebec",
        }
        holiday = convert_holiday_info_to_obj(nth_day_holiday_info)
        assert isinstance(holiday, CanadaHoliday) is True

    def test_validate_holiday_condition_nth_day_raise_exception(self):
        invalid_nth_day_holiday_info = {
            "name": "Thanksgiving Day",
            "month": 10,
            "nth_day": ("mon", 2),
            "preceding_date": ("mon", 25),
            "province": "Quebec",
        }
        expected_exc_str = f"Cannot validate the Holiday. Please check the Holiday: {invalid_nth_day_holiday_info['name']}."

        with pytest.raises(Exception) as excinfo:
            convert_holiday_info_to_obj(invalid_nth_day_holiday_info)

        assert expected_exc_str in str(excinfo.value)

    def test_validate_holiday_condition_nearest_day(self):
        nearest_day_holiday_info = {
            "name": "St. George's Day",
            "month": 4,
            "nearest_day": ("mon", 23),
            "province": "Newfoundland and Labrador",
        }
        holiday = convert_holiday_info_to_obj(nearest_day_holiday_info)
        assert isinstance(holiday, CanadaHoliday) is True

    def test_validate_holiday_condition_nearest_day_raise_exception(self):
        invalid_nearest_day_holiday_info = {
            "name": "St. George's Day",
            "month": 4,
            "nearest_day": ("mon", 23),
            "preceding_date": ("fri", 30),
            "province": "Newfoundland and Labrador",
        }
        expected_exc_str = f"Cannot validate the Holiday. Please check the Holiday: {invalid_nearest_day_holiday_info['name']}."

        with pytest.raises(Exception) as excinfo:
            convert_holiday_info_to_obj(invalid_nearest_day_holiday_info)

        assert expected_exc_str in str(excinfo.value)

    def test_validate_holiday_condition_preceding_date(self):
        preceding_date_holiday_info = {
            "name": "Victoria Day",
            "month": 5,
            "preceding_date": ("mon", 25),
            "province": "Ontario",
        }
        holiday = convert_holiday_info_to_obj(preceding_date_holiday_info)
        assert isinstance(holiday, CanadaHoliday) is True

    def test_validate_holiday_condition_preceding_date_raise_exception(self):
        invalid_preceding_date_holiday_info = {
            "name": "Victoria Day",
            "month": 5,
            "preceding_date": ("mon", 25),
            "succeeding_date": ("wed", 12),
            "province": "Ontario",
        }
        expected_exc_str = f"Cannot validate the Holiday. Please check the Holiday: {invalid_preceding_date_holiday_info['name']}."

        with pytest.raises(Exception) as excinfo:
            convert_holiday_info_to_obj(invalid_preceding_date_holiday_info)

        assert expected_exc_str in str(excinfo.value)

    def test_validate_holiday_condition_succeeding_date(self):
        succeeding_date_holiday_info = {
            "name": "Easter Monday",
            "month": 4,
            "succeeding_date": ("mon", "Easter Sunday"),
            "province": "Quebec",
        }
        holiday = convert_holiday_info_to_obj(succeeding_date_holiday_info)
        assert isinstance(holiday, CanadaHoliday) is True

    def test_validate_holiday_condition_succeeding_date_raise_exception(self):
        invalid_succeeding_date_holiday_info = {
            "name": "Easter Monday",
            "month": 4,
            "nearest_day": ("thu", 10),
            "succeeding_date": ("mon", "Easter Sunday"),
            "province": "Quebec",
        }
        expected_exc_str = f"Cannot validate the Holiday. Please check the Holiday: {invalid_succeeding_date_holiday_info['name']}."

        with pytest.raises(Exception) as excinfo:
            convert_holiday_info_to_obj(invalid_succeeding_date_holiday_info)

        assert expected_exc_str in str(excinfo.value)
