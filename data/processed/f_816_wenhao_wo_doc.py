import os
import shutil


def f_576(path, delimiter="/"):
    """
    Splits a given file path by a specific delimiter and computes disk usage for each directory component.

    Parameters:
    - path (str): The file path to split.
    - delimiter (str, optional): The delimiter to use for splitting the path. Default is '/'.

    Returns:
    list: A list of tuples where each tuple contains a path component and its disk usage as a dictionary.
          The disk usage dictionary contains keys 'total', 'used', and 'free'.

    Raises:
    - ValueError: If the 'path' is empty, not a string, or contain invalid components.
    - FileNotFoundError: If the 'path' does not exist in the filesystem.

    Requirements:
    - os
    - shutil

    Examples:
    >>> f_576('Docs/src', '/')
    [('Docs', {'total': 100, 'used': 50, 'free': 50}), ('src', {'total': 200, 'used': 100, 'free': 100})]

    >>> f_576('a/b', '/')
    [('a', {'total': 300, 'used': 150, 'free': 150}), ('b', {'total': 400, 'used': 200, 'free': 200})]
    """
    if not path or not isinstance(path, str):
        raise ValueError("Path must be a non-empty string")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Path '{path}' does not exist")

    path_components = path.strip(delimiter).split(delimiter)
    if not all(path_components):
        raise ValueError("Path contains invalid components")

    results = []
    for index, component in enumerate(path_components):
        sub_path = delimiter.join(path_components[: index + 1])
        if not sub_path.startswith(delimiter):
            sub_path = delimiter + sub_path
        usage = shutil.disk_usage(sub_path)
        results.append(
            (component, {"total": usage.total, "used": usage.used, "free": usage.free})
        )

    return results

import unittest
from collections import namedtuple
from unittest.mock import patch
import tempfile
import os
class TestCases(unittest.TestCase):
    def setUp(self):
        DiskUsage = namedtuple("DiskUsage", ["total", "used", "free"])
        # Setup realistic disk usage values for different directories
        self.mock_usage_root = DiskUsage(500000000000, 300000000000, 200000000000)
        self.mock_usage_docs = DiskUsage(100000000000, 50000000000, 50000000000)
        self.mock_usage_src = DiskUsage(50000000000, 25000000000, 25000000000)
        self.mock_usage_home = DiskUsage(200000000000, 100000000000, 100000000000)
    def disk_usage_side_effect(self, path):
        # Helper for mocking
        if path.endswith("src"):
            return self.mock_usage_src
        elif path.endswith("Docs"):
            return self.mock_usage_docs
        elif path == "/home":
            return self.mock_usage_home
        return self.mock_usage_root
    @patch("os.path.exists")
    def test_nonexist_path(self, mock_exists):
        # Test function should raise error if path does not exist
        mock_exists.return_value = True
        with tempfile.TemporaryDirectory() as tmpdirname:
            non_exist_path = os.path.join(tmpdirname, "nonexist")
            with self.assertRaises(FileNotFoundError):
                f_576(non_exist_path)
    def test_invalid_path(self):
        # Test function should raise error if path is not valid
        with self.assertRaises(ValueError):
            f_576("")
        with self.assertRaises(ValueError):
            f_576(123)
    @patch("os.path.exists")
    @patch("shutil.disk_usage")
    def test_varied_path(self, mock_disk_usage, mock_exists):
        # Test functionality
        mock_exists.return_value = True
        mock_disk_usage.side_effect = self.disk_usage_side_effect
        result = f_576("Docs/src")
        expected = [
            (
                "Docs",
                {
                    "total": self.mock_usage_docs.total,
                    "used": self.mock_usage_docs.used,
                    "free": self.mock_usage_docs.free,
                },
            ),
            (
                "src",
                {
                    "total": self.mock_usage_src.total,
                    "used": self.mock_usage_src.used,
                    "free": self.mock_usage_src.free,
                },
            ),
        ]
        self.assertEqual(result, expected)
    @patch("os.path.exists")
    @patch("shutil.disk_usage")
    def test_deep_nested_path(self, mock_disk_usage, mock_exists):
        # Test nested paths
        mock_exists.return_value = True
        mock_disk_usage.return_value = self.mock_usage_src
        deep_path = "Docs/src/Projects/Python/Example"
        result = f_576(deep_path)
        expected = [
            ("Docs", self.mock_usage_src._asdict()),
            ("src", self.mock_usage_src._asdict()),
            ("Projects", self.mock_usage_src._asdict()),
            ("Python", self.mock_usage_src._asdict()),
            ("Example", self.mock_usage_src._asdict()),
        ]
        self.assertEqual(result, expected)
    @patch("os.path.exists")
    @patch("shutil.disk_usage")
    def test_single_directory(self, mock_disk_usage, mock_exists):
        # Test function works on single directory
        mock_exists.return_value = True
        mock_disk_usage.return_value = self.mock_usage_home
        result = f_576("home")
        expected = [("home", self.mock_usage_home._asdict())]
        self.assertEqual(result, expected)
    @patch("os.path.exists")
    @patch("shutil.disk_usage")
    def test_path_with_multiple_delimiters(self, mock_disk_usage, mock_exists):
        # Test should fail if there is an invalid path component
        mock_exists.return_value = True
        mock_disk_usage.side_effect = lambda path: {
            "/Docs": self.mock_usage_docs,
            "/Docs/src": self.mock_usage_src,
        }.get(path, self.mock_usage_root)
        with self.assertRaises(ValueError):
            result = f_576("Docs//src")
            expected = [
                ("Docs", self.mock_usage_docs._asdict()),
                ("", {"total": 0, "used": 0, "free": 0}),
                ("src", self.mock_usage_src._asdict()),
            ]
            self.assertEqual(result, expected)
    @patch("os.path.exists")
    @patch("shutil.disk_usage")
    def test_path_with_trailing_delimiter(self, mock_disk_usage, mock_exists):
        # Test should handle trailing delimiter
        mock_exists.return_value = True
        mock_disk_usage.side_effect = lambda path: {
            "/Docs": self.mock_usage_docs,
            "/Docs/src": self.mock_usage_src,
        }.get(path, self.mock_usage_root)
        result = f_576("Docs/src/")
        expected = [
            ("Docs", self.mock_usage_docs._asdict()),
            ("src", self.mock_usage_src._asdict()),
        ]
        self.assertEqual(result, expected)
