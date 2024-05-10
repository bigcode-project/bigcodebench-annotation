import re
import json
import os


def f_290(file_path: str, regex_pattern=r'\(.+?\)|\w') -> dict:
    """
    Extracts matches from a JSON file based on a predefined regular pattern.
    The default regular expression pattern is designed to extract any content between parentheses
    as a single match and any individual character outside the parentheses as a separate match.
    
    Parameters:
    - file_path (str): The path to the JSON file. The JSON file should contain key-value pairs
                       where the values are strings to be matched against the regex pattern.
                       
    Returns:
    - dict: A dictionary with the JSON file name as the key and a list of matches as values.
            The format is: {filename: [match1, match2, ...]}.
            
    Requirements:
    - The function makes use of the following libraries/modules: re, json, os.
    
    Example:
    >>> import tempfile
    >>> temp_dir = tempfile.gettempdir()
    >>> file_path = os.path.join(temp_dir, 'sample_data.json')
    >>> with open(file_path, 'w') as file:
    ...     json.dump({'content': 'This is a (sample) text with some (matches) and characters.'}, file)
    >>> matches = f_290(file_path)
    >>> len(matches['sample_data.json'])
    34
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
        text = ' '.join(data.values())
        matches = re.findall(regex_pattern, text)

    match_dict = {os.path.basename(file_path): matches}
    return match_dict


import unittest
import shutil
import doctest
import tempfile


class TestCases(unittest.TestCase):

    def setUp(self):
        sample_data = {
            "data1.json": {
                "text1": "This is a (sample) text with some (matches) and characters.",
                "text2": "Another (example) with multiple matches."
            },
            "data2.json": {
                "text1": "(Hello) world!",
                "text2": "No matches here."
            },
            "data3.json": {
                "text1": "Testing (with) another (file).",
                "text2": "Just some (random) text."
            },
            "data4.json": {
                "text1": "(A) quick brown (fox) jumps.",
                "text2": "Over the lazy (dog)."
            },
            "data5.json": {
                "text1": "Yet (another) test file.",
                "text2": "With (various) matches."
            }
        }

        # Directory to save the test data
        self.base_tmp_dir = tempfile.mkdtemp()
        self.test_data_dir = f"{self.base_tmp_dir}/test/"

        # Create the directory if it doesn't exist
        if not os.path.exists(self.test_data_dir):
            os.makedirs(self.test_data_dir)

        # Saving the test data as JSON files
        for filename, content in sample_data.items():
            with open(os.path.join(self.test_data_dir, filename), "w") as file:
                json.dump(content, file)

    def tearDown(self):
        # Remove the test data directory
        shutil.rmtree(self.test_data_dir)

    def test_case_1(self):
        matches = f_290(os.path.join(self.test_data_dir, "data1.json"))
        expected = {
            "data1.json": [
                'T', 'h', 'i', 's', 'i', 's', 'a', '(sample)', 't', 'e', 'x', 't', 'w', 'i', 't', 
                'h', 's', 'o', 'm', 'e', '(matches)', 'a', 'n', 'd', 'c', 'h', 'a', 'r', 'a', 'c', 
                't', 'e', 'r', 's', 'A', 'n', 'o', 't', 'h', 'e', 'r', '(example)', 'w', 'i', 't',
                'h', 'm', 'u', 'l', 't', 'i', 'p', 'l', 'e', 'm', 'a', 't', 'c', 'h', 'e', 's'
            ]
        }
        self.assertEqual(matches, expected)

    def test_case_2(self):
        matches = f_290(os.path.join(self.test_data_dir, "data2.json"))
        expected = {
            "data2.json": [
                '(Hello)', 'w', 'o', 'r', 'l', 'd', 'N', 'o', 'm', 'a', 't', 'c', 'h', 
                'e', 's', 'h', 'e', 'r', 'e'
            ]
        }
        self.assertEqual(matches, expected)

    def test_case_3(self):
        matches = f_290(os.path.join(self.test_data_dir, "data3.json"))
        expected = {
            "data3.json": [
                'T', 'e', 's', 't', 'i', 'n', 'g', '(with)', 'a', 'n', 'o', 't', 'h', 'e', 'r', '(file)', 'J',
                'u', 's', 't', 's', 'o', 'm', 'e', '(random)', 't', 'e', 'x', 't'    
            ]
        }
        self.assertEqual(matches, expected)

    def test_case_4(self):
        matches = f_290(os.path.join(self.test_data_dir, "data4.json"))
        expected = {
            "data4.json": [
                '(A)', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', '(fox)', 'j', 'u', 'm', 'p',
                's', 'O', 'v', 'e', 'r', 't', 'h', 'e', 'l', 'a', 'z', 'y', '(dog)'
            ]
        }
        self.assertEqual(matches, expected)

    def test_case_5(self):
        matches = f_290(os.path.join(self.test_data_dir, "data5.json"))
        expected = {
            "data5.json": [
                'Y', 'e', 't', '(another)', 't', 'e', 's', 't', 'f', 'i', 'l', 'e', 'W', 'i', 't', 
                'h', '(various)', 'm', 'a', 't', 'c', 'h', 'e', 's'   
            ]
        }
        self.assertEqual(matches, expected)


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    doctest.testmod()
    run_tests()
