import pytest

from canada_holidays import get_holidays
from tests.fixtures import (
    ALBERTA_2023,
    ALBERTA_2030,
    BRITISH_COLUMBIA_2023,
    BRITISH_COLUMBIA_2030,
    MANITOBA_2023,
    MANITOBA_2030,
    NEW_BRUNSWICK_2023,
    NEW_BRUNSWICK_2030,
    NEWFOUNDLAND_AND_LABRADOR_2023,
    NEWFOUNDLAND_AND_LABRADOR_2030,
    NOVA_SCOTIA_2023,
    NOVA_SCOTIA_2030,
    NORTHWEST_TERRITORIES_2023,
    NORTHWEST_TERRITORIES_2030,
    NUNAVUT_2023,
    NUNAVUT_2030,
    ONTARIO_2023,
    ONTARIO_2030,
    PRINCE_EDWARD_ISLAND_2023,
    PRINCE_EDWARD_ISLAND_2030,
    QUEBEC_2023,
    QUEBEC_2030,
    SASKATCHEWAN_2023,
    SASKATCHEWAN_2030,
    YUKON_2023,
    YUKON_2030,
)
from tests.utils import compare_holidays_list


class TestCanadaProvincialHolidays:
    @pytest.mark.parametrize(
        "expected_holidays, province_name, year",
        [
            (ALBERTA_2023, "Alberta", 2023),
            (ALBERTA_2030, "Alberta", 2030),
            (BRITISH_COLUMBIA_2023, "British Columbia", 2023),
            (BRITISH_COLUMBIA_2030, "British Columbia", 2030),
            (MANITOBA_2023, "Manitoba", 2023),
            (MANITOBA_2030, "Manitoba", 2030),
            (NEW_BRUNSWICK_2023, "New Brunswick", 2023),
            (NEW_BRUNSWICK_2030, "New Brunswick", 2030),
            (NEWFOUNDLAND_AND_LABRADOR_2023, "Newfoundland and Labrador", 2023),
            (NEWFOUNDLAND_AND_LABRADOR_2030, "Newfoundland and Labrador", 2030),
            (NOVA_SCOTIA_2023, "Nova Scotia", 2023),
            (NOVA_SCOTIA_2030, "Nova Scotia", 2030),
            (NORTHWEST_TERRITORIES_2023, "Northwest Territories", 2023),
            (NORTHWEST_TERRITORIES_2030, "Northwest Territories", 2030),
            (NUNAVUT_2023, "Nunavut", 2023),
            (NUNAVUT_2030, "Nunavut", 2030),
            (ONTARIO_2023, "Ontario", 2023),
            (ONTARIO_2030, "Ontario", 2030),
            (PRINCE_EDWARD_ISLAND_2023, "Prince Edward Island", 2023),
            (PRINCE_EDWARD_ISLAND_2030, "Prince Edward Island", 2030),
            (QUEBEC_2023, "Quebec", 2023),
            (QUEBEC_2030, "Quebec", 2030),
            (SASKATCHEWAN_2023, "Saskatchewan", 2023),
            (SASKATCHEWAN_2030, "Saskatchewan", 2030),
            (YUKON_2023, "Yukon", 2023),
            (YUKON_2030, "Yukon", 2030),
        ],
    )
    def test_get_all_holidays_given_year_for_each_province_for_2023(
        self, expected_holidays, province_name, year
    ):
        year = year
        actual_holidays = get_holidays(province_name, year)
        diff = compare_holidays_list(expected_holidays, actual_holidays)

        assert diff == []
