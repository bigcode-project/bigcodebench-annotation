import requests
import os
import json
import time

# Redefining the function in the current context

HEADERS = {
    'accept': 'text/json',
    'Content-Type': 'application/json'
}

def f_333(url, directory, metadata):
    """
    Upload all files from a specific directory to the specified server URL, along with the associated metadata. 
    In addition, the speed limit function pauses for one second after each upload.

    Parameters:
    url (str): The server URL.
    directory (str): The directory containing the files to be uploaded.
    metadata (dict): The metadata to be associated with the files.

    Returns:
    list: A list of status codes for the upload responses.

    Requirements:
    - requests
    - os
    - json
    - time

    Example:
    >>> f_333('https://www.example.com', './uploads', {'userId': 'abc'})
    """

    files = os.listdir(directory)
    status_codes = []

    for file in files:
        if os.path.isfile(os.path.join(directory, file)):
            with open(os.path.join(directory, file), 'rb') as f:
                files = {'file': f}
                response = requests.post(url, files=files, headers=HEADERS, data=json.dumps(metadata))
                status_codes.append(response.status_code)
                time.sleep(1)

    return status_codes

import unittest
from unittest.mock import patch, Mock
import os
TEST_URL = "https://www.example.com"
TEST_DIRECTORY = "./test_uploads_f_333"
TEST_DIRECTORY_EMPTY = "./test_uploads_f_333_empty"
TEST_METADATA = {'userId': 'abc'}
# Mocking the requests.post method
def mock_requests_post(*args, **kwargs):
    class MockResponse:
        def __init__(self, status_code):
            self.status_code = status_code
        
    # Simulate successful upload (status code 200)
    return MockResponse(200)
# Mocking the requests.post method fail
def mock_requests_post_fail(*args, **kwargs):
    class MockResponse:
        def __init__(self, status_code):
            self.status_code = status_code
        
    # Simulate fail upload (status code 404)
    return MockResponse(400)
class TestCases(unittest.TestCase):
    def setUp(self):
        # Create a test directory with dummy files
        os.makedirs(TEST_DIRECTORY, exist_ok=True)
        for i in range(5):
            with open(os.path.join(TEST_DIRECTORY, f"test_file_{i}.txt"), "w") as f:
                f.write(f"This is test file {i}")
        os.makedirs(TEST_DIRECTORY_EMPTY, exist_ok=True)
    def tearDown(self):
        # Remove the test directory and its contents after testing
        if os.path.exists(TEST_DIRECTORY):
            for file in os.listdir(TEST_DIRECTORY):
                os.remove(os.path.join(TEST_DIRECTORY, file))
            os.rmdir(TEST_DIRECTORY)
        if os.path.exists(TEST_DIRECTORY_EMPTY):
            os.rmdir(TEST_DIRECTORY_EMPTY)
    @patch('requests.post', side_effect=mock_requests_post)
    def test_upload_success(self, mock_post):
        # Test successful upload with mock response
        status_codes = f_333(TEST_URL, TEST_DIRECTORY, TEST_METADATA)
        self.assertEqual(status_codes, [200, 200, 200, 200, 200])
    @patch('requests.post', side_effect=mock_requests_post)
    def test_directory_not_found(self, mock_post):
        # Test if directory does not exist
        with self.assertRaises(FileNotFoundError):
            f_333(TEST_URL, "non_existing_directory", TEST_METADATA)
    @patch('requests.post', side_effect=mock_requests_post)
    def test_empty_directory(self, mock_post):
        # Test if directory is empty
        status_codes = f_333(TEST_URL, TEST_DIRECTORY_EMPTY, TEST_METADATA)
        self.assertEqual(status_codes, [])
    def test_invalid_url(self):
        # Test with invalid URL
        with self.assertRaises(Exception):
            f_333("invalid_url", TEST_DIRECTORY, TEST_METADATA)
    @patch('requests.post', side_effect=mock_requests_post_fail)
    def test_urls(self, mock_post):
        status_codes = f_333(TEST_URL, TEST_DIRECTORY, TEST_METADATA)
        self.assertEqual(status_codes, [400, 400, 400, 400, 400])
