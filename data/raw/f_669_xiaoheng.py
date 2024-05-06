import numpy as np
import random

# Constants
ELEMENTS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

def f_669(l=None):
    """
    Create a numeric array from a list "l" and move the first 3 elements to the end of the array.

    Parameters:
    - l (list): A list of elements to be processed.

    Returns:
    - arr (numpy.ndarray): The processed array with the first three elements moved to the end.

    Requirements:
    - numpy
    - random

    Example:
    >>> random.seed(42)
    >>> f_669(ELEMENTS)
    array(['I', 'F', 'G', 'J', 'E', 'A', 'B', 'H', 'D', 'C'], dtype='<U1')
    """
    if l is None:
        l = ELEMENTS.copy()  # Use a copy to avoid modifying the original list
    random.shuffle(l)
    arr = np.array(l)
    arr = np.concatenate((arr[3:], arr[:3]))
    return arr

import unittest
import numpy as np

class TestCases(unittest.TestCase):
    def test_default_input(self):
        # Test Case 1: Default Input
        # Description: This test case checks the function's behavior with its default settings.
        # The random seed is set to ensure reproducibility.
        random.seed(42)
        result = f_669()
        expected_output = np.array(['I', 'F', 'G', 'J', 'E', 'A', 'B', 'H', 'D', 'C'])
        np.testing.assert_array_equal(result, expected_output)

    def test_custom_list_input(self):
        # Test Case 2: Custom List Input
        # Description: This test case checks the function's behavior with a custom list of elements.
        # The random seed is set to ensure reproducibility.
        random.seed(42)
        input_list = ['X', 'Y', 'Z', 'W', 'V', 'U']
        result = f_669(input_list)
        expected_output = np.array(['V', 'X', 'U', 'W', 'Y', 'Z'])  # Corrected based on actual shuffle and cycle
        np.testing.assert_array_equal(result, expected_output)

    def test_empty_list(self):
        # Test Case 3: Empty List
        # Description: This test case checks the function's behavior when an empty list is provided as input.
        # The random seed is set to ensure reproducibility, though it doesn't affect the outcome in this case.
        random.seed(42)
        result = f_669([])
        self.assertEqual(len(result), 0)

    def test_single_element_list(self):
        # Test Case 4: Single Element List
        # Description: This test case checks the function's behavior with a single element list.
        # The random seed is set to ensure reproducibility.
        random.seed(42)
        result = f_669(['X'])
        expected_output = np.array(['X'])
        np.testing.assert_array_equal(result, expected_output)

    def test_three_elements_list(self):
        # Test Case 5: Three Elements List
        # Description: This test case checks the function's behavior with a three element list.
        # The random seed is set to ensure reproducibility.
        random.seed(42)
        result = f_669(['Y', 'X', 'Z'])
        expected_output = np.array(['X', 'Y', 'Z'])  # Corrected based on actual shuffle and cycle
        np.testing.assert_array_equal(result, expected_output)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()
