import datetime
import json
from typing import List

from holiday import Holiday


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


def compare_holidays(h1: Holiday, h2: Holiday):
    """
    Check if the two given holidays are the same by checking their
    attributes.
    """
    return (
        h1.name == h2.name
        and h1.month == h2.month
        and h1.year == h2.year
        and h1.day == h2.day
        and h1.date == h2.date
        and h1.nth_day == h2.nth_day
        and h1.preceding_date == h2.preceding_date
        and h1.province == h2.province
        and h1.succeeding_date == h2.succeeding_date
    )


def compare_holidays_list(h1: List[Holiday], h2: List[Holiday]):
    """
    set1 = set((x.id,x.name,...) for x in list1)
    difference = [ x for x in list2 if (x.id,x.name,...) not in set1 ]
    """
    h1_set = set(
        (
            h.name,
            h.month,
            h.year,
            h.day,
            h.date,
            h.nth_day,
            h.preceding_date,
            h.province,
            h.succeeding_date,
        )
        for h in h1
    )
    diff = [
        h
        for h in h2
        if (
            h.name,
            h.month,
            h.year,
            h.day,
            h.date,
            h.nth_day,
            h.preceding_date,
            h.province,
            h.succeeding_date,
        )
        not in h1_set
    ]
    return diff
