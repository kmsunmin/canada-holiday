import pytest

from holidays import get_all_holidays
from tests.fixtures import (
    ALBERTA_2023,
    BRITISH_COLUMBIA_2023,
    MANITOBA_2023,
    NEW_BRUNSWICK_2023,
    NEWFOUNDLAND_AND_LABRADOR_2023,
    NOVA_SCOTIA_2023,
    NORTHWEST_TERRITORIES_2023,
    NUNAVUT_2023,
    ONTARIO_2023,
    PRINCE_EDWARD_ISLAND_2023,
    QUEBEC_2023,
    SASKATCHEWAN_2023,
    YUKON_2023,
)
from tests.utils.test_utils import compare_holidays_list


class TestCanadaProvincialHolidays:
    @pytest.mark.parametrize(
        "expected_holidays,province_name",
        [
            (ALBERTA_2023, "Alberta"),
            (BRITISH_COLUMBIA_2023, "British Columbia"),
            (MANITOBA_2023, "Manitoba"),
            (NEW_BRUNSWICK_2023, "New Brunswick"),
            (NEWFOUNDLAND_AND_LABRADOR_2023, "Newfoundland and Labrador"),
            (NOVA_SCOTIA_2023, "Nova Scotia"),
            (NORTHWEST_TERRITORIES_2023, "Northwest Territories"),
            (NUNAVUT_2023, "Nunavut"),
            (ONTARIO_2023, "Ontario"),
            (PRINCE_EDWARD_ISLAND_2023, "Prince Edward Island"),
            (QUEBEC_2023, "Quebec"),
            (SASKATCHEWAN_2023, "Saskatchewan"),
            (YUKON_2023, "Yukon"),
        ],
    )
    def test_get_all_holidays_given_year_for_each_province(
        self, expected_holidays, province_name
    ):
        year = 2023
        actual_holidays = get_all_holidays(province_name, year)
        diff = compare_holidays_list(expected_holidays, actual_holidays)

        assert diff == []
