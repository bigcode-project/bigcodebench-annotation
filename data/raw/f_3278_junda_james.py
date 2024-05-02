from PIL import Image, ImageFilter
import cv2
import numpy as np
import os

def f_3278(img_path, blur_radius=5):
    """
    Open an RGB image from a specific path, apply a blur filter, convert it to grayscale, and then display both the original and the edited images side by side.
    Returns numpy arrays representing both the original and the processed images.

    Parameters:
    - img_path (str): The path of the image file.
    - blur_radius (int): The radius of the Gaussian blur filter. Default is 5.

    Returns:
    - tuple: A tuple containing two numpy arrays, the first representing the original image and 
             the second representing the blurred and grayscaled image.

    Raises:
    - FileNotFoundError: If the image file does not exist at the specified path.

    Requirements:
    - PIL
    - opencv-python
    - numpy
    - os

    Example:
    >>> image_path = 'sample.png'
    >>> create_dummy_image(image_path=image_path)
    >>> original, processed = f_3278(image_path)
    >>> os.remove(image_path)
    """
    if not os.path.exists(img_path):
        raise FileNotFoundError(f"No file found at {img_path}")

    img = Image.open(img_path)
    img = img.convert("RGB")

    blurred_img = img.filter(ImageFilter.GaussianBlur(blur_radius))
    grey_img = cv2.cvtColor(np.array(blurred_img), cv2.COLOR_RGB2GRAY)

    return np.array(img), np.array(grey_img)

import unittest
import numpy as np
from PIL import Image, ImageDraw

def create_dummy_image(image_path='test_image.jpg', size=(10, 10)):
    img = Image.new('RGB', size, color='white')
    draw = ImageDraw.Draw(img)
    draw.rectangle([2, 2, 8, 8], fill='black')
    img.save(image_path)

class TestCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        create_dummy_image()

    @classmethod
    def tearDownClass(cls):
        os.remove('test_image.jpg')

    def test_normal_functionality(self):
        original, processed = f_3278('test_image.jpg')
        self.assertIsInstance(original, np.ndarray)
        self.assertIsInstance(processed, np.ndarray)
        
        original_img_list = original.tolist()
        processed_img_list = processed.tolist()
        
        # self.assertTrue(np.array_equal(segmented_img_list, segment_expect), "The arrays should not be equal")
        
        with open('df_contents.txt', 'w') as file:
            file.write(str(processed_img_list))
            
        expect_original = [[[255, 255, 255], [252, 252, 252], [251, 251, 251], [255, 255, 255], [255, 255, 255], [255, 255, 255], [249, 249, 249], [249, 249, 249], [255, 255, 255], [247, 247, 247]], [[242, 242, 242], [255, 255, 255], [241, 241, 241], [255, 255, 255], [255, 255, 255], [250, 250, 250], [255, 255, 255], [255, 255, 255], [233, 233, 233], [255, 255, 255]], [[255, 255, 255], [237, 237, 237], [4, 4, 4], [0, 0, 0], [0, 0, 0], [0, 0, 0], [12, 12, 12], [0, 0, 0], [23, 23, 23], [250, 250, 250]], [[255, 255, 255], [255, 255, 255], [0, 0, 0], [5, 5, 5], [10, 10, 10], [3, 3, 3], [7, 7, 7], [0, 0, 0], [0, 0, 0], [255, 255, 255]], [[253, 253, 253], [255, 255, 255], [8, 8, 8], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [17, 17, 17], [11, 11, 11], [255, 255, 255]], [[255, 255, 255], [255, 255, 255], [2, 2, 2], [0, 0, 0], [12, 12, 12], [15, 15, 15], [0, 0, 0], [0, 0, 0], [0, 0, 0], [246, 246, 246]], [[254, 254, 254], [255, 255, 255], [4, 4, 4], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [3, 3, 3], [16, 16, 16], [254, 254, 254]], [[253, 253, 253], [255, 255, 255], [0, 0, 0], [0, 0, 0], [12, 12, 12], [0, 0, 0], [11, 11, 11], [0, 0, 0], [0, 0, 0], [249, 249, 249]], [[255, 255, 255], [250, 250, 250], [4, 4, 4], [0, 0, 0], [0, 0, 0], [7, 7, 7], [0, 0, 0], [7, 7, 7], [13, 13, 13], [241, 241, 241]], [[248, 248, 248], [255, 255, 255], [230, 230, 230], [255, 255, 255], [255, 255, 255], [255, 255, 255], [244, 244, 244], [249, 249, 249], [241, 241, 241], [255, 255, 255]]]
        
        expect_processed = [[190, 188, 187, 186, 185, 183, 182, 182, 182, 182], [189, 187, 185, 184, 183, 181, 180, 180, 180, 180], [187, 185, 184, 182, 181, 179, 178, 178, 178, 178], [185, 184, 182, 180, 179, 178, 177, 177, 177, 177], [184, 182, 181, 179, 178, 176, 175, 175, 175, 176], [183, 181, 179, 178, 177, 175, 174, 174, 174, 174], [182, 180, 178, 177, 176, 174, 173, 173, 173, 174], [182, 180, 178, 176, 175, 174, 173, 173, 173, 173], [182, 180, 178, 176, 175, 174, 173, 173, 173, 173], [182, 180, 178, 176, 176, 174, 173, 173, 173, 174]]
        self.assertTrue(np.array_equal(expect_processed, processed_img_list), "The arrays should not be equal")
        self.assertTrue(np.array_equal(expect_original, original_img_list), "The arrays should not be equal")

    def test_non_existent_file(self):
        with self.assertRaises(FileNotFoundError):
            f_3278('non_existent.jpg')

    def test_blur_effectiveness(self):
        _, processed = f_3278('test_image.jpg')
        self.assertNotEqual(np.mean(processed), 255)  # Ensuring it's not all white

    def test_returned_image_shapes(self):
        original, processed = f_3278('test_image.jpg')
        self.assertEqual(original.shape, (10, 10, 3))
        self.assertEqual(processed.shape, (10, 10))

    def test_different_blur_radius(self):
        _, processed_default = f_3278('test_image.jpg')
        _, processed_custom = f_3278('test_image.jpg', blur_radius=10)
        self.assertFalse(np.array_equal(processed_default, processed_custom))

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