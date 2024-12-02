import pytest

from canada_holiday.holidays import get_holidays
from tests.fixtures import (
    ALBERTA_2030,
    BRITISH_COLUMBIA_2030,
    MANITOBA_2030,
    NEW_BRUNSWICK_2030,
    NEWFOUNDLAND_AND_LABRADOR_2030,
    NOVA_SCOTIA_2030,
    NORTHWEST_TERRITORIES_2030,
    NUNAVUT_2030,
    ONTARIO_2030,
    PRINCE_EDWARD_ISLAND_2030,
    QUEBEC_2030,
    SASKATCHEWAN_2030,
    YUKON_2030,
)
from tests.utils import compare_holidays_list


class TestCanadaProvincialHolidays:
    @pytest.mark.parametrize(
        "expected_holidays, province_name, year",
        [
            (ALBERTA_2030, "Alberta", 2030),
            (BRITISH_COLUMBIA_2030, "British Columbia", 2030),
            (MANITOBA_2030, "Manitoba", 2030),
            (NEW_BRUNSWICK_2030, "New Brunswick", 2030),
            (NEWFOUNDLAND_AND_LABRADOR_2030, "Newfoundland and Labrador", 2030),
            (NOVA_SCOTIA_2030, "Nova Scotia", 2030),
            (NORTHWEST_TERRITORIES_2030, "Northwest Territories", 2030),
            (NUNAVUT_2030, "Nunavut", 2030),
            (ONTARIO_2030, "Ontario", 2030),
            (PRINCE_EDWARD_ISLAND_2030, "Prince Edward Island", 2030),
            (QUEBEC_2030, "Quebec", 2030),
            (SASKATCHEWAN_2030, "Saskatchewan", 2030),
            (YUKON_2030, "Yukon", 2030),
        ],
    )
    def test_get_all_holidays_given_year_for_each_province(
        self, expected_holidays, province_name, year
    ):
        year = year
        actual_holidays = get_holidays(province_name, year)
        diff = compare_holidays_list(expected_holidays, actual_holidays)

        assert diff == []
