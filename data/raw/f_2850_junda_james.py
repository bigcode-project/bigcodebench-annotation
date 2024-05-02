import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def f_2850(image_path):
    """
    Displays the color histogram of an image.

    Parameters:
    image_path (str): The path to the image.

    Returns:
    None

    Requirements:
    - cv2
    - numpy
    - PIL
    - matplotlib.pyplot

    Example:
    >>> f_2850('images/image.png')
    """
    image = cv2.imread(image_path)
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        histr = cv2.calcHist([image], [i], None, [256], [0,256])
        plt.plot(histr, color=col)
    plt.xlim([0,256])
    plt.show()
