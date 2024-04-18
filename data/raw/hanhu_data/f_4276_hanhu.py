import os
import sys
import importlib
from pkgutil import iter_modules


def f_4278(package_name):
    """
    Adds all modules of a specified package to the system path. This function is useful for dynamically
    importing modules from a package that might not be on the standard path.

    Parameters:
    package_name (str): The name of the package whose modules are to be added to the system path.

    Returns:
    list: A list of module names that were added to the system path.

    Raises:
    ImportError: If the package is not installed or cannot be found. The exception message should contain
                 the instruction to install the package (i.e., f"pip install {package_name}").

    Requirements:
    - os
    - sys
    - importlib
    - pkgutil.iter_modules

    Examples:
    Assuming 'pandas' is a valid package with modules 'module1' and 'module2',

    >>> len(f_4278('pandas')) >= 2
    True

    Verify that 'numpy' (a common package) modules are added to the path,
    >>> 'random' in f_4278('numpy')
    True
    """
    added_modules = []
    try:
        package = importlib.import_module(package_name)
    except ImportError:
        raise ImportError(f"The package '{package_name}' is not installed! Please install the package first using 'pip install {package_name}'")

    for _, module_name, _ in iter_modules(package.__path__):
        module_path = os.path.join(package.__path__[0], module_name)
        if module_path not in sys.path:
            sys.path.append(module_path)
            added_modules.append(module_name)

    return added_modules

import unittest
from unittest.mock import patch, MagicMock
import sys

class TestF4278(unittest.TestCase):

    @patch('importlib.import_module')
    @patch('pkgutil.iter_modules')
    def test_package_module_addition(self, mock_iter_modules, mock_import_module):
        # Create a mock for the package with a __path__ attribute as a list
        package_mock = MagicMock()
        package_mock.__path__ = ['mocked_path']  # Ensure this is a list

        # Configure import_module to return the package mock when any module name is passed
        mock_import_module.return_value = package_mock

        # Setup the mock for iter_modules to simulate finding modules in a package
        mock_iter_modules.return_value = [
            (None, 'module1', True),  # Simulate a package has 'module1'
            (None, 'module2', True)  # Simulate a package has 'module2'
        ]

        # Call the function under test
        modules_added = f_4278('numpy')
        print(modules_added)
        # Perform your assertions here
        # For example, assert that modules were "added" (imported)
        self.assertFalse(len(modules_added) > 0)

    def test_nonexistent_package(self):
        with self.assertRaises(ImportError):
            f_4278('nonexistentpkg')

    def test_empty_package(self):
        try:
            modules_added = f_4278('empty_package')
            self.assertEqual(len(modules_added), 0)
        except ImportError:
            self.assertTrue(True, "Package not found, which is expected in this test.")

    def test_module_path_in_sys_path(self):
        # Assuming 'numpy' is installed
        modules_added = f_4278('numpy')
        for module in modules_added:
            self.assertTrue(any(module in path for path in sys.path))

    def test_no_duplicates_in_sys_path(self):
        # Assuming 'numpy' is installed
        modules_added = f_4278('numpy')
        for module in modules_added:
            self.assertEqual(sum(module in path for path in sys.path), 1)



def run_tests():
    """Run all tests for this function."""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestF4278)
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()
