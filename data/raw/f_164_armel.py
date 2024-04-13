import json

def f_164(json_string, sort_key='title'):
    """
    Given
    - a JSON string representing a list of dictionaries.
    - a key which is a string. It represents either one string or multiple strings separated by a dot ('.')
    Sort the JSON string by that specific key. If the JSON string has nested dictionaries, the function will sort the top-level dictionaries by the specified key.

    Parameters:
    json_string (str): The JSON string to sort.
    sort_key (str): The key to sort the JSON string by. Default is 'title'. 
                    If the key is nested within the JSON, use dot notation. 
                    E.g., 'address.street' will sort by the 'street' key inside an 'address' dictionary.

    Returns:
    str: The sorted JSON string.

    Requirements:
    - json

    Example:
    >>> json_string = '[{"title":"New York Times","title_url":"New_York_Times","id":4},{"title":"USA Today","title_url":"USA_Today","id":6},{"title":"Apple News","title_url":"Apple_News","id":2}]'
    >>> f_164(json_string, 'title')
    """
    # Function to handle nested keys
    def get_nested_item(data, key_list):
        for key in key_list:
            data = data[key]
        return data

    try:
        json_data = json.loads(json_string)
        keys = sort_key.split('.')
        json_data.sort(key=lambda x: get_nested_item(x, keys))
        sorted_json_string = json.dumps(json_data)
    except json.JSONDecodeError as e:
        raise ValueError(f"Error while decoding the JSON string: {str(e)}")
    except KeyError:
        raise KeyError(f"Key '{sort_key}' not found in the JSON string.")
        
    return sorted_json_string

import unittest
import json
from faker import Faker

def generate_mock_data(num_entries=5):
    fake = Faker()
    Faker.seed(0)
    data = []
    for _ in range(num_entries):
        entry = {
            "title": fake.company(),
            "details": {
                "address": {
                    "street": fake.street_name(),
                    "city": fake.city()
                },
                "website": fake.url(),
                "id": fake.random_number()
            },
            "employees": [fake.name() for _ in range(3)]
        }
        data.append(entry)
    return json.dumps(data)

class TestCases(unittest.TestCase):
    """Test cases for the f_164 function."""
    def test_case_1(self):
        json_string = '[{"title":"New York Times","title_url":"New_York_Times","id":4},{"title":"USA Today","title_url":"USA_Today","id":6},{"title":"Apple News","title_url":"Apple_News","id":2}]'
        expected_output = '[{"title": "Apple News", "title_url": "Apple_News", "id": 2}, {"title": "New York Times", "title_url": "New_York_Times", "id": 4}, {"title": "USA Today", "title_url": "USA_Today", "id": 6}]'
        self.assertEqual(f_164(json_string, 'title'), expected_output)

    def test_case_2(self):
        data = [
            {
                "title": "earthium",
                "details": {
                    "address" : {
                        "street": "street S1",
                        "city": "city C3",
                    },
                "website": "www.first.com",
                "id": "id 1",
                "employees": ["Marco", "Alice", "Bob"]
                }
            },
            {
                "title": "daranik",
                "details": {
                    "address" : {
                        "street": "street S0",
                        "city": "city 2",
                    },
                "website": "www.second.com",
                "id": "id 1",
                "employees": ["Marc", "Anna", "Bobby"],
                }
            },
            {
                "title": "arkemia",
                "details": {
                    "address" : {
                        "street": "street S4",
                        "city": "city C2",
                    },
                "website": "www.third.com",
                "id": "id 3",
                "employees": ["Arthur", "Jerome", "Zhang"]
                }
            },
        ]
        json_string = json.dumps(data)
        sorted_json = f_164(json_string, 'details.address.city')
        data = json.loads(sorted_json)
        cities = [entry['details']['address']['city'] for entry in data]
        self.assertEqual(cities, sorted(cities))
    
    def test_case_3(self):
        with self.assertRaises(KeyError):
            json_string = generate_mock_data()
            f_164(json_string, 'non_existent_key')
            
    def test_case_4(self):
        data = [
            {
                "title": "earthium",
                "details": {
                    "address" : {
                        "street": "street S1",
                        "city": "city C3",
                    },
                "website": "www.first.com",
                "id": "id 2",
                "employees": ["Marco", "Alice", "Bob"]
                }
            },
            {
                "title": "daranik",
                "details": {
                    "address" : {
                        "street": "street S0",
                        "city": "city 2",
                    },
                "website": "www.second.com",
                "id": "id 3",
                "employees": ["Marc", "Anna", "Bobby"],
                }
            },
            {
                "title": "arkemia",
                "details": {
                    "address" : {
                        "street": "street S4",
                        "city": "city C2",
                    },
                "website": "www.third.com",
                "id": "id 1",
                "employees": ["Arthur", "Jerome", "Zhang"]
                }
            },
        ]
        json_string = json.dumps(data)
        sorted_json = f_164(json_string, 'details.id')
        data = json.loads(sorted_json)
        ids = [entry['details']['id'] for entry in data]
        self.assertEqual(ids, sorted(ids))
    
    def test_case_5(self):
        with self.assertRaises(ValueError):
            incorrect_json = '[{"title":"New York Times","title_url":"New_York_Times", "id":4},]'
            f_164(incorrect_json, 'title')

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()
