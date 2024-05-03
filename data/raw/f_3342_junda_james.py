import numpy as np
import cv2
import os

def f_3342(image_path='image.jpg', threshold=128):
    """
    Read an RGB image, convert it to grayscale, binarize it using a given threshold, and return both the original and binarized images as numpy arrays.
    The function checks for the existence of the image file and validates the threshold value.

    Parameters:
    - image_path (str): Path to the image file. Defaults to 'image.jpg'.
    - threshold (int): Threshold value for binarization. Must be an integer in the range 0-255. Defaults to 128.

    Returns:
    - tuple: A tuple containing two numpy arrays. The first array represents the original grayscale image,
             and the second array represents the binarized image.

    Raises:
    - FileNotFoundError: If the image file does not exist at the specified path.
    - ValueError: If the threshold is not an integer or not in the range 0-255.

    Requirements:
    - opencv
    - numpy
    - os
    - PIL

    Example:
    >>> img_path = 'image.jpg'
    >>> create_dummy_image(img_path)
    >>> original_img_array, binary_img_array = f_3342(img_path, 128)
    >>> os.remove(img_path)
    >>> original_img_array.shape, binary_img_array.shape # ((image_height, image_width), (image_height, image_width))
    ((20, 20), (20, 20))
    """

    if not isinstance(threshold, int) or not (0 <= threshold <= 255):
        raise ValueError("Threshold must be an integer between 0 and 255.")

    if not os.path.exists(image_path):
        raise FileNotFoundError(f"No image found at {image_path}")

    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    binary_img = np.where(img > threshold, 255, 0).astype('uint8')

    return np.array(img), binary_img

import unittest
import os
from PIL import Image, ImageDraw

def create_dummy_image(image_path='test_image.jpg', size=(20, 20)):
    """
    Creates a dummy grayscale image for testing.
    The image size is 20x20 pixels.
    """
    img = Image.new('L', size, color='white')
    draw = ImageDraw.Draw(img)
    draw.rectangle([5, 5, 15, 15], fill='black')
    img.save(image_path)

class TestCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        create_dummy_image()

    @classmethod
    def tearDownClass(cls):
        os.remove('test_image.jpg')

    def test_normal_functionality(self):
        original_img, binary_img = f_3342('test_image.jpg', 10)
        self.assertIsInstance(original_img, np.ndarray)
        self.assertIsInstance(binary_img, np.ndarray)
        self.assertEqual(binary_img.max(), 255)
        self.assertEqual(binary_img.min(), 0)

    def test_non_existent_file(self):
        with self.assertRaises(FileNotFoundError):
            f_3342('non_existent.jpg')

    def test_invalid_threshold_non_integer(self):
        with self.assertRaises(ValueError):
            f_3342('test_image.jpg', 'invalid')

    def test_invalid_threshold_out_of_range(self):
        with self.assertRaises(ValueError):
            f_3342('test_image.jpg', -10)

    def test_threshold_effect(self):
        _, binary_img_high_threshold = f_3342('test_image.jpg', 200)
        self.assertEqual(np.sum(binary_img_high_threshold), 71145)

    def test_binary_output_values(self):
        _, binary_img = f_3342('test_image.jpg', 128)
        unique_values = np.unique(binary_img)
        self.assertTrue(np.array_equal(unique_values, [0, 255]))

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