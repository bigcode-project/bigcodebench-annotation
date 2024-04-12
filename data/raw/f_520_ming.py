import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

def f_520(x, y, labels):
    """
    Draw normal distributions for multiple 'x' and 'y' arrays with labels.
    Each pair (x, y) represents a different chemical compound in the 'labels' list.

    Parameters:
    x (list): List of numpy arrays representing the x-values of the data points.
    y (list): List of numpy arrays representing the y-values of the data points.
    labels (list): List of strings representing the labels for the chemical compounds.

    Returns:
    fig: Matplotlib figure object.

    Requirements:
    - numpy
    - matplotlib.pyplot
    - scipy.stats

    Example:
    >>> x = [np.array([1,2,3]), np.array([4,5,6]), np.array([7,8,9])]
    >>> y = [np.array([4,5,6]), np.array([7,8,9]), np.array([10,11,12])]
    >>> labels = ['H₂O', 'O₂', 'CO₂']
    >>> fig = f_520(x, y, labels)
    >>> plt.show(fig)
    """
    fig, ax = plt.subplots()

    for i in range(len(x)):
        mu = np.mean(y[i])
        sigma = np.std(y[i])
        pdf = stats.norm.pdf(x[i], mu, sigma)
        ax.plot(x[i], pdf, label=labels[i])
    
    ax.legend()
    
    return fig

import unittest
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.stats as stats


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):

    def test_case_1(self):
        x = [np.array([1,2,3]), np.array([4,5,6]), np.array([7,8,9])]
        y = [np.array([4,5,6]), np.array([7,8,9]), np.array([10,11,12])]
        labels = ['H₂O', 'O₂', 'CO₂']
        fig = f_520(x, y, labels)
        self.assertIsInstance(fig, matplotlib.figure.Figure)

    def test_case_2(self):
        x = [np.array([1,3,5]), np.array([2,4,6])]
        y = [np.array([2,4,6]), np.array([1,3,5])]
        labels = ['N₂', 'Ar']
        fig = f_520(x, y, labels)
        self.assertIsInstance(fig, matplotlib.figure.Figure)

    def test_case_3(self):
        x = [np.array([10,20,30])]
        y = [np.array([15,25,35])]
        labels = ['H₂O']
        fig = f_520(x, y, labels)
        self.assertIsInstance(fig, matplotlib.figure.Figure)

    def test_case_4(self):
        x = [np.array([5,15,25]), np.array([10,20,30]), np.array([15,25,35])]
        y = [np.array([10,20,30]), np.array([15,25,35]), np.array([5,15,25])]
        labels = ['H₂O', 'O₂', 'CO₂']
        fig = f_520(x, y, labels)
        self.assertIsInstance(fig, matplotlib.figure.Figure)

    def test_case_5(self):
        x = [np.array([2,4,8]), np.array([1,3,7])]
        y = [np.array([1,3,7]), np.array([2,4,8])]
        labels = ['N₂', 'Ar']
        fig = f_520(x, y, labels)
        self.assertIsInstance(fig, matplotlib.figure.Figure)


if __name__ == "__main__":
    run_tests()