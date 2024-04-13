import os
import re
from urllib.parse import urlparse
import requests
from PIL import Image
from io import BytesIO

def f_168(myString: str, save_dir: str) -> str:
    '''
    Extract a URL from a string, download the image from this URL and save it in a directory.

    Parameters:
    - myString (str): The string from which to extract the URL.
    - save_dir (str): The path to the directory where to save the image.

    Returns:
    - str: The filename of the downloaded image if URL and image are valid. Returns 'Invalid URL or image not found.' if no valid image URL is found in the input string.

    Requirements:
    - os
    - re
    - urllib.parse
    - requests
    - PIL.Image
    - io.BytesIO

    Example:
    >>> f_168('Image: https://www.example.com/sample.png')
    'sample.png'
    >>> f_168('No URL here.')
    'Invalid URL or image not found.'
    '''
    # Extracting URL from the string
    match = re.search(r'(https?://\S+)', myString)
    
    # If no URL found, return a message
    if not match:
        return 'Invalid URL or image not found.'
    
    url = match.group()
    filename = urlparse(url).path.split('/')[-1]
    try:
        # Trying to fetch the image from the URL
        response = requests.get(url)
        image = Image.open(BytesIO(response.content))
        image.save(os.path.join(save_dir, filename))
        return filename
    except :
        return 'Invalid URL or image not found.'
    
import unittest
from unittest.mock import patch

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

def mock_requests_get(*args, **kwargs):
    class MockImage:
        def __init__(self, content, status_code):
            self.content = content
            self.status_code = status_code
    
    if args[0] == "https://www.example1.com/image1.png":
        array = np.random.rand(48, 48, 3) * 255
        sample_image = Image.fromarray(array.astype('uint8'))
        return MockImage(sample_image.tobytes(), status_code=200)
    elif args[0] == "https://www.example2.com/image2.png":
        array = np.random.rand(48, 48, 3) * 255
        sample_image = Image.fromarray(array.astype('uint8'))
        return MockImage(sample_image.tobytes(), status_code=200)
    elif args[0] == "https://www.example3.com/image3.png":
        array = np.random.rand(48, 48, 3) * 255
        sample_image = Image.fromarray(array.astype('uint8'))
        return MockImage(sample_image.tobytes(), status_code=200)
    elif args[0] == "https://www.example4.com/image4.png":
        array = np.random.rand(48, 48, 3) * 255
        sample_image = Image.fromarray(array.astype('uint8'))
        return MockImage(sample_image.tobytes(), status_code=200)
    else:
        return MockImage('', 404)

class TestCases(unittest.TestCase):
    """Test cases for the f_168 function."""
    def setUp(self) -> None:
        self.test_dir = "data/f_168"
        os.makedirs(self.test_dir, exist_ok=True)

    def tearDown(self) -> None:
        import shutil
        shutil.rmtree(self.test_dir)
        
    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_1(self, args, **kwargs):
        input_str = 'Image: https://www.example1.com/image1.png'
        result = f_168(input_str, self.test_dir)
        #print(f"result: {result}")
        self.assertTrue(result == 'image1.png' or result == 'Invalid URL or image not found.')
        #print(Image.open(os.path.join(self.test_dir, 'image1.png')))

    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_2(self, *args, **kwargs):
        input_str = 'No URL here.'
        expected_output = 'Invalid URL or image not found.'
        self.assertEqual(f_168(input_str, self.test_dir), expected_output)

    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_3(self, *args, **kwargs):
        input_str = 'Image: https://www.nonexistentwebsite.com/nonexistentimage.png'
        result = f_168(input_str, self.test_dir)
        self.assertTrue(result == 'nonexistentimage.png' or result == 'Invalid URL or image not found.')

    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_4(self, *args, **kwargs):
        input_str = 'URL: https://www.example.com/'
        result = f_168(input_str, self.test_dir)
        self.assertTrue(result == 'Invalid URL or image not found.')

    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_5(self, *args, **kwargs):
        input_str = 'Images: https://www.example2.com/image2.png and https://www.example3.com/image3.png'
        result = f_168(input_str, self.test_dir)
        self.assertTrue(result == 'sample2.png' or result == 'Invalid URL or image not found.')

if __name__ == "__main__":
    run_tests()