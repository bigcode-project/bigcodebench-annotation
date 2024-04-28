import pandas as pd
from datetime import datetime

# Constants
ROOMS = ["Room1", "Room2", "Room3", "Room4", "Room5"]

def f_325(date_str, booking_data):
    """
    This function generates a status report of room bookings for a specified date
    and displays a bar plot representing the booking statuses of various rooms.
    It validates the provided date, compiles a booking status report, and visualizes
    the data in a bar plot.

    Parameters:
    - date_str (str): The date for which the booking status needs to be checked,
                      in "yyyy-mm-dd" format. The function validates this date.
    - booking_data (dict): A dictionary with room names as keys and booking statuses
                           as values. The keys should match the rooms listed in the ROOMS constant.

    Returns:
    - DataFrame: A pandas DataFrame containing booking status for each room.
    - matplotlib.pyplot.Axes: A matplotlib Axes object for the bar plot of booking statuses.

    Raises:
    - ValueError: Raised in two scenarios:
                  1. If `date_str` does not follow the "yyyy-mm-dd" format or is not a valid date.
                  2. If `date_str` refers to a past date.

    Requirements:
    - pandas
    - datetime

    Example:
    >>> future_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    >>> booking_info = {"Room1": "Booked", "Room2": "Available"}
    >>> report_df, ax = f_325(future_date, booking_info)
    >>> print(report_df)
        Room Booking Status
    0  Room1         Booked
    1  Room2      Available
    2  Room3     Not Listed
    3  Room4     Not Listed
    4  Room5     Not Listed
    """
    # Validate the date string
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
        if date < datetime.now():
            raise ValueError("Date is in the past. Please provide a future date.")
    except ValueError as e:
        raise ValueError(f"Invalid date: {e}") from e

    report_data = [[room, booking_data.get(room, "Not Listed")] for room in ROOMS]
    report_df = pd.DataFrame(report_data, columns=["Room", "Booking Status"])

    # Create a bar plot of the booking statuses
    ax = (
        report_df["Booking Status"]
        .value_counts()
        .plot(kind="bar", title="Booking Statuses for " + date_str)
    )

    return report_df, ax

import unittest
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    """Test cases for f_325"""
    def test_future_date_valid_booking_data(self):
        """
        Test f_325 with a future date and valid booking data.
        """
        future_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
        booking_data = {"Room1": "Booked", "Room2": "Available"}
        report_df, _ = f_325(future_date, booking_data)
        self.assertIn("Room1", report_df["Room"].values)
        self.assertIn("Booked", report_df["Booking Status"].values)
    def test_past_date(self):
        """
        Test f_325 with a past date to ensure it raises a ValueError.
        """
        past_date = "2020-01-01"
        booking_data = {"Room1": "Booked"}
        with self.assertRaises(ValueError):
            f_325(past_date, booking_data)
    def test_invalid_date_format(self):
        """
        Test f_325 with an invalid date format to check for ValueError.
        """
        invalid_date = "15-06-2023"
        booking_data = {"Room1": "Booked"}
        with self.assertRaises(ValueError):
            f_325(invalid_date, booking_data)
    def test_booking_data_for_nonexistent_room(self):
        """
        Test f_325 with booking data for a room not in the ROOMS constant.
        """
        future_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
        booking_data = {"Room6": "Booked"}
        report_df, _ = f_325(future_date, booking_data)
        self.assertIn("Not Listed", report_df["Booking Status"].values)
    def test_no_booking_data(self):
        """
        Test f_325 with no booking data provided.
        """
        future_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
        booking_data = {}
        report_df, _ = f_325(future_date, booking_data)
        self.assertTrue((report_df["Booking Status"] == "Not Listed").all())
    def tearDown(self):
        plt.clf()
