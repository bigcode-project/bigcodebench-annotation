import numpy as np
from sklearn.preprocessing import MinMaxScaler

def f_72(my_dict):
    """
    Updates a dictionary by adding a normalized version of a numpy array found under the 'array' key.
    The normalization is performed using MinMaxScaler, scaling each value to fall between 0 and 1.

    Parameters:
        my_dict (dict): A dictionary containing a key 'array' with a numpy array as its value.

    Returns:
        dict: The dictionary after adding a key 'normalized_array' with the normalized values.

    Notes:
        The function modifies the dictionary in-place and does not create a new dictionary.
        The function assumes that 'array' key exists and its value is a numpy array.

    Raises:
        TypeError if the value of the 'array' key in my_dict is not a numpy array
        
    Requirements:
    - numpy
    - sklearn.preprocessing.MinMaxScaler

    Examples:
    >>> example_dict = {'array': np.array([1, 2, 3, 4, 5])}
    >>> result = f_72(example_dict)
    >>> 'normalized_array' in result
    True
    >>> isinstance(result['normalized_array'], np.ndarray)
    True
    """
    if not isinstance(my_dict["array"], np.ndarray):
        raise TypeError
    SCALER = MinMaxScaler()
    array = my_dict['array'].reshape(-1, 1)
    normalized_array = SCALER.fit_transform(array).reshape(-1)
    my_dict['normalized_array'] = normalized_array
    return my_dict

import unittest
import numpy as np
from unittest.mock import patch
class TestCases(unittest.TestCase):
    def test_return_type(self):
        """Test that the function returns a dictionary."""
        result = f_72({'array': np.array([1, 2, 3])})
        self.assertIsInstance(result, dict)
    def test_normalized_array_presence(self):
        """Test that 'normalized_array' key is present in the returned dictionary."""
        result = f_72({'array': np.array([1, 2, 3])})
        self.assertIn('normalized_array', result)
    def test_normalized_array_values(self):
        """Test that the normalized array contains correct values."""
        input_array = np.array([10, 20, 30])
        expected_normalized = np.array([0., 0.5, 1.])
        result = f_72({'array': input_array})
        np.testing.assert_array_almost_equal(result['normalized_array'], expected_normalized)
    def test_single_value_array(self):
        """Test the function with a single value array."""
        result = f_72({'array': np.array([42])})
        self.assertEqual(result['normalized_array'][0], 0)  # Single value should be normalized to 0
    def test_inplace_modification(self):
        """Test that the function modifies the input dictionary in place."""
        input_dict = {'array': np.array([1, 2, 3])}
        result = f_72(input_dict)
        self.assertIs(result, input_dict)
        self.assertIn('normalized_array', input_dict)
    def test_negative_values_normalization(self):
        """Test normalization on an array with negative values."""
        input_array = np.array([-10, 0, 10])
        expected_normalized = np.array([0., 0.5, 1.])
        result = f_72({'array': input_array})
        np.testing.assert_array_almost_equal(result['normalized_array'], expected_normalized)
    def test_key_error_raise(self):
        """Test that a KeyError is raised if 'array' key is missing."""
        with self.assertRaises(KeyError):
            f_72({})
    def test_type_error_raise(self):
        """Test that a TypeError is raised if value is not a numpy array."""
        with self.assertRaises(TypeError):
            f_72({'array': [1, 2, 3]})
    @patch('sklearn.preprocessing.MinMaxScaler.fit_transform')
    def test_mock_minmaxscaler(self, mock_fit_transform):
        """Test the function with a mock of MinMaxScaler's fit_transform method."""
        input_array = np.array([1, 2, 3])
        mock_fit_transform.return_value = input_array.reshape(-1, 1)
        f_72({'array': input_array})
        mock_fit_transform.assert_called_once()
