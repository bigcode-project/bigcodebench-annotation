import base64
import numpy as np
from PIL import Image
import tempfile

def f_187(array, img_format='png'):
    """
    Convert a numeric array into an image, save it to a temporary file, and then encode the image file with base64.

    Parameters:
    - array (np.array): A 2D or 3D numpy array representing image data.
    - img_format (str): The format of the image to save. Defaults to 'png'. Supported formats are 'png', 'jpeg', etc.

    Returns:
    - str: The base64 encoded image string.

    Requirements:
    - base64
    - numpy
    - Pillow (PIL)
    - tempfile

    Example:
    >>> array = np.zeros((100, 100))
    >>> encoded_image = f_187(array)
    >>> print(type(encoded_image))
    <class 'str'>
    """
    # Convert array to image
    image = Image.fromarray((array * 255).astype(np.uint8))
    
    # Create a temporary file to save the image
    with tempfile.NamedTemporaryFile(suffix=f".{img_format}", delete=False) as temp_file:
        image_path = temp_file.name
    
    # Save the image
    image.save(image_path)

    # Read the image and encode with base64
    with open(image_path, 'rb') as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    
    return encoded_image

import unittest
import numpy as np

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    """Test cases for the f_187 function.""" 
    def test_case_1(self):
        # Test grayscale image with all zeros
        array = np.zeros((100, 100))
        encoded_image = f_187(array)
        self.assertIsInstance(encoded_image, str)

    def test_case_2(self):
        # Test grayscale image with varying values
        array = np.random.rand(100, 100)
        encoded_image = f_187(array)        
        self.assertIsInstance(encoded_image, str)

    def test_case_3(self):
        # Test RGB image with all zeros
        array = np.zeros((100, 100, 3))
        encoded_image = f_187(array)
        self.assertIsInstance(encoded_image, str)

    def test_case_4(self):
        # Test RGB image with varying values
        array = np.random.rand(100, 100, 3)
        encoded_image = f_187(array)
        self.assertIsInstance(encoded_image, str)

    def test_case_5(self):
        # Test grayscale image with JPEG format
        array = np.zeros((100, 100))
        encoded_image = f_187(array, img_format="jpeg")
        self.assertIsInstance(encoded_image, str)

if __name__ ==  "__main__" :
    run_tests()