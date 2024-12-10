from typing import List

from canada_holiday.holiday import CanadaHoliday


def compare_holidays(h1: CanadaHoliday, h2: CanadaHoliday):
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
        and h1.holiday_type == h2.holiday_type
    )


def compare_holidays_list(h1: List[CanadaHoliday], h2: List[CanadaHoliday]):
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
            h.nth_day,
            h.preceding_date,
            h.province,
            h.succeeding_date,
        )
        for h in h1
    )
    h2_set = set(
        (
            h.name,
            h.month,
            h.year,
            h.day,
            h.nth_day,
            h.preceding_date,
            h.province,
            h.succeeding_date,
        )
        for h in h2
    )
    diff = [
        h
        for h in h2
        if (
            h.name,
            h.month,
            h.year,
            h.day,
            h.nth_day,
            h.preceding_date,
            h.province,
            h.succeeding_date,
        )
        not in h1_set
    ]
    return diff
