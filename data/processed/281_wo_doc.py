import re
import os
from collections import Counter


def task_func(folder_path: str) -> dict:
    """
    Scan a directory for log files and count the occurrences of each IP address in all files.
    
    Parameters:
    - folder_path (str): The path to the directory containing log files to be scanned.
    
    Returns:
    dict: A dictionary with IP addresses as keys and their counts as values.
    
    Requirements:
    - re
    - os
    - collections.Counter
    
    The function utilizes a regular expression pattern to identify IP addresses in the log files.
    
    Example:
    >>> import tempfile
    >>> temp_dir = tempfile.mkdtemp() # Create a temporary directory that is empty
    >>> task_func(temp_dir)
    {}
    """

    IP_REGEX = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
    counter = Counter()
    for filename in os.listdir(folder_path):
        if filename.endswith('.log'):
            with open(os.path.join(folder_path, filename)) as file:
                content = file.read()
                ips = re.findall(IP_REGEX, content)
                counter.update(ips)
    return dict(counter)

import unittest
import tempfile
import doctest
class TestCases(unittest.TestCase):
    def setUp(self):
        self.test_data_dir = tempfile.mkdtemp()
        self.log_text_1 = "Request from 102.168.0.1\nRequest from 118.128.1.11\nRequest from 175.193.115.67"
        self.log_text_2 = "Request from 189.56.7.1\nRequest from 128.45.234.88\nRequest from 985.123.1.1"
        self.log_text_3 = "Request from localhost\nRequest from remote"
        self.log_text_4 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam nec odio. Sed non posuere."
        self.log_text_5 = "Request from 181.94.113.34\nMemory usage: 50"
    def test_case_1(self):
        """Tests with 5 log files containing various IP addresses."""
        with open(os.path.join(self.test_data_dir, "file1.log"), 'w') as file:
            file.write(self.log_text_1)
        with open(os.path.join(self.test_data_dir, "file2.log"), 'w') as file:
            file.write(self.log_text_2)
        with open(os.path.join(self.test_data_dir, "file3.log"), 'w') as file:
            file.write(self.log_text_3)
        with open(os.path.join(self.test_data_dir, "file4.log"), 'w') as file:
            file.write(self.log_text_4)
        with open(os.path.join(self.test_data_dir, "file5.log"), 'w') as file:
            file.write(self.log_text_5)
        result = task_func(self.test_data_dir)
        expected = {
            '189.56.7.1': 1, 
            '128.45.234.88': 1, 
            '985.123.1.1': 1, 
            '102.168.0.1': 1, 
            '118.128.1.11': 1, 
            '175.193.115.67': 1, 
            '181.94.113.34': 1
        }
        self.assertDictEqual(result, expected)
    
    def test_case_2(self):
        """Tests with an empty directory."""
        empty_dir = os.path.join(self.test_data_dir, "empty_dir")
        os.makedirs(empty_dir, exist_ok=True)
        result = task_func(empty_dir)
        self.assertDictEqual(result, {})
    
    def test_case_3(self):
        """Tests with a directory containing only non-log files."""
        non_log_dir = os.path.join(self.test_data_dir, "non_log_dir")
        os.makedirs(non_log_dir, exist_ok=True)
        with open(os.path.join(non_log_dir, "file.txt"), 'w') as file:
            file.write("192.168.0.1\n192.168.0.2")
        result = task_func(non_log_dir)
        self.assertDictEqual(result, {})
    
    def test_case_4(self):
        """Tests with log files not containing any IP addresses."""
        no_ip_dir = os.path.join(self.test_data_dir, "no_ip_dir")
        os.makedirs(no_ip_dir, exist_ok=True)
        with open(os.path.join(no_ip_dir, "file.log"), 'w') as file:
            file.write("This is a log file without any IP addresses.")
        result = task_func(no_ip_dir)
        self.assertDictEqual(result, {})
    
    def test_case_5(self):
        """Tests with log files containing IP addresses and other numbers."""
        mix_num_dir = os.path.join(self.test_data_dir, "mix_num_dir")
        os.makedirs(mix_num_dir, exist_ok=True)
        with open(os.path.join(mix_num_dir, "file.log"), 'w') as file:
            file.write("192.168.0.1\n255.255.255.255\n10.0.0.1\n12345")
        result = task_func(mix_num_dir)
        expected = {
            '192.168.0.1': 1,
            '10.0.0.1': 1,
            '255.255.255.255': 1,
        }
        self.assertDictEqual(result, expected)
