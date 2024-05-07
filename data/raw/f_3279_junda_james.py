from PIL import Image
import cv2
import numpy as np
import os

def f_3279(img_path):
    """
    Open an RGB image, convert it to grayscale, find contours using the cv2 library, and return the original image and contours.

    Parameters:
    - img_path (str): The path of the image file.

    Returns:
    - tuple: A tuple containing the original image as a numpy array and a list of contours.

    Raises:
    - FileNotFoundError: If the image file does not exist at the specified path.

    Requirements:
    - PIL
    - opencv-python
    - numpy
    - os

    Example:
    >>> img_path = 'sample.png'
    >>> create_dummy_image(image_path=img_path)
    >>> img, contours = f_3279(img_path)
    >>> os.remove(img_path)
    """
    if not os.path.exists(img_path):
        raise FileNotFoundError(f"No file found at {img_path}")
    
    img = cv2.imread(img_path)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Find contours
    contours, _ = cv2.findContours(gray_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    return np.array(img), contours

import unittest
import numpy as np
from PIL import Image, ImageDraw
import os
            
            
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
        img, contours = f_3279('test_image.jpg')
        self.assertIsInstance(img, np.ndarray)
        self.assertTrue(isinstance(contours, tuple) and len(contours) > 0)
        with open("filename", 'w') as file:
            # Convert the image array to a list and save
            file.write("# Image Array\n")
            image_list = img.tolist()
            file.write(f"{image_list}\n")
            
            # Save the contours
            file.write("\n# Contours\n")
            for contour in contours:
                # Convert each contour array to a list
                contour_list = contour.tolist()
                file.write(f"{contour_list}\n")
        
        expect_img = [[[255, 255, 255], [252, 252, 252], [251, 251, 251], [255, 255, 255], [255, 255, 255], [255, 255, 255], [249, 249, 249], [249, 249, 249], [255, 255, 255], [247, 247, 247]], [[242, 242, 242], [255, 255, 255], [241, 241, 241], [255, 255, 255], [255, 255, 255], [250, 250, 250], [255, 255, 255], [255, 255, 255], [233, 233, 233], [255, 255, 255]], [[255, 255, 255], [237, 237, 237], [4, 4, 4], [0, 0, 0], [0, 0, 0], [0, 0, 0], [12, 12, 12], [0, 0, 0], [23, 23, 23], [250, 250, 250]], [[255, 255, 255], [255, 255, 255], [0, 0, 0], [5, 5, 5], [10, 10, 10], [3, 3, 3], [7, 7, 7], [0, 0, 0], [0, 0, 0], [255, 255, 255]], [[253, 253, 253], [255, 255, 255], [8, 8, 8], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [17, 17, 17], [11, 11, 11], [255, 255, 255]], [[255, 255, 255], [255, 255, 255], [2, 2, 2], [0, 0, 0], [12, 12, 12], [15, 15, 15], [0, 0, 0], [0, 0, 0], [0, 0, 0], [246, 246, 246]], [[254, 254, 254], [255, 255, 255], [4, 4, 4], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [3, 3, 3], [16, 16, 16], [254, 254, 254]], [[253, 253, 253], [255, 255, 255], [0, 0, 0], [0, 0, 0], [12, 12, 12], [0, 0, 0], [11, 11, 11], [0, 0, 0], [0, 0, 0], [249, 249, 249]], [[255, 255, 255], [250, 250, 250], [4, 4, 4], [0, 0, 0], [0, 0, 0], [7, 7, 7], [0, 0, 0], [7, 7, 7], [13, 13, 13], [241, 241, 241]], [[248, 248, 248], [255, 255, 255], [230, 230, 230], [255, 255, 255], [255, 255, 255], [255, 255, 255], [244, 244, 244], [249, 249, 249], [241, 241, 241], [255, 255, 255]]]
        
        expect_contours = [[[[0, 0]], [[0, 9]], [[9, 9]], [[9, 0]]],
                            [[[5, 8]], [[6, 7]], [[7, 8]], [[6, 9]]],
                            [[[6, 7]], [[7, 6]], [[8, 6]], [[9, 7]], [[8, 8]], [[7, 8]]],
                            [[[2, 4]], [[3, 3]], [[6, 3]], [[7, 4]], [[8, 4]], [[9, 5]], [[8, 6]], [[7, 6]], [[5, 8]], [[4, 7]], [[5, 8]], [[4, 9]], [[3, 9]], [[1, 7]], [[2, 6]]],
                            [[[4, 5]], [[5, 5]]],
                            [[[1, 3]], [[2, 2]], [[3, 3]], [[2, 4]]],
                            [[[6, 2]], [[7, 1]], [[9, 3]], [[8, 4]], [[7, 4]], [[6, 3]]],
                            [[[2, 2]], [[3, 1]], [[5, 1]], [[6, 2]], [[5, 3]], [[3, 3]]]]
        
        self.assertTrue(np.array_equal(expect_img, img), "The arrays should not be equal")
        
        for i in range(len(contours)):
            self.assertTrue(np.array_equal(contours[i], expect_contours[i]), "The arrays should not be equal")
        



    def test_non_existent_file(self):
        with self.assertRaises(FileNotFoundError):
            f_3279('non_existent.jpg')

    def test_image_shape(self):
        img, _ = f_3279('test_image.jpg')
        self.assertEqual(img.shape, (10, 10, 3))

    def test_contours_output_type(self):
        _, contours = f_3279('test_image.jpg')
        self.assertIsInstance(contours, tuple)

    def test_invalid_img_path_type(self):
        with self.assertRaises(FileNotFoundError):
            f_3279(123)  # Passing a non-string path

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