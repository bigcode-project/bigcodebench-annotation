import time
from datetime import datetime
import random
import matplotlib.pyplot as plt

# Constants
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def f_118(n, output_path=None):
    """
    Generate n random Unix timestamps and convert them to strings formatted as UTC DATE_FORMAT.
    Plot a histogram of the distribution of the generated timestamps. If an output path is provided,
    save the histogram to the specified path. Otherwise, display the plot.

    Parameters:
    n (int): The number of timestamps to generate.
    output_path (str, optional): Path to save the histogram plot. Defaults to None.

    Returns:
    list: The list of n formatted timestamps.

    Requirements:
    - time
    - datetime
    - random
    - matplotlib.pyplot

    Example:
    >>> random.seed(42)
    >>> timestamps = f_118(n=3, output_path=None)
    >>> print(timestamps)
    ['2013-07-06 20:56:46', '1977-07-29 23:34:23', '1971-09-14 11:29:44']
    """
    timestamps = []
    for _ in range(n):
        timestamp = random.randint(0, int(time.time()))
        formatted_time = datetime.utcfromtimestamp(timestamp).strftime(DATE_FORMAT)
        timestamps.append(formatted_time)

    plt.hist([datetime.strptime(t, DATE_FORMAT) for t in timestamps])

    if output_path:
        plt.savefig(output_path)
    else:
        plt.show()
    return timestamps


import unittest
import os

class TestCases(unittest.TestCase):
    """Test cases for the f_118 function."""

    def setUp(self):
        self.test_dir = "data/f_118"
        os.makedirs(self.test_dir, exist_ok=True)

        self.o_1 = os.path.join(self.test_dir, "histogram_1.png")

    def tearDown(self) -> None:
        import shutil

        try:
            shutil.rmtree(self.test_dir)
        except:
            pass

    def test_case_1(self):
        random.seed(42)
        result = f_118(10)
        self.assertEqual(len(result), 10)

    def test_case_2(self):
        random.seed(42)
        result = f_118(15)
        for timestamp in result:
            try:
                datetime.strptime(timestamp, DATE_FORMAT)
            except ValueError:
                self.fail(f"Timestamp {timestamp} doesn't match the specified format.")

    def test_case_3(self):
        random.seed(42)
        f_118(20, output_path=self.o_1)
        self.assertTrue(os.path.exists(self.o_1))

    def test_case_4(self):
        result = f_118(50)
        self.assertEqual(len(result), len(set(result)))

    def test_case_5(self):
        result = f_118(0)
        self.assertEqual(len(result), 0)


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run_tests()
