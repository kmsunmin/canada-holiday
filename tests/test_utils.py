import datetime

from canada_holiday.holidays import convert_holiday_info_to_obj
from canada_holiday.holiday_class import (
    CanadaHoliday,
    parse_preceding_day_str,
)
from canada_holiday.utils import (
    check_province_name,
    update_list_of_holidays,
    sort_list_of_holidays,
    filter_list_of_holidays_by_month,
    find_easter_day,
    get_day_of_the_week_idx,
    get_last_day_str_of_month,
)
from tests.fixtures.on import (
    ONTARIO_2023,
    ONTARIO_2023_APRIL,
)
from tests.utils import compare_holidays, compare_holidays_list


class TestUtils:
    def test_check_province_name(self):
        assert check_province_name("ab") == "Alberta"
        assert check_province_name("bc") == "British Columbia"
        assert check_province_name("mb") == "Manitoba"
        assert check_province_name("nb") == "New Brunswick"
        assert check_province_name("nl") == "Newfoundland and Labrador"
        assert check_province_name("ns") == "Nova Scotia"
        assert check_province_name("nt") == "Northwest Territories"
        assert check_province_name("nu") == "Nunavut"
        assert check_province_name("on") == "Ontario"
        assert check_province_name("pe") == "Prince Edward Island"
        assert check_province_name("qc") == "Quebec"
        assert check_province_name("sk") == "Saskatchewan"
        assert check_province_name("yt") == "Yukon"

    def test_update_list_of_holidays_to_date_given_year(self):
        year = 2023
        expected_holiday_obj_list_with_date = [
            CanadaHoliday(
                "Labour Day",
                month=9,
                year=2023,
                day=4,
                date=datetime.date(2023, 9, 4),
                nth_day=("mon", 1),  # 1st Monday in September
                province="all",
            )
        ]
        holiday_obj_list_without_date = [
            CanadaHoliday(
                "Labour Day",
                month=9,
                year=2023,
                nth_day=("mon", 1),  # 1st Monday in September
                province="all",
            )
        ]

        actual_holidays_with_date = update_list_of_holidays(
            holiday_obj_list_without_date, year
        )
        diff = compare_holidays_list(
            expected_holiday_obj_list_with_date, actual_holidays_with_date
        )

        assert diff == []

    def test_sort_list_of_holidays_by_date(self):
        expected_sorted_holiday_objs = [
            CanadaHoliday(
                "Family Day",
                month=2,
                year=2023,
                day=20,
                date=datetime.date(2023, 2, 20),
                nth_day=("mon", 3),
                province="Ontario",
            ),
            CanadaHoliday(
                "Victoria Day",
                month=5,
                year=2023,
                day=22,
                date=datetime.date(2023, 5, 22),
                preceding_date=("mon", 25),
                province="Ontario",
            ),
            CanadaHoliday(
                "Labour Day",
                month=9,
                year=2023,
                day=4,
                date=datetime.date(2023, 9, 4),
                nth_day=("mon", 1),
                province="all",
            ),
        ]
        unsorted_holiday_objs = [
            CanadaHoliday(
                "Labour Day",
                month=9,
                year=2023,
                day=4,
                date=datetime.date(2023, 9, 4),
                nth_day=("mon", 1),
                province="all",
            ),
            CanadaHoliday(
                "Family Day",
                month=2,
                year=2023,
                day=20,
                date=datetime.date(2023, 2, 20),
                nth_day=("mon", 3),
                province="Ontario",
            ),
            CanadaHoliday(
                "Victoria Day",
                month=5,
                year=2023,
                day=22,
                date=datetime.date(2023, 5, 22),
                preceding_date=("mon", 25),
                province="Ontario",
            ),
        ]

        actual_sorted_holidays = sort_list_of_holidays(unsorted_holiday_objs)
        diff = compare_holidays_list(
            expected_sorted_holiday_objs, actual_sorted_holidays
        )

        assert diff == []

    def test_filter_list_holidays_by_month(self):
        month = 4
        all_ontario_holidays = ONTARIO_2023
        expected_holidays_list_in_month = ONTARIO_2023_APRIL

        actual_holidays_in_month = filter_list_of_holidays_by_month(
            all_ontario_holidays, month
        )
        diff = compare_holidays_list(
            expected_holidays_list_in_month, actual_holidays_in_month
        )

        assert diff == []

    def test_find_easter_day(self):
        year = 2023
        expected_easter_day = datetime.date(2023, 4, 9)
        actual_easter_day = find_easter_day(year)
        assert actual_easter_day == expected_easter_day

    def test_get_last_day_str_of_month(self):
        year = 2023
        month = 2
        actual_last_sunday_of_february = get_last_day_str_of_month(
            year, month, "sunday"
        )
        expected_last_sunday_of_february = datetime.date(2023, 2, 26)
        assert actual_last_sunday_of_february == expected_last_sunday_of_february

    def test_convert_holiday_info_to_obj(self):
        expected_holiday_obj = CanadaHoliday(
            "New Year's Day",
            month=1,
            year=2023,
            day=1,
            date=datetime.date(2023, 1, 1),
            province="all",
        )
        actual_holiday_info = {
            "name": "New Year's Day",
            "month": 1,
            "year": 2023,
            "day": 1,
            "date": datetime.date(2023, 1, 1),
            "province": "all",
        }
        actual_holiday_obj = convert_holiday_info_to_obj(actual_holiday_info)
        result = compare_holidays(actual_holiday_obj, expected_holiday_obj)
        assert result is True

    def test_parse_preceding_day_str(self):
        preceding_day_str = "Last Sunday"
        expected_preceding_str_list = ["Last", "Sunday"]
        actual_preceding_str_list = parse_preceding_day_str(preceding_day_str)
        assert actual_preceding_str_list == expected_preceding_str_list

    def test_get_day_of_the_week_idx_with(self):
        # Condition that has 2nd Monday in October (Thanksgiving Day)
        day_condition = ("mon", 2)
        day_of_the_week_idx, condition = get_day_of_the_week_idx(day_condition)
        assert day_of_the_week_idx == 0
        assert condition == 2

    def test_get_day_of_the_week_idx_with_good_friday(self):
        # Condition that has preceding_day (Good Friday)
        day_condition = ("fri", "Easter Sunday")
        day_of_the_week_idx, condition = get_day_of_the_week_idx(day_condition)
        assert day_of_the_week_idx == 4
        assert condition == "Easter Sunday"
