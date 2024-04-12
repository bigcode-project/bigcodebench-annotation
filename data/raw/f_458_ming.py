import unittest
from unittest.mock import patch
from datetime import datetime
import time
from random import randint
import matplotlib.pyplot as plt


def f_458(duration):
    """
    Generate and draw random data in real time for the specified duration.

    Parameters:
    - duration (int): The duration in seconds for which data is to be generated and plotted.

    Returns:
    - tuple: A tuple containing two lists.
        - The first list contains timestamps (as strings) in the format '%H:%M:%S.%f'.
        - The second list contains the generated random values.

    Requirements:
    - datetime: Used for generating timestamp strings for each data point.
    - time: Used to manage the duration for which data is generated.
    - random: Required for generating random values within a specified range.
    - matplotlib.pyplot: Necessary for plotting the generated data points.
    """
    # Constants
    VALUES_RANGE = (0, 100)
    PLOT_INTERVAL = 0.1

    plt.ion()
    x_data = []
    y_data = []

    end_time = time.time() + duration
    while time.time() < end_time:
        x_data.append(datetime.now().strftime('%H:%M:%S.%f'))
        y_data.append(randint(*VALUES_RANGE))

        plt.clf()
        plt.plot(x_data, y_data)
        plt.draw()
        plt.pause(PLOT_INTERVAL)

    plt.ioff()
    plt.show()

    return x_data, y_data


### Unit Tests

class TestF458(unittest.TestCase):
    @patch('matplotlib.pyplot.pause', return_value=None)
    def test_data_list_lengths_match(self, mock_pause):
        """
        Test that the lengths of timestamp and data lists match.
        """
        x_data, y_data = f_458(1)
        self.assertEqual(len(x_data), len(y_data))

    @patch('matplotlib.pyplot.pause', return_value=None)
    def test_function_runs_without_error(self, mock_pause):
        """
        Test that the function runs without error.
        """
        try:
            f_458(1)
            function_ran_successfully = True
        except Exception as e:
            function_ran_successfully = False
        self.assertTrue(function_ran_successfully)

    @patch('matplotlib.pyplot.pause', return_value=None)
    def test_random_values_within_range(self, mock_pause):
        """
        Test that the random values are within the specified range.
        """
        _, y_data = f_458(1)
        self.assertTrue(all(0 <= y <= 100 for y in y_data))

    @patch('matplotlib.pyplot.pause', return_value=None)
    @patch('f_458_ming.randint', return_value=50)
    def test_random_values_consistency(self, mock_randint, mock_pause):
        """
        Test that generated values are consistent with the mocked random function.
        """
        _, y_data = f_458(1)
        self.assertTrue(all(y == 50 for y in y_data))

    @patch('matplotlib.pyplot.pause', return_value=None)
    def test_timestamps_format(self, mock_pause):
        """
        Test that timestamps are in the expected format.
        """
        x_data, _ = f_458(1)
        for timestamp in x_data:
            datetime.strptime(timestamp, '%H:%M:%S.%f')


if __name__ == "__main__":
    unittest.main()
