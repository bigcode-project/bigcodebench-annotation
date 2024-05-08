from collections import Counter
import logging

def f_682(letter_list, element, log_path):
    """
    Count the frequency of a particular letter in a given list of letters with logging.

    Logs are written to a file named 'f_682.log' with encoding 'utf-8' and logging level DEBUG.
    The log file is created by the function or overwritten if already exists.
    For each function call the following is logged with the respective logging level:
        - info: f"Function called with list: {letter_list} and element: {element}"
        - error: if the element is not in the letter list
        - info: f"Frequency of '{element}' is {element_frequency}"
    
    After the last info has been logged, the logging is shutdown, such that all
    files are released.

    Parameters:
    letter_list (list of str): The list of letters.
    element (str): The specific letter for which the frequency needs to be counted.
    log_path (str): the path to the folder in which to save the log file

    Returns:
    int: The frequency of the letter.

    Raises:
    ValueError: If element is not in letter_list.

    Requirements:
    - collections
    - logging

    Example:
    >>> f_682(['a', 'b', 'a', 'c', 'a'], 'a', log_path='./')
    3
    >>> with open('f_682.log') as log:
    ...     print(log.read())
    INFO:Function called with list: ['a', 'b', 'a', 'c', 'a'] and element: a
    INFO:Frequency of 'a' is 3
    <BLANKLINE>

    >>> f_682(['x', 'y', 'z'], 'y', log_path='./')
    1
    >>> with open('f_682.log') as log:
    ...     print(log.read())
    INFO:Function called with list: ['x', 'y', 'z'] and element: y
    INFO:Frequency of 'y' is 1
    <BLANKLINE>

    >>> try:
    ...     f_682(['x', 'y', 'z'], 'a', log_path='./')
    ... except:
    ...     with open('f_682.log') as log:
    ...        print(log.read())
    INFO:Function called with list: ['x', 'y', 'z'] and element: a
    ERROR:The element is not in the letter list.
    <BLANKLINE>

    """
    formatter = logging.Formatter('%(levelname)s:%(message)s')
    handler = logging.FileHandler(log_path+'/f_682.log', mode='w')
    logger = logging.getLogger()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    logger.info(f"Function called with list: {letter_list} and element: {element}")

    if element not in letter_list:
        logger.error("The element is not in the letter list.")
        logger.handlers[0].close
        logger.removeHandler(logger.handlers[0])
        logging.shutdown()

        raise ValueError("The element is not in the letter list.")
        
    letter_frequencies = Counter(letter_list)
    element_frequency = letter_frequencies[element]
    
    logger.info(f"Frequency of '{element}' is {element_frequency}")
    logger.handlers[0].close
    logger.removeHandler(logger.handlers[0])
    logging.shutdown()

    return element_frequency


import unittest
import os, shutil
import tempfile

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):

    def setUp(self):
        self.temp_folder = tempfile.mkdtemp()

    def test_case_1(self):
        result = f_682(['a', 'b', 'a', 'c', 'a'], 'a', self.temp_folder)
        self.assertEqual(result, 3)
        with open(self.temp_folder+'/f_682.log') as log:
            self.assertTrue("INFO:Function called with list: ['a', 'b', 'a', 'c', 'a'] and element: a" in log.readline())
            self.assertTrue("INFO:Frequency of 'a' is 3" in log.readline())

    def test_case_2(self):
        result = f_682(['x', 'y', 'z'], 'y', self.temp_folder)
        self.assertEqual(result, 1)
        with open(self.temp_folder+'/f_682.log') as log:
            self.assertTrue("INFO:Function called with list: ['x', 'y', 'z'] and element: y" in log.readline())
            self.assertTrue("INFO:Frequency of 'y' is 1" in log.readline())

    def test_case_3(self):
        result = f_682(['m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'], 'r', self.temp_folder)
        self.assertEqual(result, 1)
        with open(self.temp_folder+'/f_682.log') as log:
            self.assertTrue("INFO:Function called with list: ['m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'] and element: r" in log.readline())
            self.assertTrue("INFO:Frequency of 'r' is 1" in log.readline())

    def test_case_4(self):
        result = f_682(['z', 'z', 'z', 'z'], 'z', self.temp_folder)
        self.assertEqual(result, 4)
        with open(self.temp_folder+'/f_682.log') as log:
            self.assertTrue("INFO:Function called with list: ['z', 'z', 'z', 'z'] and element: z" in log.readline())
            self.assertTrue("INFO:Frequency of 'z' is 4" in log.readline())

    def test_case_5(self):
        with self.assertRaises(ValueError):
            f_682(['a', 'b', 'c'], 'z', self.temp_folder)
        with open(self.temp_folder+'/f_682.log') as log:
            self.assertTrue("INFO:Function called with list: ['a', 'b', 'c'] and element: z" in log.readline())
            self.assertTrue("ERROR:The element is not in the letter list." in log.readline())



if __name__ == "__main__":
    run_tests()