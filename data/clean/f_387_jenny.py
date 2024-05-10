import pandas as pd
from datetime import datetime, timedelta
import random


def f_387(epoch_milliseconds, seed=0):
    """
    Generate user activity logs from a given epoch time to the current time.

    This function iterates from the starting epoch time to the current system
    time, incrementally increasing the time by a random number of seconds (an
    integer in [1, 10]) between each log entry. Each log entry records a user
    performing an activity at a specific time.

    Parameters:
    - epoch_milliseconds (int): Starting epoch time in milliseconds. Must be in
                                the past compared to current system time.
    - seed (int): random seed for reproducibility. Defaults to 0.

    Returns:
    - pd.DataFrame: A DataFrame containing logs of user activities, with columns:
        - 'User':   User names, randomly chosen from a predefined list of users,
                    ['user1', 'user2', 'user3', 'user4', 'user5'].
        - 'Activity': Activities performed by the users, randomly chosen from a
                      predefined list of activities, ['login', 'logout', 'browse',
                      'search', 'purchase'].
        - 'Time': The timestamp of when the activity occurred, incrementally
                  increasing from the starting epoch time to the current time.

    Raises:
    - ValueError: If the start time is after the current system time.
    
    Requirements:
    - pandas
    - datetime.datetime.fromtimestamp
    - datetime.timedelta
    - random

    Example:
    >>> log = f_387(1615168051807)
    >>> type(log)
    <class 'pandas.core.frame.DataFrame'>
    >>> log.iloc[0]
    User                             user4
    Activity                        search
    Time        2021-03-08 12:47:31.807000
    Name: 0, dtype: object
    """
    random.seed(seed)

    USERS = ["user1", "user2", "user3", "user4", "user5"]
    ACTIVITIES = ["login", "logout", "browse", "search", "purchase"]

    start_time = datetime.fromtimestamp(epoch_milliseconds / 1000.0)
    end_time = datetime.now()
    if start_time >= end_time:
        raise ValueError("Start time must be before current system time")

    logs = []
    current_time = start_time
    while current_time <= end_time:
        user = random.choice(USERS)
        activity = random.choice(ACTIVITIES)
        logs.append([user, activity, current_time])
        current_time += timedelta(seconds=random.randint(1, 10))
    log_df = pd.DataFrame(logs, columns=["User", "Activity", "Time"])
    return log_df


import unittest
import pandas as pd
from datetime import datetime, timedelta


class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test basic functionality - 1 day ago
        epoch_milliseconds = int(
            (datetime.now() - timedelta(days=1)).timestamp() * 1000
        )
        log = f_387(epoch_milliseconds)
        self.assertTrue(isinstance(log, pd.DataFrame))
        self.assertTrue("User" in log.columns)
        self.assertTrue("Activity" in log.columns)
        self.assertTrue("Time" in log.columns)
        start_time = datetime.fromtimestamp(epoch_milliseconds / 1000.0)
        self.assertEqual(log.iloc[0]["Time"], start_time)

    def test_case_2(self):
        # Test with a short time frame - 1 minutes ago
        epoch_milliseconds = int(
            (datetime.now() - timedelta(minutes=1)).timestamp() * 1000
        )
        log = f_387(epoch_milliseconds)
        self.assertTrue(len(log) > 0)  # Should have at least one entry
        self.assertTrue(
            log["Time"].min() >= datetime.fromtimestamp(epoch_milliseconds / 1000.0)
        )

    def test_case_3(self):
        # Test with a specific seed
        epoch_milliseconds = int(
            (datetime.now() - timedelta(days=1)).timestamp() * 1000
        )
        seed = 42
        log = f_387(epoch_milliseconds, seed=seed)
        first_row = log.iloc[0]
        expected_user = "user1"
        expected_activity = "login"
        self.assertEqual(first_row["User"], expected_user)
        self.assertEqual(first_row["Activity"], expected_activity)

    def test_case_4(self):
        # Test functionality over a longer period - 1 month ago
        epoch_milliseconds = int(
            (datetime.now() - timedelta(days=30)).timestamp() * 1000
        )
        log = f_387(epoch_milliseconds)

        # Ensure that log timestamps are properly incrementing
        time_diffs = log["Time"].diff().dropna()
        self.assertTrue(all(time_diffs > timedelta(seconds=0)))

        seconds_in_a_month = (
            30 * 24 * 60 * 60
        )  # Approximate number of seconds in a month
        max_possible_entries = (
            seconds_in_a_month  # Assuming a minimum of 1-second increments
        )
        min_possible_entries = (
            seconds_in_a_month // 10
        )  # Assuming a maximum of 10-second increments
        # Verify that the log has a reasonable number of entries given the time frame
        self.assertTrue(min_possible_entries <= len(log) <= max_possible_entries)

        self.assertTrue(
            log["Time"].min() >= datetime.fromtimestamp(epoch_milliseconds / 1000.0)
        )
        self.assertTrue(log["Time"].max() <= datetime.now())

    def test_case_5(self):
        # Test invalid start time (future)
        epoch_milliseconds = int(
            (datetime.now() + timedelta(days=1)).timestamp() * 1000
        )
        with self.assertRaises(Exception):
            f_387(epoch_milliseconds)


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()
