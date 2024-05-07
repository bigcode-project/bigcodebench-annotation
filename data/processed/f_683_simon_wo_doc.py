import time
import random


def f_810(iterations=5, min_delay=1.0, max_delay=2.0, seed=None):
    """
    Simulates a delay and then returns a message indicating the elapsed time. This is repeated for a specified number of iterations.

    For each iteration the delay is randomly sampled from a uniform distribution specified by min_delay and max_delay.
    After each iteration the message: '{delay} seconds have passed', where {delay} is replaces with the actual delay
    of the iteration with 2 positions after the decimal point, is saved to an array.

    The function returns a list of all messages, as well as the total delay.

    Parameters:
    - iterations (int): The number of times the delay and message should be simulated. Default is 5.
    - min_delay (float): The duration (in seconds) of the delay between messages. Default is 1.0.
    - max_delay (float): The max delay of each iteration in seconds. Default is 2.0
    - seed (float): The seed used for random sampling the delays for each iteration. Defalut is None.

    Returns:
    - list of str: A list of messages indicating the elapsed time for each iteration.
    - float: The total amount of delay

    Raises:
    - ValueError: If iterations is not a positive integer or if min_delay/max_delay is not a positive floating point value.

    Requirements:
    - time
    - random
    
    Example:
    >>> messages, delay = f_810(2, 0.4, seed=1)
    >>> print(messages)
    ['0.61 seconds have passed', '1.76 seconds have passed']
    >>> print(delay)
    2.3708767696794144

    >>> messages, delay = f_810(2, 2.0, 4.2, seed=12)
    >>> print(messages)
    ['3.04 seconds have passed', '3.45 seconds have passed']
    >>> print(delay)
    6.490494998960768
    """
    random.seed(seed)
    if not isinstance(iterations, int) or iterations <= 0:
        raise ValueError("iterations must be a positive integer.")
    if not isinstance(min_delay, (int, float)) or min_delay <= 0:
        raise ValueError("min_delay must be a positive floating point value.")
    if not isinstance(max_delay, (int, float)) or max_delay <= min_delay:
        raise ValueError("max_delay must be a floating point value larger than min_delay.")
    total_delay = 0
    messages = []
    for _ in range(iterations):
        delay = random.uniform(min_delay, max_delay)
        total_delay += delay
        time.sleep(delay)
        message_string = f'{delay:.2f} seconds have passed'
        messages.append(message_string)
    return messages, total_delay

import unittest
import time
class TestCases(unittest.TestCase):
    def test_case_1(self):
        start_time = time.time()
        messages, total_delay = f_810(3, 0.2, 0.3, 12)
        elapsed_time = time.time() - start_time
        self.assertEqual(messages, ['0.25 seconds have passed', '0.27 seconds have passed', '0.27 seconds have passed'])
        self.assertAlmostEqual(elapsed_time, total_delay, delta=0.1)
        
    def test_case_2(self):
        start_time = time.time()
        result, total_delay = f_810(1, 0.5, 2.5, seed=42)
        elapsed_time = time.time() - start_time
        self.assertEqual(result, ['1.78 seconds have passed'])
        self.assertAlmostEqual(elapsed_time, total_delay, delta=0.1)
        
    def test_case_3(self):
        start_time = time.time()
        result, total_delay = f_810(seed=123)
        elapsed_time = time.time() - start_time
        self.assertEqual(result, ['1.05 seconds have passed',
                                  '1.09 seconds have passed',
                                  '1.41 seconds have passed',
                                  '1.11 seconds have passed',
                                  '1.90 seconds have passed'
                                  ])
        self.assertAlmostEqual(elapsed_time, total_delay, delta=0.1)
        
    def test_case_4(self):
        with self.assertRaises(ValueError):
            f_810(-1, 1.0)
        
    def test_case_5(self):
        with self.assertRaises(ValueError):
            f_810(3, -1.0)
    def test_case_rng(self):
        mess1, del1 = f_810(3, 0.1, 0.2, seed=12)
        mess2, del2 = f_810(3, 0.1, 0.2, seed=12)
        self.assertEqual(mess1, mess2)
        self.assertAlmostEqual(del1, del2, delta=0.05)
        mess3, del3 = f_810(5, 0.01, 0.05)
        mess4, del4 = f_810(5, 0.01, 0.05)
        self.assertNotEqual(mess3, mess4)
        self.assertNotAlmostEqual(del3, del4)
