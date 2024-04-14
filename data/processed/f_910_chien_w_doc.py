import numpy as np
import matplotlib.pyplot as plt

# Constants
NUM_SAMPLES = 100
NUM_OUTLIERS = 5


def f_910(num_samples=NUM_SAMPLES, num_outliers=NUM_OUTLIERS):
    """
    Generate a dataset comprising both normal data and artificially introduced outliers,
    and plot a histogram of the combined data. The function detects outliers in the dataset
    using the Interquartile Range (IQR) method, but it only considers the normally distributed
    portion of the data for outlier detection. The outliers detected and the artificially
    introduced outliers might not always coincide.

    Parameters:
    - num_samples (int): Number of samples to be drawn from a normal distribution. The default 
      value is 100. If set to zero or a negative number, no normal data will be generated, 
      and the dataset will only contain artificially introduced outliers.
    - num_outliers (int): Number of outliers to be artificially introduced into the dataset. 
      These outliers are uniformly distributed between -10 and 10. The default value is 5. 
      If set to zero, no outliers will be artificially introduced.


    Returns:
    - data (numpy array): The combined dataset, including both normally distributed data and 
      the artificially introduced outliers.
    - outliers_detected (numpy array): The outliers detected using the IQR method. This 
      detection is based solely on the normally distributed portion of the data.
    - ax (matplotlib.axes._subplots.AxesSubplot): The AxesSubplot object for the histogram 
      plot of the combined dataset.

    Requirements:
    - numpy
    - matplotlib

    Note:
    - The artificially introduced outliers are not necessarily the same as the outliers
    detected by the IQR method. The IQR method is applied only to the normally distributed
    data, and thus some of the artificially introduced outliers may not be detected,
    and some normal data points may be falsely identified as outliers.

    Example:
    >>> import numpy as np
    >>> np.random.seed(0)
    >>> data, outliers_detected, ax = f_910()
    >>> print(outliers_detected)
    [-9.61613603 -3.96850367  3.20347075]
    """
    normal_data = np.random.normal(size=num_samples)
    outliers = np.random.uniform(low=-10, high=10, size=num_outliers)
    data = np.concatenate([normal_data, outliers]) if num_samples > 0 else outliers

    # Identify outliers using IQR (only if there is normal data)
    outliers_detected = np.array([])
    if num_samples > 0:
        q75, q25 = np.percentile(normal_data, [75, 25])
        iqr = q75 - q25
        lower_bound = q25 - (iqr * 1.5)
        upper_bound = q75 + (iqr * 1.5)
        outliers_detected = data[(data < lower_bound) | (data > upper_bound)]

    # Plot histogram
    _, ax = plt.subplots()
    ax.hist(data, bins=30)

    return data, outliers_detected, ax

import unittest
import numpy as np
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    """Test cases for the function f_910."""
    def test_default_values(self):
        """Test the function with default values."""
        np.random.seed(0)
        data, _, _ = f_910()
        self.assertEqual(len(data), 105)
    def test_custom_values(self):
        """Test the function with custom values."""
        np.random.seed(1)
        data, outliers_detected, _ = f_910(num_samples=50, num_outliers=10)
        self.assertEqual(len(data), 60)
        # Replicate the IQR calculation for testing
        normal_data = data[:50]  # Assuming the first 50 are normal data
        q75, q25 = np.percentile(normal_data, [75, 25])
        iqr = q75 - q25
        lower_bound = q25 - (iqr * 1.5)
        upper_bound = q75 + (iqr * 1.5)
        expected_outliers_count = len(
            [o for o in data if o < lower_bound or o > upper_bound]
        )
        self.assertEqual(len(outliers_detected), expected_outliers_count)
    def test_no_outliers(self):
        """Test the function with no outliers."""
        np.random.seed(2)
        data, outliers_detected, ax = f_910(num_samples=100, num_outliers=0)
        self.assertEqual(len(data), 100)
        # Adjust the expectation to consider possible false positives
        self.assertTrue(len(outliers_detected) <= 1)  # Allow for up to 1 false positive
    def test_only_outliers(self):
        """Test the function with only outliers."""
        np.random.seed(3)
        data, outliers_detected, _ = f_910(num_samples=0, num_outliers=100)
        self.assertEqual(len(data), 100)
        # Since no normal data is generated, IQR is not applied, and no outliers are detected.
        self.assertEqual(len(outliers_detected), 0)
    def test_negative_values(self):
        """Test the function with negative values."""
        np.random.seed(4)
        with self.assertRaises(ValueError):
            f_910(num_samples=-10, num_outliers=-5)
    def tearDown(self):
        plt.close()
