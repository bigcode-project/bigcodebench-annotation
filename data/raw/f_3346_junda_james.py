import numpy as np
import cv2
import os

def f_3346(image_path='image.jpg', threshold=128):
    """
    Read an image, convert it to grayscale, binarize it using a given threshold, and save it as 'binary_image.jpg'.
    The function returns numpy arrays of the original and binarized images, and ensures that the threshold value is valid.

    Parameters:
    - image_path (str): The path to the image file. Default is 'image.jpg'.
    - threshold (int): The threshold value for binarization, must be between 0 and 255. Default is 128.

    Returns:
    - tuple: A tuple containing two numpy arrays; the first is the original grayscale image, the second is the binarized image.

    Raises:
    - FileNotFoundError: If the image file does not exist at the specified path.
    - ValueError: If the threshold is not an integer or not in the range 0-255.

    Requirements:
    - opencv
    - numpy
    - os
    - pillow

    Example:
    >>> create_dummy_image('image.jpg')
    >>> original_img_array, binary_img_array = f_3346('image.jpg', 128)
    >>> os.remove('image.jpg')
    >>> original_img_array.shape, binary_img_array.shape # ((image_height, image_width), (image_height, image_width))
    ((20, 20), (20, 20))
    """

    if not isinstance(threshold, int) or not (0 <= threshold <= 255):
        raise ValueError("Threshold must be an integer between 0 and 255.")

    if not os.path.exists(image_path):
        raise FileNotFoundError(f"No image found at {image_path}")

    # Image processing
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    binary_img = np.where(img >= threshold, 255, 0).astype('uint8')
    cv2.imwrite('binary_image.jpg', binary_img)

    return np.array(img), np.array(binary_img)

# Additional libraries required for test cases
import unittest
from PIL import Image, ImageDraw

# Updated test cases and dummy image creation function will be provided below.
def create_dummy_image(image_path='test_image.jpg', size=(20, 20)):
    """
    Creates a dummy grayscale image with basic shapes for testing.
    The image size is 20x20 pixels.
    """
    img = Image.new('L', size, color='white')
    draw = ImageDraw.Draw(img)
    draw.rectangle([2, 2, 6, 6], fill='black')
    draw.ellipse([10, 2, 14, 6], fill='gray')
    draw.line([2, 15, 18, 15], fill='black', width=1)
    img.save(image_path)

class TestCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        create_dummy_image()

    @classmethod
    def tearDownClass(cls):
        os.remove('test_image.jpg')
        if os.path.exists('binary_image.jpg'):
            os.remove('binary_image.jpg')

    def test_normal_functionality(self):
        original_img, binary_img = f_3346('test_image.jpg', 126)
        self.assertTrue(os.path.exists('binary_image.jpg'))
        self.assertIsInstance(original_img, np.ndarray)
        self.assertIsInstance(binary_img, np.ndarray)
        self.assertEqual(original_img.shape, (20, 20))
        self.assertEqual(binary_img.shape, (20, 20))

        # Additional checks to ensure binarization is correct
        unique_values = np.unique(binary_img)
        self.assertTrue(np.array_equal(unique_values, [0, 255]))

    def test_non_existent_file(self):
        with self.assertRaises(FileNotFoundError):
            f_3346('non_existent.jpg')

    def test_invalid_threshold_non_integer(self):
        with self.assertRaises(ValueError):
            f_3346('test_image.jpg', 'invalid')

    def test_invalid_threshold_out_of_range(self):
        with self.assertRaises(ValueError):
            f_3346('test_image.jpg', -10)

    def test_normal_functionality1(self):
        original_img, binary_img = f_3346('test_image.jpg', 126)
        original_img_list = original_img.tolist()
        binary_img_list = binary_img.tolist()
        expect_original = [[255, 248, 255, 250, 246, 255, 255, 251, 240, 255, 255, 253, 255, 252, 255, 254, 255, 255, 255, 255], [240, 248, 246, 255, 255, 249, 240, 253, 255, 255, 240, 255, 245, 252, 255, 255, 255, 255, 255, 255], [255, 255, 2, 0, 0, 11, 2, 255, 255, 243, 254, 135, 112, 128, 255, 246, 255, 255, 255, 255], [250, 246, 0, 16, 0, 0, 0, 252, 248, 255, 133, 117, 143, 130, 124, 250, 255, 255, 255, 255], [255, 255, 12, 0, 4, 0, 7, 252, 255, 251, 132, 127, 124, 120, 134, 255, 255, 255, 255, 255], [253, 242, 0, 3, 0, 6, 5, 255, 255, 245, 120, 129, 138, 127, 123, 252, 255, 255, 255, 255], [255, 255, 5, 0, 0, 18, 0, 250, 255, 255, 255, 122, 128, 131, 253, 253, 255, 255, 255, 255], [254, 247, 255, 252, 255, 250, 253, 255, 239, 255, 253, 249, 255, 255, 255, 252, 255, 255, 255, 255], [255, 244, 255, 255, 249, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 249, 249, 255], [255, 255, 244, 255, 255, 255, 252, 247, 255, 255, 255, 255, 255, 255, 255, 255, 255, 249, 249, 255], [250, 255, 243, 255, 250, 248, 246, 255, 253, 253, 253, 253, 253, 253, 253, 253, 248, 255, 255, 255], [243, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 241, 254], [255, 242, 255, 244, 243, 254, 251, 241, 255, 255, 255, 255, 255, 255, 255, 255, 255, 243, 255, 255], [254, 242, 255, 255, 251, 255, 255, 255, 253, 253, 253, 253, 253, 253, 253, 253, 246, 240, 255, 250], [248, 255, 230, 255, 255, 255, 244, 249, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 239, 255], [255, 250, 4, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 245], [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255], [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255], [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255], [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]]
        expect_binary = [[255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255], [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255], [255, 255, 0, 0, 0, 0, 0, 255, 255, 255, 255, 255, 0, 255, 255, 255, 255, 255, 255, 255], [255, 255, 0, 0, 0, 0, 0, 255, 255, 255, 255, 0, 255, 255, 0, 255, 255, 255, 255, 255], [255, 255, 0, 0, 0, 0, 0, 255, 255, 255, 255, 255, 0, 0, 255, 255, 255, 255, 255, 255], [255, 255, 0, 0, 0, 0, 0, 255, 255, 255, 0, 255, 255, 255, 0, 255, 255, 255, 255, 255], [255, 255, 0, 0, 0, 0, 0, 255, 255, 255, 255, 0, 255, 255, 255, 255, 255, 255, 255, 255], [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255], [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255], [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255], [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255], [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255], [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255], [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255], [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255], [255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255], [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255], [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255], [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255], [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]]
        # with open('df_contents.txt', 'w') as file:
        #     file.write(str(original_img_list))

        self.assertTrue(np.array_equal(original_img_list, expect_original), "The arrays should be equal")

        # Check if array1 is not equal to array3 (they are not)
        self.assertTrue(np.array_equal(binary_img_list, expect_binary), "The arrays should not be equal")

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