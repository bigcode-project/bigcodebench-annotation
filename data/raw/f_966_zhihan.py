from collections import defaultdict
import os
import json
import glob

def f_966(source_dir, target_file):
    """
    Aggregate data from all JSON files in a specified directory and write the aggregated data to a target JSON file.
    
    Functionality:
    This function aggregates data from multiple JSON files located in the specified source directory. 
    Each key-value pair in the source JSON files is aggregated, with values for the same key being collected into a list.
    The aggregated data is then written to the target JSON file.
    
    Parameters:
    - source_dir (str): The directory containing the source JSON files. 
      (For example: 'path/to/source/')
    - target_file (str): The path to the target JSON file where aggregated data will be written.
      (For example: 'path/to/target.json')
    
    Returns:
    str: The path to the created target JSON file.
    
    Requirements:
    - os
    - json
    - glob
    - collections.defaultdict
    
    Examples:
    >>> f_966('path/to/source/', 'path/to/target.json')
    'path/to/target.json'
    
    >>> f_966('another/path/to/source/', 'another/path/to/target.json')
    'another/path/to/target.json'
    """
    aggregated_data = defaultdict(list)

    for file_name in glob.glob(os.path.join(source_dir, '*.json')):
        with open(file_name, 'r') as file:
            data = json.load(file)
            for key, value in data.items():
                aggregated_data[key].append(value)

    with open(target_file, 'w') as file:
        json.dump(aggregated_data, file)

    return target_file

import unittest
import os
import json

# Mock data for testing
MOCK_DIR = "test_data/"
MOCK_TARGET = "test_data/mock_target.json"


class TestAggregateJsonFiles(unittest.TestCase):
    def test_aggregation(self):
        # Run the function with mock data
        result_path = f_966(MOCK_DIR, MOCK_TARGET)
        
        # Load the aggregated data from the target file
        with open(result_path, "r") as file:
            aggregated_data = json.load(file)
            
        # Assertions to check if the aggregation is correct
        self.assertEqual(aggregated_data["name"], ["John", "Jane"])
        self.assertEqual(aggregated_data["age"], [25, 30])
        self.assertEqual(aggregated_data["city"], ["London", "Paris"])
        self.assertEqual(aggregated_data["country"], ["France"])

    # Additional test cases can be added as needed

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestAggregateJsonFiles))
    runner = unittest.TextTestRunner()
    runner.run(suite)
if __name__ == "__main__":
    run_tests()