import bs4
import requests
import os

def f_171(url="http://example.com", headers={'User-Agent': 'Mozilla/5.0'}, save_dir="data/f_171"):
    """
    Scratches a web page to extract all image URLs and saves the images to the hard drive.
    - Save the images in save_dir.
    - If save_dir does not exist make sure to create it.
    - THe image should be saved as jpg, with their names being img0, img1, img2, img3 etc.

    Parameters:
    - url (str): The web page from which data is fetched. Default is "http://example.com".
    - headers (dict): HTTP headers for the request. Default includes 'User-Agent' as 'Mozilla/5.0'.
    - save_dir (str): Path to the directory where to save the images.
    
    Requirements:
    - bs4
    - requests
    - os
    
    Example:
    >>> f_171()
    """
    response = requests.get(url, headers=headers)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    image_urls = [img['src'] for img in soup.find_all('img')]

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    for i, img_url in enumerate(image_urls):
        response = requests.get(url + img_url if url.endswith("/") else url + "/" + img_url)
        with open(os.path.join(save_dir, 'img{}.jpg'.format(i)), 'wb') as f:
            f.write(response.content)

import unittest
from unittest.mock import patch

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

def mock_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, text, status_code):
            self.text = text
            self.status_code = status_code
    
    class MockImage:
        def __init__(self, content, status_code):
            self.content = content
            self.status_code = status_code
    
    if args[0] == "http://www.example1.com":
        content = """
        <html>
            <body>
                <h1>Hello, BeautifulSoup!</h1>
                <ul>
                    <li><a href="index.html"><img alt="Soumission" class="thumbnail" src="image11.jpg"/></a></li>
                    <li><a href="index.html"><img alt="Soumission" class="thumbnail" src="image12.jpg"/></a></li>
                </ul>
            </body>
        </html>
        """
        return MockResponse(
            content,
            200
        )
    elif args[0] == "http://www.example1.com/image11.jpg":
        return MockImage(content=b"This is image 11", status_code=200)
    elif args[0] == "http://www.example1.com/image12.jpg":
        return MockImage(content=b"This is image 12", status_code=200)
    elif args[0] == "http://www.example2.com":
        content = """
        <html>
            <body>
                <h1>Hello, BeautifulSoup!</h1>
                <ul>
                    <li><a href="index.html"><img alt="Soumission" class="thumbnail" src="image2.jpg"/></a></li>
                </ul>
            </body>
        </html>
        """
        return MockResponse(
            content,
            200
        )
    elif args[0] == "http://www.example2.com/image2.jpg":
        return MockImage(content=b"This is image 2", status_code=200)
    elif args[0] == "http://www.example3.com":
        content = """
        <html>
            <body>
                <h1>Hello, BeautifulSoup!</h1>
                <ul>
                    <li><a href="index.html"><img alt="Soumission" class="thumbnail" src="image3.jpg"/></a></li>
                </ul>
            </body>
        </html>
        """
        return MockResponse(
            content,
            200
        )
    elif args[0] == "http://www.example3.com/image3.jpg":
        return MockImage(content=b"This is image 3", status_code=200)
    elif args[0] == "http://www.example4.com":
        content = """
        <html>
            <body>
                <h1>Hello, BeautifulSoup!</h1>
                <ul>
                    <li><a href="index.html"><img alt="Soumission" class="thumbnail" src="image4.jpg"/></a></li>
                </ul>
            </body>
        </html>
        """
        return MockResponse(
            content,
            200
        )
    elif args[0] == "http://www.example4.com/image4.jpg":
        return MockImage(content=b"This is image 4", status_code=200)
    else:
        return MockResponse('', 404)
    
class TestCases(unittest.TestCase):
    """Test cases for the f_171 function."""
    def setUp(self):
        self.test_dir = "data/f_171"
        os.makedirs(self.test_dir, exist_ok=True)
    def tearDown(self) -> None:
        import shutil
        shutil.rmtree(self.test_dir)
        
    @patch('requests.get', side_effect=mock_requests_get) 
    #@patch('requests.get', side_effect=mock_requests_get) 
    #@patch('requests.get', side_effect=mock_requests_get)   
    def test_case_1(self, *args, **kwargs):
        f_171("http://www.example1.com", save_dir=self.test_dir)
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "img0.jpg")))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "img1.jpg")))

    @patch('requests.get', side_effect=mock_requests_get) 
    #@patch('requests.get', side_effect=mock_requests_get) 
    def test_case_2(self, *args, **kwargs):
        f_171("http://www.example2.com", save_dir=self.test_dir)
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "img0.jpg")))

    @patch('requests.get', side_effect=mock_requests_get) 
    #@patch('requests.get', side_effect=mock_requests_get) 
    def test_case_3(self, *args, **kwargs):
        f_171("http://www.example3.com", save_dir=self.test_dir)
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "img0.jpg")))

    @patch('requests.get', side_effect=mock_requests_get)
    #@patch('requests.get', side_effect=mock_requests_get) 
    def test_case_4(self, *args, **kwargs):
        f_171("http://www.example4.com", save_dir=self.test_dir)
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "img0.jpg")))

    @patch('requests.get', side_effect=mock_requests_get) 
    def test_case_5(self, *args, **kwargs):
        f_171("http://www.example5.com", save_dir=self.test_dir)
        self.assertTrue(len(os.listdir(self.test_dir)) == 0)

if __name__ == "__main__":
    run_tests()