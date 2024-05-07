import psutil
import platform

def f_1020():
    """
    Obtain system details, including operating system, architecture, and memory usage.
    
    This function gathers information about the system's operating system, architecture,
    and memory usage. It calculates the percentage of used memory  by comparing the total
    and currently used memory. The gathered details are then returned in a dictionary 
    format with specific keys for each piece of information.
    
    Returns:
    dict: A dictionary containing:
        - 'OS': Operating System name (e.g., 'Windows', 'Linux').
        - 'Architecture': System architecture (typically first item from platform.architecture(), e.g., '64bit').
        - 'Memory Usage': Formatted string representing the percentage of memory currently in use, 
                            calculated as (used memory / total memory) * 100.
  
    Requirements:
    - platform
    - psutil

    Examples:
    >>> system_info = f_1020()
    >>> isinstance(system_info, dict)
    True
    >>> 'OS' in system_info
    True
    >>> 'Architecture' in system_info
    True
    >>> 'Memory Usage' in system_info
    True
    """
    system_info = {}

    system_info['OS'] = platform.system()
    system_info['Architecture'] = platform.architecture()[0]

    total_memory = psutil.virtual_memory().total
    used_memory = psutil.virtual_memory().used
    system_info['Memory Usage'] = f'{used_memory/total_memory*100:.2f}%'

    return system_info

import unittest

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    
    def test_presence_OS(self):
        """Test that the result has the correct keys and that each key maps to the expected data type."""
        result = f_1020()
        self.assertTrue('OS' in result and isinstance(result['OS'], str))

    def test_presence_architecture(self):
        """Test that the result has the correct keys and that each key maps to the expected data type."""
        result = f_1020()
        self.assertTrue('Architecture' in result and isinstance(result['Architecture'], str))

    def test_presence_memory_usage(self):
        """Test that the result has the correct keys and that each key maps to the expected data type."""
        result = f_1020()
        self.assertTrue('Memory Usage' in result and isinstance(result['Memory Usage'], str))

    def test_return_type(self):
        """Test that the result has the correct keys and that each key maps to the expected data type."""
        result = f_1020()
        self.assertIsInstance(result, dict)

    def test_memory_usage_format(self):
        """Test that the 'Memory Usage' key is correctly formatted as a percentage."""
        result = f_1020()
        self.assertRegex(result['Memory Usage'], r"\d{1,3}\.\d{2}%")
    
    def test_non_empty_values(self):
        """Ensure that the values associated with each key are non-empty."""
        result = f_1020()
        for key, value in result.items():
            self.assertTrue(bool(value))

if __name__ == "__main__":
    run_tests()