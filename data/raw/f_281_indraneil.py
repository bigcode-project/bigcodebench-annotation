import numpy as np
import random
from sklearn.preprocessing import MinMaxScaler


def f_281(list_of_lists, seed=42):
    """
    Scale the values in a list of lists to a (0,1) range using MinMaxScaler.
    If any inner list is empty, the function fills it with five random integers between 0 and 100, and then scales the values.
    
    Parameters:
    list_of_lists (list of list of int): A list containing inner lists of integers.
    seed (int, Optional): Seed for random number generation. Default is 42.
    
    Returns:
    list of list of float: A list of lists containing scaled values between the range [0, 1].
    
    Requirements:
    - numpy
    - random
    - sklearn.preprocessing.MinMaxScaler
    
    Example:
    >>> f_281([[1, 2, 3], [], [4, 5, 6]])
    [[0.0, 0.5, 1.0], [0.8571428571428572, 0.1208791208791209, 0.0, 1.0, 0.3516483516483517], [0.0, 0.5, 1.0]]
    """
    np.random.seed(seed)
    random.seed(seed)
    scaled_data = []
    scaler = MinMaxScaler(feature_range=(0, 1))
    for list_ in list_of_lists:
        if not list_:
            list_ = [random.randint(0, 100) for _ in range(5)]
        # Reshape the data to fit the scaler
        reshaped_data = np.array(list_).reshape(-1, 1)
        scaled_list = scaler.fit_transform(reshaped_data)
        # Flatten the list and append to the result
        scaled_data.append(scaled_list.flatten().tolist())
    
    return scaled_data


import unittest
import doctest


class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        input_data = [[1, 2, 3], [], [4, 5, 6]]
        output = f_281(input_data)
        for inner_list in output:
            self.assertTrue(0.0 <= min(inner_list) <= 1.0)
            self.assertTrue(0.0 <= max(inner_list) <= 1.0)
            self.assertTrue(len(inner_list) <= 5)
    
    def test_case_2(self):
        input_data = [[10, 20, 30, 40, 50], [], [60, 70, 80, 90, 100]]
        output = f_281(input_data)
        for inner_list in output:
            self.assertTrue(0.0 <= min(inner_list) <= 1.0)
            self.assertTrue(0.0 <= max(inner_list) <= 1.0)
            self.assertEqual(len(inner_list), 5)
        
    def test_case_3(self):
        input_data = [[], [], []]
        output = f_281(input_data)
        for inner_list in output:
            self.assertTrue(0.0 <= min(inner_list) <= 1.0)
            self.assertTrue(0.0 <= max(inner_list) <= 1.0)
            self.assertEqual(len(inner_list), 5)

    def test_case_4(self):
        input_data = [[15], [25], [35], [45], [55]]
        expected_output = [[0.0], [0.0], [0.0], [0.0], [0.0]]
        output = f_281(input_data)
        self.assertEqual(output, expected_output)
    
    def test_case_5(self):
        input_data = [[0, 100], [0, 50], [50, 100]]
        expected_output = [[0.0, 1.0], [0.0, 1.0], [0.0, 1.0]]
        output = f_281(input_data)
        self.assertEqual(output, expected_output)
        

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    doctest.testmod()
    run_tests()
