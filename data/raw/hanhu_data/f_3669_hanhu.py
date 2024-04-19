import json
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class EnumEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Enum):
            return obj.name  # or obj.value, depending on the requirement
        return json.JSONEncoder.default(self, obj)

def f_3671(my_obj):
    """
    Serializes an object into a JSON string with support for complex data types like Enum.
    The function uses a custom JSONEncoder to handle Enum types by converting them to their names or values.

    Parameters:
    my_obj (object): The object to be serialized. Can be a dictionary, list, etc.

    Returns:
    str: The serialized JSON string of the object.

    Requirements:
    - json
    - enum

    Examples:
    Serialize a dictionary containing Enum.
    >>> result = f_3671({'color': Color.RED})
    >>> 'RED' in result
    True

    Serialize a simple dictionary.
    >>> f_3671({'name': 'Alice', 'age': 30})
    '{"name": "Alice", "age": 30}'
    """
    return json.dumps(my_obj, cls=EnumEncoder)

import unittest

class TestCases(unittest.TestCase):
    def test_enum_serialization(self):
        # Test serialization of a dictionary containing an Enum to check if the Enum is properly converted to its name.
        obj = {'color': Color.RED}
        result = f_3671(obj)
        self.assertIn('"color": "RED"', result)

    def test_multiple_enum_serialization(self):
        # Test serialization of a dictionary with a list of Enums to verify if all Enums are correctly serialized by their names.
        obj = {'colors': [Color.RED, Color.GREEN, Color.BLUE]}
        result = f_3671(obj)
        self.assertIn('"colors": ["RED", "GREEN", "BLUE"]', result)

    def test_no_enum_serialization(self):
        # Test serialization of a simple dictionary without Enums to ensure basic JSON serialization functionality is unaffected.
        obj = {'name': 'Bob', 'age': 25}
        result = f_3671(obj)
        self.assertEqual(result, '{"name": "Bob", "age": 25}')

    def test_nested_enum_serialization(self):
        # Test serialization of a nested dictionary containing an Enum to ensure deep serialization handles Enums correctly.
        obj = {'person': {'name': 'Alice', 'favorite_color': Color.BLUE}}
        result = f_3671(obj)
        self.assertIn('"favorite_color": "BLUE"', result)

    def test_empty_object_serialization(self):
        # Test serialization of an empty dictionary to verify the encoder handles empty objects correctly.
        obj = {}
        result = f_3671(obj)
        self.assertEqual(result, '{}')

    def test_direct_enum_serialization(self):
        # Test direct serialization of an Enum instance
        result = f_3671(Color.GREEN)
        self.assertEqual(result, '"GREEN"')

    def test_complex_nested_structures(self):
        # Test serialization of complex nested structures including Enum
        obj = {'people': [{'name': 'Alice', 'favorite_color': Color.BLUE}, {'name': 'Bob', 'favorite_color': Color.RED}]}
        result = f_3671(obj)
        self.assertIn('"favorite_color": "BLUE"', result)
        self.assertIn('"favorite_color": "RED"', result)


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
