import numpy as np
import random
import itertools
import pandas as pd

# Constants
PLANETS = [
    "Mercury",
    "Venus",
    "Earth",
    "Mars",
    "Jupiter",
    "Saturn",
    "Uranus",
    "Neptune",
]
ELEMENTS = [
    "Hydrogen",
    "Helium",
    "Oxygen",
    "Carbon",
    "Nitrogen",
    "Magnesium",
    "Silicon",
    "Iron",
    "Nickel",
]


def f_903():
    """
    Generate a DataFrame where each row contains random planet-element pairs.
    Each pair is formatted as 'Planet:Element'. The number of rows is determined by
    the number of planets, and each row will contain as many planet-element pairs as there are elements.

    Parameters:
    - None

    Returns:
    pandas.DataFrame: A DataFrame where each cell contains a string in the format 'Planet:Element'.
                      The DataFrame has a number of rows equal to the number of planets and
                      a number of columns equal to the number of elements.

    Requirements:
    - numpy
    - random
    - itertools
    - pandas

    Example:
    >>> random.seed(0)
    >>> planet_elements_table = f_903()
    >>> planet_elements_table.head(2)
              Hydrogen         Helium           Oxygen          Carbon          Nitrogen     Magnesium            Silicon          Iron         Nickel
    0   Uranus:Silicon  Earth:Silicon  Neptune:Silicon  Neptune:Nickel   Uranus:Hydrogen  Jupiter:Iron   Neptune:Nitrogen  Earth:Nickel  Uranus:Helium
    1  Venus:Magnesium  Saturn:Helium    Mars:Nitrogen  Mercury:Helium  Jupiter:Nitrogen  Venus:Oxygen  Neptune:Magnesium  Mercury:Iron   Venus:Helium
    """
    # Generate all possible pairs
    pairs = [
        f"{planet}:{element}"
        for planet, element in itertools.product(PLANETS, ELEMENTS)
    ]
    # Shuffle the pairs to ensure randomness
    random.shuffle(pairs)

    # Convert the list of pairs into a numpy array, then reshape it to fit the DataFrame dimensions
    data = np.array(pairs).reshape(len(PLANETS), len(ELEMENTS))
    # Create the DataFrame with ELEMENTS as column headers
    df = pd.DataFrame(data, columns=ELEMENTS)

    return df


import unittest
import itertools
import pandas as pd
import random


class TestCases(unittest.TestCase):
    """Tests for `f_903`."""

    def test_basic_structure(self):
        """Test the basic structure of the table."""
        random.seed(0)
        table = f_903()
        # Verify the structure of the table
        self.assertEqual(len(table), len(PLANETS))
        self.assertEqual(list(table.columns), ELEMENTS)

    def test_pair_existence(self):
        """Test the existence of planet-element pairs."""
        random.seed(1)
        table = f_903()
        # Verify all planet-element pairs are present
        all_pairs = set(f"{p}:{e}" for p, e in itertools.product(PLANETS, ELEMENTS))
        generated_pairs = set(table.values.flatten())
        self.assertEqual(all_pairs, generated_pairs)
        # Verify no extra pairs are present
        self.assertEqual(len(all_pairs), len(generated_pairs))

    def test_data_type(self):
        """Test the data type of the table and its elements."""
        random.seed(2)
        table = f_903()
        # Check the data type of the table and its elements
        self.assertIsInstance(table, pd.DataFrame)
        self.assertTrue(all(isinstance(cell, str) for cell in table.values.flatten()))

    def test_data_format(self):
        """Test the format of the elements in the table."""
        random.seed(3)
        table = f_903()
        # Check the format of the elements in the table
        self.assertTrue(
            all(
                ":" in cell and len(cell.split(":")) == 2
                for cell in table.values.flatten()
            )
        )

    def test_uniqueness(self):
        """Test the uniqueness of the pairs."""
        random.seed(4)
        table = f_903()
        # Check uniqueness of the pairs
        generated_pairs = table.values.flatten()
        self.assertEqual(len(generated_pairs), len(set(generated_pairs)))


# Running the test cases
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
