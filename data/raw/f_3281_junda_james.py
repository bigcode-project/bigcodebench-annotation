from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os

def f_3281(img_path, angle):
    """
    Open an image, rotate it around a certain angle, and then display both the original and the rotated images side by side. 
    Additionally, return both images as numpy arrays.

    Parameters:
    img_path (str): The path of the image file.
    angle (float): The angle to rotate the image (in degrees).

    Returns:
    tuple: A tuple containing two numpy arrays, the first representing the original image and 
           the second representing the rotated image. Expands the rotated image to make it large enough to hold the entire rotated image.

    Raises:
    FileNotFoundError: If the image file does not exist at the specified path.

    Requirements:
    - PIL
    - matplotlib
    - numpy
    - os

    Example:
    >>> img_path = 'sample.png'
    >>> create_dummy_image(image_path=img_path)
    >>> original_img_array, rotated_img_array = f_3281(img_path, 45)
    >>> os.remove(img_path)
    """
    if not os.path.exists(img_path):
        raise FileNotFoundError(f"No file found at {img_path}")
    
    img = Image.open(img_path)
    rotated_img = img.rotate(angle,expand=True)

    # Convert images to numpy arrays
    original_img_array = np.array(img)
    rotated_img_array = np.array(rotated_img)
    
    # Display original and rotated images side by side
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(img)
    plt.title('Original Image')
    plt.subplot(1, 2, 2)
    plt.imshow(rotated_img)
    plt.title('Rotated Image')

    return original_img_array, rotated_img_array

import unittest
from PIL import Image, ImageDraw
import numpy as np
import os

def create_dummy_image(image_path='test_image.png', size=(10, 10)):
    """
    Creates a dummy color image for testing.
    The image size is 10x10 pixels.
    """
    img = Image.new('RGB', size, color='white')
    draw = ImageDraw.Draw(img)

    # Draw small shapes
    draw.point((2, 2), fill='red')  # Red point
    draw.point((5, 5), fill='green')  # Green point
    draw.point((8, 8), fill='blue')  # Blue point

    img.save(image_path)

class TestCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        create_dummy_image()

    @classmethod
    def tearDownClass(cls):
        os.remove('test_image.png')

    def test_normal_functionality(self):
        original_img, rotated_img = f_3281('test_image.png', 45)
        self.assertIsInstance(original_img, np.ndarray)
        self.assertIsInstance(rotated_img, np.ndarray)

    def test_non_existent_file(self):
        with self.assertRaises(FileNotFoundError):
            f_3281('non_existent.png', 45)

    def test_zero_rotation(self):
        original_img, rotated_img = f_3281('test_image.png', 0)
        self.assertTrue(np.array_equal(original_img, rotated_img))

    def test_full_rotation(self):
        original_img, rotated_img = f_3281('test_image.png', 360)
        self.assertTrue(np.array_equal(original_img, rotated_img))

    def test_negative_angle(self):
        _, rotated_img = f_3281('test_image.png', -45)
        self.assertIsInstance(rotated_img, np.ndarray)

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