import re
from urllib import request
import json

# Constants
IP_REGEX = r'[0-9]+(?:\.[0-9]+){3}'

def task_func(ip_address):
    """
    Get the public IP address from a JSON response containing the IP address.
    
    Parameters:
    ip_address (str): JSON-formatted string containing the IP address. 

    Returns:
    str: The public IP address.
    
    Note:
    - The function needs to check whether the provided IP address is valid.
      If the IP address is not valid, the function will return 'Invalid IP address received'.

    Requirements:
    - re
    - urllib.request
    - json
    
    Example:
    >>> ip_address = '{"ip": "192.168.1.1"}'
    >>> task_func(ip_address)
    '192.168.1.1'
    """
    try:
        response = ip_address
        data = json.loads(response)
        ip = data['ip']
        if re.match(IP_REGEX, ip):
            return ip
        else:
            return 'Invalid IP address received'
    except Exception as e:
        return str(e)

import unittest
import json
class TestCases(unittest.TestCase):
    def test_case_1(self):
        ip_address = json.dumps({'ip': '192.168.1.1'}).encode('utf-8')
        
        result = task_func(ip_address)
        self.assertEqual(result, '192.168.1.1')
    def test_case_2(self):
        ip_address = json.dumps({'ip': '500.500.500.500'}).encode('utf-8')
        
        result = task_func(ip_address)
        self.assertEqual(result, '500.500.500.500')
    def test_case_3(self):
        ip_address = json.dumps({'ip': '192.168.0.3'}).encode('utf-8')
        
        result = task_func(ip_address)
        self.assertEqual(result, '192.168.0.3')
    def test_case_4(self):
        ip_address = json.dumps({'ip': ''}).encode('utf-8')
        
        result = task_func(ip_address)
        self.assertEqual(result, 'Invalid IP address received')
    def test_case_5(self):
        ip_address = json.dumps({'ip': 'Non-JSON response'}).encode('utf-8')
        
        result = task_func(ip_address)
        self.assertEqual(result, 'Invalid IP address received')
