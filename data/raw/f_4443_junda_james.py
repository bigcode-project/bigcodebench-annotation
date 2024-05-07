import inspect
import pandas as pd
import os

def f_4443(f_list, file_path):
    """
    Exports the specifications of functions in 'f_list' to a CSV file at 'file_path'.

    The CSV file columns are as follows:
    - 'Function Name': The name of the function.
    - 'Number of Arguments': The number of arguments the function takes.
    - 'Defaults': Default values for the function's arguments, if any.
    - 'Annotations': Type annotations of the function's arguments and return value, if any.
    - 'Is Lambda': Boolean value indicating whether the function is a lambda function.

    Each row in the CSV file corresponds to a function in 'f_list'.

    Parameters:
    f_list (list): A list of function objects to inspect. Each element should be a callable object.
    file_path (str): The path (including filename) where the CSV file will be saved. Should be a writable path.

    Returns:
    None

    Requirements:
    - os
    - inspect
    - pandas

    Raises:
    - ValueError: If 'f_list' is not a list of functions, 'f_list' is empty, or 'file_path' is not a valid path.
    - IOError: If there's an error in writing to the specified file path.

    Example:
    >>> def f(x): return 2 * x
    >>> def g(x, y=2): return x * y
    >>> f_4443([f, g], './function_info.csv')
    >>> os.remove('./function_info.csv')
    """
    
    if not all(callable(f) for f in f_list):
        raise ValueError("All elements in f_list must be callable functions.")
    if not f_list:
        raise ValueError("f_list should not be empty.")
    if not isinstance(file_path, str):
        raise ValueError("file_path must be a string.")


    func_info = []
    for f in f_list:
        spec = inspect.getfullargspec(f)
        is_lambda = lambda x: x.__name__ == (lambda: None).__name__
        func_info.append([
            f.__name__, 
            len(spec.args), 
            spec.defaults, 
            spec.annotations, 
            is_lambda(f)
        ])

    df = pd.DataFrame(func_info, columns=['Function Name', 'Number of Arguments', 'Defaults', 'Annotations', 'Is Lambda'])
    try:
        df.to_csv(file_path, index=False)
    except IOError as e:
        raise IOError(f"Error writing to file: {e}")

import unittest
import pandas as pd
import os

class TestCases(unittest.TestCase):
    def test_valid_input(self):
        def sample_func(x, y=1): return x + y
        f_4443([sample_func], 'test.csv')
        df = pd.read_csv('test.csv')
        self.assertEqual(df.loc[0, 'Function Name'], 'sample_func')
        self.assertEqual(df.loc[0, 'Number of Arguments'], 2)
        self.assertIsNotNone(df.loc[0, 'Defaults'])
        self.assertFalse(df.loc[0, 'Is Lambda'])

    def test_empty_function_list(self):
        with self.assertRaises(ValueError):
            f_4443([], 'test.csv')

    def test_invalid_function_list(self):
        with self.assertRaises(ValueError):
            f_4443([1, 2, 3], 'test.csv')

    def test_invalid_file_path(self):
        with self.assertRaises(ValueError):
            f_4443([lambda x: x], 123)

    def test_io_error(self):
        def sample_func(x): return x
        with self.assertRaises(IOError):
            f_4443([sample_func], '/invalidpath/test.csv')

    def test_lambda_function(self):
        f_4443([lambda x: x], 'test.csv')
        df = pd.read_csv('test.csv')
        self.assertTrue(df.loc[0, 'Is Lambda'])

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove('test.csv')
        except OSError:
            pass
    
    def test_multiple_functions(self):
        def func_a(x): return x * 2
        def func_b(x, y=1): return x + y
        lambda_func = lambda x: x ** 2

        f_4443([func_a, func_b, lambda_func], 'test.csv')
        df = pd.read_csv('test.csv')

        # Check if all functions are listed
        expected_names = ['func_a', 'func_b', '<lambda>']
        self.assertListEqual(list(df['Function Name']), expected_names)

        # Check number of arguments
        self.assertEqual(df.loc[df['Function Name'] == 'func_a', 'Number of Arguments'].values[0], 1)
        self.assertEqual(df.loc[df['Function Name'] == 'func_b', 'Number of Arguments'].values[0], 2)
        self.assertEqual(df.loc[df['Function Name'] == '<lambda>', 'Number of Arguments'].values[0], 1)

        # Check if lambda is correctly identified
        self.assertFalse(df.loc[df['Function Name'] == 'func_a', 'Is Lambda'].values[0])
        self.assertFalse(df.loc[df['Function Name'] == 'func_b', 'Is Lambda'].values[0])
        self.assertTrue(df.loc[df['Function Name'] == '<lambda>', 'Is Lambda'].values[0])

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