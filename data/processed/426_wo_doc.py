import cv2
import os
from matplotlib import pyplot as plt

def task_func(image_path='image.jpg', histogram_path='histogram.png'):
    """
    Read an image, create a histogram of the image pixel intensities, save the histogram as a PNG file, 
    and return the histogram plot object. The function also displays the original image and its histogram.
    The limit to the size of the image depends on the hardware capabilities of the system you are working on. 
    A possible size of an image is 20x20. 

    Parameters:
    - image_path (str): Path to the image file. Defaults to 'image.jpg'.
    - histogram_path (str): Path to save the histogram PNG file. Defaults to 'histogram.png'.

    Returns:
    - matplotlib.axes.Axes: The Axes object of the histogram plot.

    Raises:
    - FileNotFoundError: If the image file does not exist at the specified path.

    Requirements:
    - opencv
    - os
    - matplotlib.pyplot

    Example:
    >>> create_dummy_image('image.jpg')
    >>> histogram_axes = task_func('image.jpg', 'histogram.png')
    >>> os.remove('histogram.png')
    >>> os.remove('image.jpg')
    >>> histogram_axes.title.get_text()
    'Grayscale Histogram'
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"No image found at {image_path}")
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    plt.figure()
    plt.title("Grayscale Histogram")
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")
    axes = plt.plot(hist)[0].axes
    plt.savefig(histogram_path)
    return axes

import unittest
import os
from PIL import Image, ImageDraw
import matplotlib
def create_dummy_image(image_path='test_image.jpg', size=(20, 20)):
    """
    Creates a dummy grayscale image for testing.
    The image size is 20x20 pixels.
    """
    img = Image.new('L', size, color='white')
    draw = ImageDraw.Draw(img)
    draw.rectangle([2, 2, 6, 6], fill='black')
    draw.line([2, 15, 18, 15], fill='black', width=1)
    img.save(image_path)
class TestCases(unittest.TestCase):
    def setUp(self):
        create_dummy_image()
    def tearDown(self):
        os.remove('test_image.jpg')
        if os.path.exists('histogram.png'):
            os.remove('histogram.png')
    def test_normal_functionality(self):
        histogram_axes = task_func('test_image.jpg', 'histogram.png')
        self.assertTrue(os.path.exists('histogram.png'))
        self.assertIsInstance(histogram_axes, matplotlib.axes.Axes)
        self.assertEqual(histogram_axes.title.get_text(), "Grayscale Histogram")
    def test_non_existent_file(self):
        with self.assertRaises(FileNotFoundError):
            task_func('non_existent.jpg')
    def test_histogram_labels(self):
        histogram_axes = task_func('test_image.jpg')
        self.assertEqual(histogram_axes.get_xlabel(), "Bins")
        self.assertEqual(histogram_axes.get_ylabel(), "# of Pixels")
    def test_histogram_output_type(self):
        histogram_axes = task_func('test_image.jpg')
        self.assertIsInstance(histogram_axes.get_lines()[0], matplotlib.lines.Line2D)
