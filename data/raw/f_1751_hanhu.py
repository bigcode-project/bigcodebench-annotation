import numpy as np
from scipy.stats import mode

def f_1752(my_dict):
    """
    Updates a given dictionary by adding the mode (most frequent element) of a numpy array found under the 'array' key.
    The function calculates the mode of the numpy array and adds it to the dictionary with the key 'mode'.
    The original dictionary is modified in place.

    Parameters:
        my_dict (dict): A dictionary that must contain the key 'array' with a non-empty numpy array as its value.

    Returns:
        dict: The original dictionary with the added key 'mode'. The value is the mode of the array.

    Note:
        - The function assumes that the 'array' key exists in the dictionary and it is non-empty.
        - If 'array' is not present or is empty, a runtime error will occur.
        - It assumes the array is not empty

    Requirements:
    - numpy
    - scipy.stats.mode

    Examples:
    >>> example_dict = {'array': np.array([1, 2, 2, 3, 3, 3])}
    >>> result = f_1752(example_dict)
    >>> 'mode' in result and result['mode'] == 3
    True
    >>> 'array' in f_1752({'array': np.array([1, 1, 2])})
    True
    """
    mode_value = mode(my_dict['array']).mode[0]
    my_dict['mode'] = mode_value
    return my_dict

import unittest
import numpy as np

class TestCases(unittest.TestCase):
    def test_return_type(self):
        """Test that the function returns a dictionary."""
        result = f_1752({'array': np.array([1, 2, 3])})
        self.assertIsInstance(result, dict)

    def test_mode_calculation(self):
        """Test that the mode is correctly calculated."""
        result = f_1752({'array': np.array([1, 2, 2, 3])})
        self.assertEqual(result['mode'], 2)

    def test_multiple_modes(self):
        """Test that in case of multiple modes, the first mode encountered is returned."""
        result = f_1752({'array': np.array([1, 1, 2, 2, 3])})
        self.assertEqual(result['mode'], 1)

    def test_preservation_of_original_dict(self):
        """Test that original keys in the dictionary are preserved after adding the mode."""
        original_dict = {'array': np.array([1, 1, 2, 2, 3]), 'other_key': 'value'}
        result = f_1752(original_dict)
        self.assertIn('other_key', result)
        self.assertEqual(result['other_key'], 'value')

    def test_dictionary_length_update(self):
        """Test that the dictionary length is correctly updated when a new 'mode' key is added."""
        original_dict = {'array': np.array([1, 2, 3]), 'other_key': 'value'}
        expected_length = len(original_dict) + 1
        result = f_1752(original_dict)
        self.assertEqual(len(result), expected_length)

    def test_missing_array_key(self):
        """Test that the function raises a KeyError when the 'array' key is missing."""
        with self.assertRaises(KeyError):
            f_1752({})

    def test_single_element_array(self):
        """Test that the function correctly handles an array with a single element."""
        result = f_1752({'array': np.array([42])})
        self.assertEqual(result['mode'], 42)



def run_tests():
    """Run all tests for this function."""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestCases)
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()
