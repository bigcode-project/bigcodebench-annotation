from datetime import datetime
import pytz
import re
from faker import Faker


def f_310(epoch_milliseconds, seed=0, timezones=["UTC"]):
    """Create a dictionary with a fake event schedule given an event time.

    The function converts a given epoch in milliseconds into a datetime object in
    the current system time's timezone. It generates a fake event name using Faker. 
    Then, it uses pytz and regex to check if specified timezones are valid (i.e. 
    in pytz.all_timezones or can be parsed using regex from UTC±HH:MM format), ignoring 
    invalid ones. If none is valid or if timezones were not specified, it selects UTC; 
    otherwise, it randomly selects a valid one using Faker. Finally, the function returns a 
    dictionary with the fake event name as key and a list as value, where the list itself 
    contains a schedule, i.e. a dictionary with keys 'date', 'time', 'timezone'.

    Parameters:
    - epoch_milliseconds (int): Epoch time in milliseconds. If negative, defaults to 0.
    - seed (int, optional): Random seed for Faker's RNG. Defaults to None.
    - timezones (list, optional): A list of timezones to select from.
                                  If none is valid or if not specified, defaults to ['UTC'].

    Returns:
    - A dictionary containing event names as keys and a list of event details as values.
      Event details include the date, time, and timezone of the event.

    Requirements:
    - datetime.datetime
    - faker
    - pytz
    - re

    Example:
    >>> f_310(1236472051807, seed=42)
    {'Danielle': [{'date': datetime.date(2009, 3, 8), 'time': datetime.time(11, 27, 31, 807000), 'timezone': 'UTC'}]}
    >>> f_310(1609459200000, seed=24, timezones=['UTC', 'UTC+01:00'])
    {'Jennifer': [{'date': datetime.date(2021, 1, 1), 'time': datetime.time(11, 0), 'timezone': 'UTC'}]}
    """
    Faker.seed(seed)

    faker_instance = Faker()

    event_datetime = datetime.fromtimestamp(epoch_milliseconds / 1000.0)

    event_name = faker_instance.unique.first_name()

    validated_timezones = []
    utc_offset_regex = r"^UTC([+-])(0[0-9]|1[0-4]):([0-5][0-9])$"
    for tz in timezones:
        if (
            (tz == "UTC")
            or (re.match(utc_offset_regex, tz))
            or (tz in pytz.all_timezones)
        ):
            validated_timezones.append(tz)
    if not validated_timezones:
        validated_timezones = ["UTC"]

    timezone = faker_instance.random_element(elements=(validated_timezones))

    event_schedule = {
        event_name: [
            {
                "date": event_datetime.date(),
                "time": event_datetime.time(),
                "timezone": timezone,
            }
        ]
    }

    return event_schedule

import unittest
from datetime import datetime
class TestCases(unittest.TestCase):
    TIMEZONES = ["UTC", "UTC+01:00", "UTC+02:00", "UTC+03:00", "UTC+04:00", "UTC+05:00"]
    default_time = 1236472051807
    def check_structure_and_content(self, schedule, epoch_milliseconds):
        event_name = list(schedule.keys())[0]
        event_details = schedule[event_name]
        event_datetime = datetime.fromtimestamp(epoch_milliseconds / 1000.0)
        self.assertIsInstance(schedule, dict)
        self.assertEqual(len(schedule), 1)
        self.assertEqual(len(event_details), 1)
        self.assertEqual(event_details[0]["date"], event_datetime.date())
        self.assertEqual(event_details[0]["time"], event_datetime.time())
        self.assertIn(
            event_details[0]["timezone"], self.TIMEZONES
        )  # expected in these tests
    def test_case_1(self):
        # Test defaults
        epoch_milliseconds = self.default_time
        schedule = f_310(epoch_milliseconds)
        self.check_structure_and_content(schedule, epoch_milliseconds)
        self.assertTrue(schedule[list(schedule.keys())[0]][0]["timezone"] == "UTC")
    def test_case_2(self):
        # Test with a specific known epoch
        epoch_milliseconds = self.default_time
        schedule = f_310(epoch_milliseconds, seed=2, timezones=self.TIMEZONES)
        self.check_structure_and_content(schedule, epoch_milliseconds)
    def test_case_3(self):
        # Test with an invalid timezone list - should default to UTC
        schedule = f_310(self.default_time, seed=3, timezones=["INVALID"])
        self.assertTrue(schedule[list(schedule.keys())[0]][0]["timezone"] == "UTC")
        schedule = f_310(self.default_time, seed=3, timezones=["FOO", "BAR"])
        self.assertTrue(schedule[list(schedule.keys())[0]][0]["timezone"] == "UTC")
        for valid_tz in self.TIMEZONES:
            schedule = f_310(self.default_time, seed=3, timezones=["INVALID", valid_tz])
            self.assertTrue(
                schedule[list(schedule.keys())[0]][0]["timezone"] == valid_tz,
                f'Expected {valid_tz}, got {schedule[list(schedule.keys())[0]][0]["timezone"]}',
            )
    def test_case_4(self):
        # Test random seed reproducibility
        schedule1 = f_310(self.default_time, seed=42, timezones=self.TIMEZONES)
        schedule2 = f_310(self.default_time, seed=42, timezones=self.TIMEZONES)
        self.assertEqual(schedule1, schedule2)
    def test_case_6(self):
        # Test handling invalid dates - invalid types
        for invalid in ["1", [], None]:
            with self.assertRaises(TypeError):
                f_310(invalid)
    def test_case_7(self):
        # Test handling extremely future dates
        epoch_milliseconds = (
            4133980800000  # This is a date far in the future (2100-12-31)
        )
        schedule = f_310(epoch_milliseconds, seed=5, timezones=["UTC", "UTC+05:00"])
        self.check_structure_and_content(schedule, epoch_milliseconds)
        # No additional asserts required, check_structure_and_content will validate
    def test_case_8(self):
        # Test handling leap year date
        epoch_milliseconds = 1582934400000  # This corresponds to 2020-02-29
        schedule = f_310(
            epoch_milliseconds, seed=6, timezones=["UTC", "UTC+01:00", "UTC+02:00"]
        )
        self.check_structure_and_content(schedule, epoch_milliseconds)
        # Validate it handles the leap day correctly
        event_date = schedule[list(schedule.keys())[0]][0]["date"]
        self.assertTrue(event_date.year == 2020)
        self.assertTrue(event_date.month == 2)
        self.assertTrue(event_date.day == 29)
