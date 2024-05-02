import json
import base64
from datetime import datetime

# Constants
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def f_1026(data: dict) -> str:
    """
    This function takes a Python dictionary, adds a timestamp to it, encodes the dictionary 
    into a JSON-formatted string, and then encodes the resulting string in ASCII using base64 encoding.
    
    Parameters:
    data (dict): The Python dictionary to encode. The dictionary should not contain a key named 'timestamp',
                 as this key is used to insert the current timestamp by the function.
    
    Returns:
    str: A base64 encoded string that represents the input dictionary with an added timestamp.
         The timestamp is added with the key 'timestamp' in the 'YYYY-MM-DD HH:MM:SS' format.
    
    Requirements:
    - The 'json' library is used to convert the Python dictionary to a JSON-formatted string.
    - The 'base64' library is used to encode the JSON-formatted string in ASCII.
    - The 'datetime' library is used to get the current timestamp in the specified format.
    
    Example:
    >>> data = {'name': 'John', 'age': 30, 'city': 'New York'}
    >>> encoded_data = f_1026(data)
    >>> print(encoded_data)  # The output will be a base64 encoded string representing the dictionary with the added timestamp.
    """
    # Adding current timestamp to the dictionary
    data['timestamp'] = datetime.now().strftime(DATE_FORMAT)

    # Encoding the dictionary to a JSON-formatted string and then encoding it in ASCII using base64 encoding
    json_data = json.dumps(data)
    encoded_data = base64.b64encode(json_data.encode('ascii')).decode('ascii')

    return encoded_data


import unittest
import json
import base64
from datetime import datetime

# Constants
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):

    def test_f_1026_basic(self):
        """Test the f_1026 function with a basic dictionary."""
        data = {'name': 'John', 'age': 30, 'city': 'New York'}
        encoded_data = f_1026(data)

        # Decoding the base64 encoded string to get the JSON string, and then loading it to get the dictionary
        decoded_data = json.loads(base64.b64decode(encoded_data).decode('ascii'))

        # Checking whether the obtained dictionary contains all the original keys and values, plus the added 'timestamp' key
        self.assertDictContainsSubset(data, decoded_data)

        # Checking whether the 'timestamp' is in the correct format
        datetime.strptime(decoded_data['timestamp'], DATE_FORMAT)

    def test_f_1026_empty(self):
        """Test the f_1026 function with an empty dictionary."""
        data = {}
        encoded_data = f_1026(data)

        # Decoding the base64 encoded string to get the JSON string, and then loading it to get the dictionary
        decoded_data = json.loads(base64.b64decode(encoded_data).decode('ascii'))

        # Checking whether the obtained dictionary contains only the added 'timestamp' key
        self.assertDictEqual(decoded_data, {'timestamp': decoded_data['timestamp']})

        # Checking whether the 'timestamp' is in the correct format
        datetime.strptime(decoded_data['timestamp'], DATE_FORMAT)

    def test_f_1026_nested(self):
        """Test the f_1026 function with a nested dictionary."""
        data = {'user': {'name': 'John', 'age': 30}, 'location': {'city': 'New York', 'country': 'USA'}}
        encoded_data = f_1026(data)

        # Decoding the base64 encoded string to get the JSON string, and then loading it to get the dictionary
        decoded_data = json.loads(base64.b64decode(encoded_data).decode('ascii'))

        # Checking whether the obtained dictionary contains all the original keys and values, plus the added 'timestamp' key
        self.assertDictContainsSubset(data, decoded_data)

        # Checking whether the 'timestamp' is in the correct format
        datetime.strptime(decoded_data['timestamp'], DATE_FORMAT)

    def test_f_1026_numeric(self):
        """Test the f_1026 function with a dictionary containing numeric keys and values."""
        data = {1: 10, 2: 20, 3: 30}
        encoded_data = f_1026(data)

        # Decoding the base64 encoded string to get the JSON string, and then loading it to get the dictionary
        decoded_data = json.loads(base64.b64decode(encoded_data).decode('ascii'))

        # JSON keys are always strings, so converting the original dictionary's keys to strings for comparison
        data_str_keys = {str(k): v for k, v in data.items()}

        # Checking whether the obtained dictionary contains all the original keys and values, plus the added 'timestamp' key
        self.assertDictContainsSubset(data_str_keys, decoded_data)

        # Checking whether the 'timestamp' is in the correct format
        datetime.strptime(decoded_data['timestamp'], DATE_FORMAT)

    def test_f_1026_mixed(self):
        """Test the f_1026 function with a dictionary containing mixed types of keys and values."""
        data = {'name': 'John', 1: 30, 'nested': {'key': 'value'}, 'list': [1, 2, 3]}
        encoded_data = f_1026(data)

        # Decoding the base64 encoded string to get the JSON string, and then loading it to get the dictionary
        decoded_data = json.loads(base64.b64decode(encoded_data).decode('ascii'))

        # JSON keys are always strings, so converting the original dictionary's keys to strings for comparison
        data_str_keys = {str(k): v for k, v in data.items()}

        # Checking whether the obtained dictionary contains all the original keys and values, plus the added 'timestamp' key
        self.assertDictContainsSubset(data_str_keys, decoded_data)

        # Checking whether the 'timestamp' is in the correct format
        datetime.strptime(decoded_data['timestamp'], DATE_FORMAT)


if __name__ == "__main__":
    run_tests()
