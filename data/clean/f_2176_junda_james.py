import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

def f_2176(image, sigma=2):
    """
    Apply a Gaussian filter to a given image and draw the original and filtered images side by side.

    Parameters:
    - image (numpy.ndarray): The input image to apply the filter on.
    - sigma (float, optional): The sigma value for the Gaussian filter. Default is 2.

    Returns:
    - ax (matplotlib.axes.Axes): Axes object containing the plot. Two plots with titles 'Original' and 'Filtered'. 
    - filtered_image (numpy.ndarray): The numpy array of pixel values for the filtered image.

    Raises:
    - ValueError: If sigma is non-positive.
    - TypeError: If the input is not a numpy array.

    Requirements:
    - numpy
    - matplotlib.pyplot
    - scipy.ndimage

    Example:
    >>> from skimage import data
    >>> ax, filtered_image = f_2176(data.coins())
    >>> ax[0].get_title()  # Checking the title of the first subplot
    'Original'
    >>> ax[1].get_title()  # Checking the title of the second subplot
    'Filtered'
    """
    if not isinstance(image, np.ndarray):
        raise TypeError("The image must be a numpy array.")
    if sigma <= 0:
        raise ValueError("Sigma must be positive.")

    filtered_image = gaussian_filter(image, sigma=sigma)

    fig, ax = plt.subplots(1, 2, figsize=(10, 5))

    ax[0].imshow(image, cmap=plt.cm.gray)
    ax[0].set_title('Original')

    ax[1].imshow(filtered_image, cmap=plt.cm.gray)
    ax[1].set_title('Filtered')

    return ax, filtered_image

import unittest
from skimage import data
import numpy as np

class TestCases(unittest.TestCase):
    def test_return_types(self):
        image = data.coins()
        ax, filtered_image = f_2176(image)
        self.assertIsInstance(ax, np.ndarray, "ax is not a numpy array")
        self.assertIsInstance(filtered_image, np.ndarray, "filtered_image is not a numpy array")

    def test_error_on_non_positive_sigma(self):
        image = data.coins()
        with self.assertRaises(ValueError):
            f_2176(image, sigma=0)

    def test_error_on_invalid_image_type(self):
        invalid_image = "not an image"
        with self.assertRaises(TypeError):
            f_2176(invalid_image)

    def test_subplot_titles(self):
        image = data.coins()
        ax, _ = f_2176(image)
        self.assertEqual(ax[0].get_title(), 'Original', "Title of the first subplot is incorrect")
        self.assertEqual(ax[1].get_title(), 'Filtered', "Title of the second subplot is incorrect")

    def test_filtered_image_difference(self):
        image = data.coins()
        _, filtered_image = f_2176(image)
        expect = gaussian_filter(image, sigma=2)
        self.assertFalse(np.array_equal(image, filtered_image), "Filtered image is not different from the original")
        self.assertEqual(expect.tolist(), filtered_image.tolist(), "Filtered image is not different from the original")

    def test_sigma_blurring_effect(self):
        image = data.coins()
        _, filtered_image = f_2176(image, sigma=2)
        _, filtered_image_high_sigma = f_2176(image, sigma=5)
        diff_original = np.sum(np.abs(image - filtered_image))
        diff_high_sigma = np.sum(np.abs(image - filtered_image_high_sigma))
        self.assertGreater(diff_high_sigma, diff_original, "Higher sigma does not increase blurring")

    def test_different_images(self):
        images = [data.coins(), data.camera(), data.astronaut()]
        for img in images:
            _, filtered_image = f_2176(img)
            self.assertEqual(filtered_image.shape, img.shape, "Filtered image shape does not match original image shape")

# Running the tests
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