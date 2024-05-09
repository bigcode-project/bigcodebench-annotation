import re
import socket

def task_func(ip_addresses: list) -> dict:
    """
    Given a list of IP addresses, this function returns a dictionary mapping each valid IP address to its 
    respective hostname. If the hostname cannot be determined, the value will be None.
    
    Parameters:
    ip_addresses (list): A list of IP addresses.
    
    Returns:
    dict: A dictionary with IP addresses as keys and their hostnames as values. If the hostname cannot be determined,
          the value will be None.
    
    Requirements:
    - re
    - socket
    
    Example:
    >>> task_func(['8.8.8.8', '8.8.4.4'])
    {'8.8.8.8': 'dns.google', '8.8.4.4': 'dns.google'}
    """
    IP_REGEX = r'[0-9]+(?:\.[0-9]+){3}'
    hostnames = {}
    for ip in ip_addresses:
        if re.match(IP_REGEX, ip):
            try:
                hostname = socket.gethostbyaddr(ip)[0]
                hostnames[ip] = hostname
            except (socket.herror, socket.gaierror):
                hostnames[ip] = None
    return hostnames

import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        result = task_func(['8.8.8.8', '8.8.4.4'])
        expected = {'8.8.8.8': 'dns.google', '8.8.4.4': 'dns.google'}
        self.assertDictEqual(result, expected)
    def test_case_2(self):
        result = task_func(['8.8.4.4'])
        expected = {'8.8.4.4': 'dns.google'}
        self.assertDictEqual(result, expected)
    def test_case_3(self):
        result = task_func(['256.256.256.256'])
        expected = {'256.256.256.256': None}
        self.assertDictEqual(result, expected)
    def test_case_4(self):
        result = task_func([])
        expected = {}
        self.assertDictEqual(result, expected)
    def test_case_5(self):
        result = task_func(['1.1.1.1', '2.2.2.2'])
        expected_keys = ['1.1.1.1', '2.2.2.2']
        self.assertListEqual(list(result.keys()), expected_keys)
