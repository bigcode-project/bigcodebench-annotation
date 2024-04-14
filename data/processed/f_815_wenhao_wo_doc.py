import pathlib
import os


def f_815(path: str, delimiter: str = os.path.sep) -> list:
    """
    Validates that a given file path does not contain invalid characters for file paths
    then splits it into path components using a specified delimiter.

    Parameters:
    - path (str):      The file path to split. If empty, the function returns an empty list.
    - delimiter (str): The delimiter to use for splitting the path.
                       Defaults to the system's path separator (os.path.sep).

    Returns:
    - list: A list of the path components if the path is valid;
            otherwise, an empty list if the path contains invalid characters.

    Raises:
    - ValueError: If the path contains invalid characters.

    Requirements:
    - pathlib
    - os

    Notes:
    - Backslashes ('\\') are internally converted to forward slashes ('/') before processing.
    - This function treats '<', '>', ':', '"', '|', '?', '*' as invalid characters in paths.

    Examples:
    >>> f_815('Docs/src/Scripts/temp', '/')
    ['Docs', 'src', 'Scripts', 'temp']
    >>> f_815(r'Docs\\src\\Scripts\\temp', '\\\\')
    ['Docs', 'src', 'Scripts', 'temp']
    """

    if not path:
        return []

    path = path.replace("\\", "/")

    path_obj = pathlib.Path(path)

    invalid_chars = set('<>:"|?*')
    if any(
        set(str(component)).intersection(invalid_chars) for component in path_obj.parts
    ):
        return []

    return [
        component
        for component in path_obj.parts
        if component and component != delimiter
    ]

import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Testing a standard UNIX-like path with '/' delimiter
        self.assertEqual(
            f_815("Docs/src/Scripts/temp", "/"),
            ["Docs", "src", "Scripts", "temp"],
        )
    def test_case_2(self):
        # Testing a standard Windows-like path with '\' delimiter
        self.assertEqual(
            f_815("Docs\\src\\Scripts\\temp", "\\"),
            ["Docs", "src", "Scripts", "temp"],
        )
    def test_case_3(self):
        # Testing an empty path string
        self.assertEqual(f_815("", "/"), [])
    def test_case_4(self):
        # Testing a path with invalid characters
        self.assertEqual(f_815("Docs/src/Scripts|temp", "/"), [])
    def test_case_5(self):
        # Testing a path with a different delimiter
        self.assertEqual(f_815("Docs|src|Scripts|temp", "|"), [])
    def test_case_6(self):
        # Handle leading and trailing delimiters
        self.assertEqual(f_815("/Docs/src/Scripts/", "/"), ["Docs", "src", "Scripts"])
    def test_case_7(self):
        # Test mixed delimiters given expected conversion
        self.assertEqual(
            f_815("Docs/src\\Scripts/temp", "\\"), ["Docs", "src", "Scripts", "temp"]
        )
        self.assertEqual(
            f_815("Docs/src\\Scripts/temp", "/"), ["Docs", "src", "Scripts", "temp"]
        )
