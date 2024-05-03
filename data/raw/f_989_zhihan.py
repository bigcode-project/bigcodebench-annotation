import json
import requests
import os
import time

def f_989(json_data, unknown_key, save_dir=None):
    """
    Find a URL within nested json 'data' where the key is unknown, download the file from the URL, 
    and save it with a filename containing the key and a timestamp. The file will be saved with a ".txt" extension.
    
    Parameters:
    json_data (str): The json data as a string.
    unknown_key (str): The unknown key in the json.
    save_dir (str, optional): The directory to save the downloaded file. Defaults to the current directory.
    
    Returns:
    str: The file path of the downloaded file.
    
    Requirements:
    - json
    - requests
    - os
    - time
    
    Example:
    >>> json_str = '{"A": {"B": {"unknown": {"1": "F", "maindata": [{"Info": "https://example.com/file.txt"}]}}}}'
    >>> file_path = f_989(json_str, 'unknown')
    >>> print(file_path)
    """
    data = json.loads(json_data)
    url = list(data['A'][unknown_key].values())[0]['maindata'][0]['Info']
    
    response = requests.get(url)
    
    filename = f"{unknown_key}_{int(time.time())}.txt"
    save_dir = save_dir or os.getcwd()
    file_path = os.path.join(save_dir, filename)
    
    with open(file_path, 'wb') as f:
        f.write(response.content)

    return file_path

import unittest
import os

class TestF812(unittest.TestCase):

    def test_case_1(self):
        json_str = '{"A": {"B": {"unknown": {"1": "F", "maindata": [{"Info": "https://example.com/file.txt"}]}}}}'
        file_path = f_989(json_str, 'unknown')
        self.assertTrue(os.path.exists(file_path))
        os.remove(file_path)

    def test_case_2(self):
        json_str = '{"A": {"X": {"testkey": {"1": "G", "maindata": [{"Info": "https://example.com/file2.txt"}]}}}}'
        file_path = f_989(json_str, 'testkey')
        self.assertTrue(os.path.exists(file_path))
        os.remove(file_path)

    def test_case_3(self):
        json_str = '{"A": {"Y": {"anotherkey": {"1": "H", "maindata": [{"Info": "https://example.com/file3.txt"}]}}}}'
        save_dir = "./test_dir"
        if not os.path.exists(save_dir):
            os.mkdir(save_dir)
        file_path = f_989(json_str, 'anotherkey', save_dir=save_dir)
        self.assertTrue(os.path.exists(file_path))
        os.remove(file_path)
        os.rmdir(save_dir)

    def test_case_4(self):
        json_str = '{"A": {"Z": {"key4": {"1": "I", "maindata": [{"Info": "https://example.com/file4.txt"}]}}}}'
        file_path = f_989(json_str, 'key4')
        self.assertTrue(os.path.exists(file_path))
        os.remove(file_path)

    def test_case_5(self):
        json_str = '{"A": {"W": {"key5": {"1": "J", "maindata": [{"Info": "https://example.com/file5.txt"}]}}}}'
        file_path = f_989(json_str, 'key5')
        self.assertTrue(os.path.exists(file_path))
        os.remove(file_path)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestF812))
    runner = unittest.TextTestRunner()
    runner.run(suite)
if __name__ == "__main__":
    run_tests()