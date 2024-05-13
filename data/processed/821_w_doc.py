import time
import threading


def task_func(delay_time: float = 1.0, num_threads: int = 5):
    '''
    Introduces a delay of 'delay_time' seconds in a specified number of separate threads and 
    returns the thread completion messages.

    Parameters:
    - delay_time (float): Amounf of delay time in seconds. Defalut is 1.
    - num_threads (int): Number of threads in which the delay should be introduced. Default is 5.

    Returns:
    - list: A list of strings containing the completion messages of the threads.
            The completion message looks as follow:
            'Delay in thread x completed'

    Requirements:
    - time
    - threading

    Example:
    >>> task_func(0.1, 3)
    ['Delay in thread 0 completed', 'Delay in thread 1 completed', 'Delay in thread 2 completed']

    >>> task_func(1, 10)
    ['Delay in thread 0 completed', 'Delay in thread 1 completed', 'Delay in thread 2 completed', 'Delay in thread 3 completed', 'Delay in thread 4 completed', 'Delay in thread 5 completed', 'Delay in thread 6 completed', 'Delay in thread 7 completed', 'Delay in thread 8 completed', 'Delay in thread 9 completed']
    '''

    results = []
    def delay():
        time.sleep(delay_time)
        results.append(f'Delay in thread {threading.current_thread().name} completed')
    for i in range(num_threads):
        t = threading.Thread(target=delay, name=str(i))
        t.start()
        t.join()  # Ensure that the thread completes before moving to the next
    return results

import unittest
from faker import Faker
class TestCases(unittest.TestCase):
    def test_case_1(self):
        start = time.time()
        result = task_func()
        end = time.time()
        exec_time = end - start
        self.assertAlmostEqual(exec_time, 5, places=0)
        self.assertEqual(len(result), 5)
    def test_case_2(self):
        start = time.time()
        result = task_func(0.2, 1)
        end = time.time()
        exec_time = end - start
        self.assertAlmostEqual(exec_time, 0.2, places=1)
        self.assertEqual(len(result), 1)
    def test_case_3(self):
        delay = 0.1
        threads = 10
        start = time.time()
        result = task_func(delay, threads)
        end = time.time()
        exec_time = end - start
        self.assertAlmostEqual(exec_time, delay*threads, places=0)
        self.assertEqual(len(result), 10)
    def test_case_4(self):
        result = task_func(num_threads=0)
        self.assertEqual(len(result), 0)
    def test_case_5(self):
        'test for exact return string'
        fake = Faker()
        num_threads = fake.random_int(min=1, max=20)
        result = task_func(num_threads=num_threads)
        self.assertEqual(len(result), num_threads)
        for i in range(num_threads):
            self.assertIn(f'Delay in thread {i} completed', result)
