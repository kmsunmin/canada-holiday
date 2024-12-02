import pytest

from canada_holiday.holiday import CanadaHoliday, HolidayType
from canada_holiday.holidays import convert_holiday_info_to_obj


class TestClassHoliday:
    def test_validate_holiday_condition_nth_day(self):
        nth_day_holiday_info = {
            "name": "Thanksgiving Day",
            "month": 10,
            "year": 2024,
            "nth_day": ("mon", 2),
            "province": "Quebec",
            "holiday_type": HolidayType.NTH_DAY,
        }
        holiday = convert_holiday_info_to_obj(nth_day_holiday_info)
        assert isinstance(holiday, CanadaHoliday) is True

    def test_validate_holiday_condition_nth_day_raise_exception(self):
        invalid_nth_day_holiday_info = {
            "name": "Thanksgiving Day",
            "month": 10,
            "year": 2024,
            "nth_day": ("mon", 2),
            "preceding_date": ("mon", 25),
            "province": "Quebec",
            "holiday_type": HolidayType.NTH_DAY,
        }
        expected_exc_str = "Invalid values for the Holiday."

        with pytest.raises(Exception) as excinfo:
            convert_holiday_info_to_obj(invalid_nth_day_holiday_info)

        assert expected_exc_str in str(excinfo.value)

    def test_validate_holiday_condition_nearest_day(self):
        nearest_day_holiday_info = {
            "name": "St. George's Day",
            "month": 4,
            "year": 2024,
            "nearest_day": ("mon", 23),
            "province": "Newfoundland and Labrador",
            "holiday_type": HolidayType.NEAREST_DAY,
        }
        holiday = convert_holiday_info_to_obj(nearest_day_holiday_info)
        assert isinstance(holiday, CanadaHoliday) is True

    def test_validate_holiday_condition_nearest_day_raise_exception(self):
        invalid_nearest_day_holiday_info = {
            "name": "St. George's Day",
            "month": 4,
            "year": 2024,
            "nearest_day": ("mon", 23),
            "preceding_date": ("fri", 30),
            "province": "Newfoundland and Labrador",
            "holiday_type": HolidayType.PRECEDING_DATE,
        }
        expected_exc_str = "Invalid values for the Holiday."

        with pytest.raises(Exception) as excinfo:
            convert_holiday_info_to_obj(invalid_nearest_day_holiday_info)

        assert expected_exc_str in str(excinfo.value)

    def test_validate_holiday_condition_preceding_date(self):
        preceding_date_holiday_info = {
            "name": "Victoria Day",
            "month": 5,
            "year": 2024,
            "preceding_date": ("mon", 25),
            "province": "Ontario",
            "holiday_type": HolidayType.PRECEDING_DATE,
        }
        holiday = convert_holiday_info_to_obj(preceding_date_holiday_info)
        assert isinstance(holiday, CanadaHoliday) is True

    def test_validate_holiday_condition_preceding_date_raise_exception(self):
        invalid_preceding_date_holiday_info = {
            "name": "Victoria Day",
            "month": 5,
            "year": 2024,
            "preceding_date": ("mon", 25),
            "succeeding_date": ("wed", 12),
            "province": "Ontario",
            "holiday_type": HolidayType.PRECEDING_DATE,
        }
        expected_exc_str = "Invalid values for the Holiday."

        with pytest.raises(Exception) as excinfo:
            convert_holiday_info_to_obj(invalid_preceding_date_holiday_info)

        assert expected_exc_str in str(excinfo.value)

    def test_validate_holiday_condition_succeeding_date(self):
        succeeding_date_holiday_info = {
            "name": "Easter Monday",
            "month": 4,
            "year": 2024,
            "succeeding_date": ("mon", "Easter Sunday"),
            "province": "Quebec",
            "holiday_type": HolidayType.SUCCEEDING_DATE,
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
            "holiday_type": HolidayType.NEAREST_DAY,
        }
        expected_exc_str = "Invalid values for the Holiday."

        with pytest.raises(Exception) as excinfo:
            convert_holiday_info_to_obj(invalid_succeeding_date_holiday_info)

        assert expected_exc_str in str(excinfo.value)
