import cv2
import numpy as np
import matplotlib.pyplot as plt

def f_2505(image_path, kernel_size):
    """
    Applies a blur effect to an image using a specified kernel size, then visualizes both the original and blurred images side by side.

    Parameters:
    - image_path (str): The file path to the input image.
    - kernel_size (int): The size of the kernel used for blurring. Must be a positive integer.

    Returns:
    - tuple: A tuple containing a numpy.ndarray of the blurred image, and two matplotlib.axes.Axes objects for the plots of the original and blurred images.

    Raises:
    - FileNotFoundError: If the specified image file does not exist.
    - ValueError: If kernel_size is not a positive integer.

    Requirements:
    - opencv-python (cv2) for image processing.
    - numpy for array operations.
    - matplotlib.pyplot for plotting images.

    Example:
    >>> dummy_img_path = "image.jpg"
    >>> np.random.seed(42)
    >>> dummy_img = np.random.randint(0, 255, (20, 20, 3), dtype=np.uint8)
    >>> cv2.imwrite(dummy_img_path, dummy_img)
    True
    >>> blurred_img, ax_original, ax_blurred = f_2505('image.jpg', 5) # The function returns the blurred image array, and axes objects with titles 'Original' and 'Blurred' for the original and blurred images, respectively.
    >>> os.remove(dummy_img_path)
    """
    if kernel_size <= 0 or not isinstance(kernel_size, int):
        raise ValueError("kernel_size must be a positive integer")
    
    try:
        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError(f"No image found at {image_path}")
    except FileNotFoundError as e:
        raise e

    blurred_image = cv2.blur(image, (kernel_size, kernel_size))

    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), ax1.set_title('Original')
    ax1.set_xticks([]), ax1.set_yticks([])
    ax2.imshow(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB)), ax2.set_title('Blurred')
    ax2.set_xticks([]), ax2.set_yticks([])
    # plt.show()

    return blurred_image, ax1, ax2

import unittest
import os
import numpy as np

class TestCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create a dummy image for testing
        cls.dummy_img_path = "test_image.jpg"
        np.random.seed(42)
        dummy_img = np.random.randint(0, 255, (20, 20, 3), dtype=np.uint8)
        cv2.imwrite(cls.dummy_img_path, dummy_img)

    @classmethod
    def tearDownClass(cls):
        # Cleanup the dummy image
        os.remove(cls.dummy_img_path)

    def test_valid_input(self):
        blurred_image, ax_original, ax_blurred = f_2505(self.dummy_img_path, 3)
        self.assertEqual(blurred_image.shape, (20, 20, 3))
        self.assertEqual(ax_original.get_title(), 'Original')
        self.assertEqual(ax_blurred.get_title(), 'Blurred')
        expect = [[[96, 163, 136], [121, 170, 146], [126, 141, 127], [130, 126, 132], [118, 119, 140], [114, 132, 146], [105, 135, 124], [120, 153, 115], [84, 110, 67], [125, 141, 83], [145, 151, 81], [195, 187, 113], [207, 184, 125], [199, 161, 118], [187, 149, 114], [130, 116, 86], [93, 111, 92], [79, 103, 109], [106, 108, 145], [109, 94, 147]], [[89, 156, 146], [115, 164, 156], [128, 145, 144], [134, 134, 145], [113, 120, 136], [101, 129, 134], [95, 139, 121], [121, 167, 128], [101, 133, 86], [125, 137, 79], [141, 134, 69], [180, 155, 93], [193, 154, 110], [190, 141, 115], [177, 133, 116], [151, 131, 120], [113, 124, 121], [108, 133, 143], [111, 128, 154], [120, 129, 163]], [[95, 157, 169], [101, 146, 163], [121, 134, 158], [120, 118, 141], [113, 123, 136], [97, 135, 131], [85, 145, 125], [101, 162, 129], [100, 139, 100], [129, 131, 86], [149, 119, 74], [195, 141, 104], [204, 140, 122], [198, 137, 135], [171, 122, 129], [152, 125, 139], [117, 115, 135], [104, 127, 143], [90, 131, 137], [97, 144, 145]], [[104, 150, 159], [101, 129, 148], [119, 113, 149], [123, 100, 137], [123, 109, 133], [97, 114, 123], [75, 120, 119], [93, 144, 135], [109, 140, 119], [128, 124, 95], [140, 104, 75], [170, 111, 94], [179, 112, 109], [181, 125, 128], [159, 122, 125], [168, 149, 154], [129, 125, 137], [115, 132, 139], [77, 118, 109], [78, 131, 113]], [[127, 151, 135], [117, 122, 122], [136, 104, 133], [143, 90, 133], [154, 106, 145], [147, 123, 157], [113, 113, 146], [101, 116, 140], [111, 125, 131], [119, 119, 109], [141, 121, 107], [155, 115, 108], [171, 125, 124], [166, 131, 123], [158, 142, 121], [151, 149, 123], [123, 127, 109], [90, 100, 87], [72, 93, 76], [60, 86, 66]], [[126, 130, 98], [122, 109, 93], [138, 93, 107], [156, 91, 124], [159, 95, 134], [153, 98, 146], [113, 71, 128], [118, 99, 145], [113, 119, 137], [119, 132, 129], [124, 125, 120], [118, 101, 104], [140, 115, 119], [150, 131, 123], [168, 164, 137], [157, 167, 128], [114, 128, 90], [82, 93, 62], [84, 89, 61], [83, 86, 59]], [[121, 110, 90], [132, 112, 99], [154, 118, 121], [167, 121, 134], [157, 108, 129], [160, 107, 146], [132, 79, 134], [125, 98, 142], [108, 118, 133], [106, 131, 130], [127, 138, 143], [116, 107, 123], [136, 120, 135], [126, 112, 118], [154, 146, 140], [144, 149, 129], [118, 132, 103], [87, 102, 66], [110, 116, 75], [118, 118, 75]], [[127, 102, 109], [126, 103, 108], [127, 108, 109], [127, 115, 110], [118, 108, 105], [112, 90, 104], [103, 72, 104], [110, 96, 128], [98, 116, 131], [104, 132, 142], [121, 132, 150], [121, 114, 136], [134, 124, 139], [136, 124, 134], [157, 143, 152], [144, 138, 140], [116, 124, 110], [107, 121, 89], [134, 141, 97], [147, 149, 100]], [[110, 71, 99], [119, 90, 110], [110, 106, 107], [108, 126, 110], [93, 116, 96], [106, 116, 107], [112, 108, 116], [116, 116, 137], [102, 118, 142], [92, 111, 141], [124, 130, 164], [122, 121, 144], [137, 139, 144], [120, 116, 116], [143, 126, 135], [133, 116, 125], [136, 133, 128], [127, 132, 109], [147, 148, 114], [137, 133, 97]], [[139, 90, 123], [136, 105, 125], [103, 107, 103], [92, 126, 99], [87, 127, 92], [100, 124, 97], [126, 129, 121], [133, 128, 142], [138, 140, 171], [113, 117, 162], [119, 120, 168], [108, 117, 144], [129, 149, 149], [137, 142, 135], [160, 136, 144], [139, 105, 118], [133, 116, 116], [130, 128, 115], [143, 137, 122], [148, 136, 122]], [[116, 68, 91], [140, 109, 120], [124, 128, 114], [120, 152, 115], [97, 132, 88], [108, 123, 90], [136, 127, 114], [147, 128, 137], [158, 146, 173], [126, 119, 164], [122, 119, 171], [98, 111, 147], [109, 136, 146], [108, 118, 119], [139, 110, 123], [142, 102, 120], [145, 126, 134], [131, 131, 130], [135, 128, 130], [135, 119, 126]], [[153, 109, 125], [160, 128, 136], [152, 145, 133], [133, 147, 114], [124, 142, 100], [114, 120, 87], [141, 133, 121], [142, 130, 136], [161, 153, 171], [136, 126, 159], [128, 112, 160], [116, 112, 156], [117, 130, 156], [120, 128, 141], [128, 115, 128], [133, 117, 132], [124, 129, 141], [119, 133, 147], [114, 116, 135], [117, 108, 131]], [[125, 89, 104], [130, 101, 111], [156, 139, 135], [145, 140, 120], [140, 141, 112], [116, 122, 99], [121, 130, 123], [129, 139, 145], [153, 158, 170], [158, 147, 169], [154, 127, 162], [140, 113, 155], [120, 107, 142], [109, 110, 131], [101, 111, 121], [113, 136, 145], [113, 149, 165], [107, 140, 163], [106, 123, 146], [94, 99, 121]], [[147, 124, 133], [135, 116, 120], [149, 138, 131], [138, 130, 117], [147, 142, 131], [138, 140, 140], [130, 142, 152], [124, 137, 152], [138, 140, 153], [164, 149, 162], [158, 131, 151], [149, 119, 148], [117, 93, 125], [117, 112, 135], [103, 121, 132], [97, 136, 145], [89, 137, 154], [84, 126, 143], [102, 132, 136], [93, 116, 112]], [[148, 142, 136], [139, 138, 124], [153, 160, 135], [143, 149, 130], [131, 129, 131], [115, 110, 133], [95, 93, 122], [106, 101, 125], [137, 124, 139], [182, 166, 173], [161, 147, 152], [138, 124, 136], [101, 86, 106], [123, 113, 133], [119, 125, 140], [113, 136, 152], [93, 125, 142], [78, 111, 115], [102, 133, 111], [102, 131, 94]], [[146, 157, 132], [140, 157, 122], [132, 158, 112], [133, 154, 123], [122, 129, 132], [121, 115, 143], [112, 101, 131], [109, 98, 116], [120, 110, 117], [148, 142, 139], [135, 133, 126], [128, 124, 122], [98, 89, 95], [124, 113, 122], [120, 116, 124], [123, 125, 140], [112, 118, 137], [105, 114, 118], [113, 125, 95], [123, 137, 88]], [[132, 150, 117], [128, 153, 110], [132, 165, 112], [133, 164, 127], [122, 139, 136], [111, 114, 132], [110, 106, 121], [111, 111, 113], [122, 128, 121], [135, 144, 129], [126, 128, 110], [122, 113, 101], [115, 102, 99], [138, 129, 126], [134, 134, 128], [135, 137, 140], [127, 122, 140], [121, 109, 122], [114, 102, 89], [113, 103, 74]], [[99, 103, 82], [110, 124, 94], [109, 142, 104], [124, 164, 136], [132, 164, 160], [139, 153, 164], [150, 152, 158], [132, 134, 127], [118, 128, 111], [125, 138, 112], [137, 140, 113], [140, 129, 112], [135, 119, 114], [124, 120, 114], [120, 133, 118], [108, 125, 114], [126, 129, 135], [126, 112, 128], [120, 98, 108], [114, 92, 95]], [[112, 86, 90], [121, 113, 110], [110, 139, 127], [117, 168, 159], [115, 162, 167], [125, 147, 162], [129, 127, 139], [125, 111, 109], [117, 107, 90], [130, 131, 100], [144, 149, 116], [147, 143, 124], [140, 129, 127], [113, 114, 113], [104, 129, 116], [82, 117, 96], [112, 133, 123], [111, 111, 119], [126, 113, 135], [103, 87, 115]], [[106, 64, 81], [117, 98, 110], [101, 128, 130], [117, 173, 175], [124, 177, 187], [133, 158, 177], [142, 136, 154], [133, 108, 113], [122, 99, 84], [136, 130, 97], [160, 165, 130], [156, 157, 137], [140, 132, 131], [88, 91, 94], [95, 125, 116], [68, 111, 88], [113, 145, 125], [107, 118, 118], [124, 120, 145], [109, 100, 137]]]
        # expect = [[[87, 170, 125], [114, 178, 133], [126, 148, 114], [116, 125, 138], [91, 112, 163], [95, 128, 162], [104, 138, 121], [127, 158, 104], [90, 112, 62], [136, 137, 87], [162, 146, 82], [208, 187, 109], [199, 187, 124], [181, 161, 126], [193, 146, 119], [140, 111, 93], [103, 108, 94], [61, 105, 112], [93, 110, 146], [91, 99, 144]], [[78, 161, 140], [107, 171, 146], [130, 152, 129], [131, 135, 145], [103, 114, 152], [98, 124, 147], [102, 139, 119], [129, 171, 119], [102, 135, 82], [129, 136, 81], [154, 132, 67], [193, 156, 89], [189, 156, 110], [175, 141, 124], [177, 130, 122], [154, 129, 123], [116, 124, 119], [89, 136, 145], [99, 127, 160], [105, 128, 169]], [[77, 153, 181], [88, 146, 166], [124, 141, 144], [135, 122, 127], [136, 121, 131], [122, 131, 130], [101, 144, 122], [100, 164, 126], [87, 141, 100], [117, 134, 84], [150, 122, 65], [205, 144, 94], [209, 139, 122], [195, 131, 148], [165, 116, 144], [147, 124, 143], [109, 119, 129], [86, 131, 142], [76, 127, 149], [82, 138, 164]], [[90, 141, 182], [92, 123, 161], [130, 114, 143], [150, 102, 123], [151, 111, 118], [116, 117, 111], [77, 123, 113], [82, 144, 139], [91, 137, 131], [113, 125, 97], [135, 111, 62], [173, 119, 77], [186, 112, 107], [187, 116, 142], [162, 114, 138], [167, 147, 157], [123, 131, 128], [102, 136, 135], [67, 117, 115], [68, 127, 124]], [[123, 140, 157], [119, 113, 138], [154, 98, 138], [166, 88, 127], [166, 110, 133], [143, 131, 144], [97, 119, 142], [86, 113, 151], [100, 117, 150], [113, 116, 115], [136, 128, 94], [150, 125, 91], [170, 127, 119], [172, 125, 132], [171, 137, 126], [157, 146, 127], [123, 130, 103], [84, 104, 83], [69, 98, 69], [60, 92, 59]], [[132, 121, 114], [131, 101, 106], [155, 86, 114], [167, 90, 123], [155, 97, 130], [143, 101, 145], [105, 70, 134], [121, 93, 155], [121, 111, 147], [125, 129, 129], [124, 128, 114], [111, 105, 98], [130, 118, 117], [142, 133, 122], [171, 166, 132], [154, 165, 131], [112, 127, 91], [80, 95, 60], [92, 95, 49], [97, 94, 42]], [[130, 103, 101], [142, 107, 106], [167, 116, 120], [168, 124, 127], [148, 110, 129], [151, 103, 157], [133, 71, 149], [141, 90, 151], [131, 114, 132], [125, 131, 124], [135, 137, 141], [112, 106, 128], [121, 122, 137], [104, 120, 111], [135, 155, 129], [122, 153, 129], [105, 132, 108], [86, 102, 68], [127, 116, 70], [142, 119, 68]], [[134, 95, 120], [133, 100, 111], [133, 114, 95], [125, 125, 92], [109, 113, 100], [101, 87, 115], [100, 64, 119], [126, 90, 135], [130, 112, 127], [136, 130, 134], [135, 131, 146], [118, 113, 141], [117, 123, 145], [110, 129, 135], [131, 150, 148], [118, 143, 139], [102, 125, 112], [105, 121, 91], [148, 138, 99], [166, 145, 101]], [[112, 65, 109], [122, 89, 111], [112, 117, 86], [104, 140, 83], [80, 127, 80], [87, 121, 105], [99, 108, 123], [126, 111, 144], [135, 109, 147], [127, 106, 139], [137, 132, 156], [115, 125, 140], [120, 140, 149], [104, 115, 125], [130, 126, 139], [125, 118, 122], [135, 136, 123], [126, 135, 103], [150, 147, 114], [139, 133, 98]], [[137, 88, 128], [136, 105, 124], [102, 116, 86], [88, 140, 73], [77, 141, 70], [87, 131, 87], [119, 128, 125], [143, 120, 153], [164, 130, 181], [137, 112, 163], [123, 124, 158], [95, 124, 135], [111, 153, 149], [126, 142, 140], [164, 134, 146], [153, 106, 111], [150, 119, 103], [131, 137, 97], [136, 142, 114], [132, 142, 116]], [[109, 67, 95], [136, 108, 123], [122, 131, 110], [118, 162, 96], [97, 144, 65], [114, 126, 82], [146, 119, 126], [157, 117, 154], [169, 141, 180], [134, 120, 159], [121, 122, 164], [91, 114, 144], [96, 141, 142], [97, 124, 112], [145, 110, 120], [159, 102, 112], [167, 128, 122], [130, 142, 107], [121, 136, 120], [110, 128, 118]], [[144, 106, 134], [153, 125, 144], [149, 145, 135], [136, 154, 99], [136, 150, 80], [129, 117, 88], [151, 120, 143], [141, 120, 156], [157, 153, 171], [137, 132, 147], [130, 115, 154], [116, 110, 160], [110, 131, 157], [109, 133, 134], [134, 114, 127], [145, 114, 134], [141, 126, 141], [113, 141, 133], [100, 122, 127], [95, 116, 124]], [[122, 82, 118], [127, 96, 121], [152, 139, 136], [151, 145, 107], [151, 145, 100], [119, 118, 105], [108, 120, 147], [108, 133, 165], [141, 159, 171], [162, 152, 157], [164, 129, 155], [146, 110, 159], [119, 103, 149], [107, 108, 135], [109, 107, 125], [119, 130, 155], [119, 144, 172], [100, 141, 164], [99, 125, 144], [82, 103, 119]], [[158, 117, 144], [140, 111, 127], [142, 140, 130], [131, 134, 110], [143, 145, 127], [127, 140, 144], [108, 140, 163], [101, 136, 163], [128, 140, 157], [168, 150, 159], [166, 132, 147], [153, 117, 150], [119, 88, 133], [124, 105, 145], [114, 117, 134], [102, 132, 151], [92, 135, 158], [83, 122, 152], [104, 130, 141], [95, 113, 117]], [[175, 137, 134], [152, 136, 123], [133, 164, 135], [110, 154, 133], [107, 131, 135], [113, 111, 135], [111, 92, 119], [125, 100, 121], [146, 123, 139], [178, 164, 177], [151, 145, 159], [130, 122, 142], [100, 83, 110], [130, 111, 136], [130, 125, 136], [117, 139, 146], [94, 128, 135], [79, 110, 117], [107, 130, 115], [109, 125, 103]], [[163, 157, 126], [149, 157, 119], [121, 161, 111], [106, 157, 127], [101, 132, 134], [129, 117, 136], [149, 103, 115], [146, 101, 98], [130, 114, 105], [129, 146, 137], [112, 136, 130], [121, 124, 126], [109, 86, 97], [138, 111, 120], [129, 120, 113], [119, 133, 126], [109, 127, 121], [113, 116, 111], [134, 122, 93], [149, 130, 90]], [[145, 149, 113], [140, 151, 108], [133, 165, 112], [119, 165, 129], [107, 143, 136], [119, 117, 125], [143, 107, 109], [145, 113, 99], [129, 134, 108], [116, 151, 121], [104, 133, 110], [119, 112, 106], [130, 96, 105], [152, 125, 129], [134, 139, 117], [123, 145, 127], [118, 133, 122], [126, 113, 113], [136, 103, 79], [142, 101, 67]], [[106, 101, 82], [122, 121, 95], [127, 140, 100], [134, 164, 132], [129, 167, 156], [128, 158, 158], [139, 156, 154], [121, 137, 126], [105, 134, 106], [111, 145, 101], [134, 146, 103], [156, 127, 111], [160, 108, 126], [140, 111, 126], [110, 139, 109], [92, 133, 104], [114, 136, 123], [133, 110, 130], [134, 98, 103], [132, 91, 88]], [[121, 89, 82], [129, 115, 103], [114, 141, 120], [117, 168, 159], [110, 161, 172], [114, 145, 170], [116, 124, 149], [113, 107, 121], [109, 105, 97], [126, 132, 98], [147, 152, 108], [158, 141, 122], [156, 120, 138], [122, 105, 128], [94, 133, 113], [79, 121, 89], [112, 136, 117], [116, 106, 129], [107, 112, 144], [76, 87, 124]], [[115, 68, 68], [126, 103, 98], [102, 132, 120], [114, 174, 173], [118, 175, 194], [120, 155, 189], [124, 132, 168], [115, 104, 129], [111, 96, 95], [136, 130, 98], [168, 166, 124], [170, 154, 137], [153, 123, 144], [94, 82, 109], [83, 128, 113], [70, 114, 81], [117, 144, 123], [113, 108, 134], [95, 117, 161], [67, 100, 152]]]
        self.assertEqual(blurred_image.tolist(), expect, "DataFrame contents should match the expected output")

    def test_invalid_image_path(self):
        with self.assertRaises(FileNotFoundError):
            f_2505('nonexistent.jpg', 3)

    def test_invalid_kernel_size(self):
        with self.assertRaises(ValueError):
            f_2505(self.dummy_img_path, -1)

    def test_zero_kernel_size(self):
        with self.assertRaises(ValueError):
            f_2505(self.dummy_img_path, 0)

    def test_non_integer_kernel_size(self):
        with self.assertRaises(ValueError):
            f_2505(self.dummy_img_path, 2.5)

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
