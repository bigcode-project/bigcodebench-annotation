from PIL import Image
import numpy as np
from skimage.transform import resize
import matplotlib.pyplot as plt
import os

def f_2221(img_path, scale_factors=[0.5, 0.75, 1.5, 2.0]):
    """
    Open an image file and scale it by different scaling factors.
    Display each scaled image using matplotlib and return the scaled images with their Axes.

    Parameters:
    img_path (str): Path to the image file.
    scale_factors (list): List of scaling factors to apply. Default is [0.5, 0.75, 1.5, 2.0].

    Returns:
    list of tuples: Each tuple contains (matplotlib.axes.Axes, numpy.ndarray) representing the Axes and the pixel values of the scaled image.

    Raises:
    FileNotFoundError: If the image file cannot be found.

    Requirements:
    - PIL
    - numpy
    - scikit-image
    - matplotlib.pyplot
    - os

    Example:
    >>> dummy_img_path = "sample.png"
    >>> Image.fromarray(np.random.randint(0, 255, (20, 20, 3), dtype=np.uint8)).save(dummy_img_path)
    >>> result = f_2221('sample.png')
    >>> os.remove(dummy_img_path)
    >>> for ax, img in result:
    ...     print(ax.get_title(), img.shape)
    Scale factor: 0.5 (10, 10, 3)
    Scale factor: 0.75 (15, 15, 3)
    Scale factor: 1.5 (30, 30, 3)
    Scale factor: 2.0 (40, 40, 3)
    """
    if not os.path.exists(img_path):
        raise FileNotFoundError(f"No file found at {img_path}")

    im = Image.open(img_path)
    img_arr = np.array(im)
    results = []

    for scale_factor in scale_factors:
        scaled_img_arr = resize(img_arr, (int(im.height * scale_factor), int(im.width * scale_factor)),
                                mode='reflect', anti_aliasing=True)
        fig, ax = plt.subplots()
        ax.imshow(scaled_img_arr)
        ax.set_title(f'Scale factor: {scale_factor}')
        results.append((ax, scaled_img_arr))
    # plt.show()
    return results

import unittest
from PIL import Image
import numpy as np

class TestCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create a dummy image for testing
        cls.dummy_img_path = "test_image.png"
        Image.fromarray(np.random.randint(0, 255, (20, 20, 3), dtype=np.uint8)).save(cls.dummy_img_path)

    @classmethod
    def tearDownClass(cls):
        # Cleanup the dummy image
        os.remove(cls.dummy_img_path)

    def test_scale_factors(self):
        results = f_2221(self.dummy_img_path)
        self.assertEqual(len(results), 4)  # Check for 4 scale factors

    def test_return_type(self):
        results = f_2221(self.dummy_img_path)
        for ax, img in results:
            self.assertIsInstance(ax, plt.Axes)
            self.assertIsInstance(img, np.ndarray)

    def test_scale_factor_effect(self):
        original_image = Image.open(self.dummy_img_path)
        original_size = original_image.size
        results = f_2221(self.dummy_img_path)
        for _, img in results:
            self.assertNotEqual(img.shape[:2], original_size)  # Scaled image should differ in size

    def test_invalid_path(self):
        with self.assertRaises(FileNotFoundError):
            f_2221("nonexistent.png")

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