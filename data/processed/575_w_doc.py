from random import shuffle
import pandas as pd
import numpy as np

# Constants



def task_func(l, n_groups = 5):
    """
    Given a list `l`, this function shuffles the list, constructs a dataframe using the shuffled list,
    and then for each row in the dataframe, moves the first n_groups elements to the end of the same row.

    Parameters:
    - l (list): A list of elements.
    - n_groups (int): number of groups. Default value is 5.

    Returns:
    - DataFrame: A modified DataFrame constructed from the shuffled list.

    Requirements:
    - pandas
    - numpy
    - random

    Example:
    >>> df = task_func(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
    >>> df.shape == (5, 10)
    True
    >>> set(df.iloc[0]) == set(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
    True
    """

    if not l:
        return pd.DataFrame()
    shuffle(l)
    df = pd.DataFrame([l for _ in range(n_groups)])
    df = df.apply(lambda row: np.roll(row, -n_groups), axis=1, result_type='expand')
    return df

import unittest
ELEMENTS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
N_GROUPS = 5
class TestCases(unittest.TestCase):
    def test_with_predefined_elements(self):
        """Test function with the predefined ELEMENTS list."""
        df = task_func(ELEMENTS.copy())  # Use a copy to prevent modification of the original list
        self.assertEqual(df.shape, (N_GROUPS, len(ELEMENTS)))
        # Ensure all original elements are present in each row
        for row in df.itertuples(index=False):
            self.assertTrue(set(ELEMENTS) == set(row))
    def test_empty_list(self):
        """Test function with an empty list."""
        df = task_func([])
        self.assertTrue(df.empty)
    def test_single_element_list(self):
        """Test function with a single-element list."""
        single_element_list = ['X']
        df = task_func(single_element_list)
        self.assertEqual(df.shape, (N_GROUPS, 1))
        # Ensure the single element is present in each row
        for row in df.itertuples(index=False):
            self.assertTrue(all([elem == 'X' for elem in row]))
    def test_varying_data_types(self):
        """Test function with a list containing varying data types."""
        mixed_list = ['A', 1, 3.14, True, None]
        df = task_func(mixed_list.copy())  # Use a copy to prevent modification of the original list
        self.assertEqual(df.shape, (N_GROUPS, len(mixed_list)))
        # Ensure all original elements are present in each row
        for row in df.itertuples(index=False):
            self.assertTrue(set(mixed_list) == set(row))
    def test_shuffle_and_roll_operation(self):
        """Test to ensure shuffle and roll operations change the list order."""
        df_initial = pd.DataFrame([ELEMENTS for _ in range(N_GROUPS)])
        df_modified = task_func(ELEMENTS.copy())
        # Compare if any row differs from the initial order
        diff = (df_initial != df_modified).any(axis=1).any()  # True if any row differs
        self.assertTrue(diff, "Shuffled DataFrame rows should differ from initial order")
