import csv
import random


def f_655(csv_file='names.csv', 
          latin_names=['Sopetón', 'Méndez', 'Gómez', 'Pérez', 'Muñoz'],
          names=['Smith', 'Johnson', 'Williams', 'Brown', 'Jones'],
          encoding='latin-1', rng_seed=None):
    """
    Create a CSV file with 100 lines. Each line contains a name and an age (randomly generated between 20 and 50).
    Half of the names are randomly selected from a list of Latin names (default: ['Sopetón', 'Méndez', 'Gómez', 'Pérez', 'Muñoz']), 
    the other half from a list of English names (default: ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones']).
    All names are encoded using the specified encoding.
    If empty name arrays are passed, a csv with headers but no entries is generated.

    Args:
    - csv_file (str, optional): Name of the CSV file to be created. Defaults to 'names.csv'.
    - latin_names (list, optional): List of Latin names. Defaults to ['Sopetón', 'Méndez', 'Gómez', 'Pérez', 'Muñoz'].
    - names (list, optional): List of English names. Defaults to ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones'].
    - encoding (str, optional): The encoding used for writing the names. Defaults to 'latin-1'
    - rng_seed (int, optional): The seed for the rng. Defaults to None.

    Returns:
    - str: The CSV file name.

    Raises:
    - TypeError: If csv_file is not a string.
    - TypeError: If latin_names is not an array.
    - TypeError: If names is not an array.

    Requirements:
    - csv
    - random

    Example:
    >>> file_name = f_655()
    >>> print(file_name)
    'names.csv'

    >>> file_name = f_655(csv_file='test.csv', names=['simon', 'alex'])
    >>> with open(file_name, 'r', newline='', encoding='latin-1') as csvfile:
    >>>     reader = csv.reader(csvfile)
    >>>     rows = list(reader)
    >>>     print(rows)
    [['Name', 'Age'], ['Sopetón', '48'], ['alex', '38'], ['Muñoz', '33'], ['simon', '34'], ['Muñoz', '38'], ['simon', '33'], ['Sopetón', '22'], ['simon', '38'], ['Sopetón', '37'], ['alex', '35'], ['Muñoz', '41'], ['alex', '39'], ['Sopetón', '33'], ['simon', '40'], ['Méndez', '27'], ['alex', '44'], ['Pérez', '26'], ['simon', '27'], ['Sopetón', '31'], ['alex', '45'], ['Sopetón', '42'], ['alex', '45'], ['Méndez', '29'], ['alex', '48'], ['Pérez', '36'], ['simon', '25'], ['Pérez', '46'], ['alex', '30'], ['Muñoz', '32'], ['simon', '41'], ['Méndez', '31'], ['alex', '35'], ['Pérez', '47'], ['alex', '45'], ['Méndez', '49'], ['simon', '35'], ['Sopetón', '36'], ['simon', '24'], ['Sopetón', '39'], ['simon', '45'], ['Gómez', '41'], ['alex', '48'], ['Muñoz', '43'], ['simon', '20'], ['Méndez', '35'], ['alex', '30'], ['Méndez', '40'], ['simon', '43'], ['Gómez', '49'], ['simon', '31'], ['Gómez', '33'], ['alex', '36'], ['Gómez', '39'], ['simon', '40'], ['Pérez', '28'], ['alex', '47'], ['Gómez', '28'], ['alex', '47'], ['Pérez', '50'], ['simon', '26'], ['Pérez', '24'], ['alex', '38'], ['Pérez', '32'], ['simon', '30'], ['Muñoz', '32'], ['alex', '28'], ['Gómez', '25'], ['simon', '24'], ['Méndez', '33'], ['alex', '37'], ['Gómez', '37'], ['simon', '41'], ['Sopetón', '49'], ['alex', '38'], ['Méndez', '24'], ['alex', '39'], ['Sopetón', '29'], ['simon', '47'], ['Sopetón', '29'], ['simon', '24'], ['Muñoz', '49'], ['alex', '44'], ['Sopetón', '40'], ['alex', '21'], ['Pérez', '32'], ['simon', '28'], ['Muñoz', '34'], ['alex', '39'], ['Gómez', '38'], ['alex', '32'], ['Sopetón', '26'], ['simon', '20'], ['Gómez', '30'], ['alex', '39'], ['Pérez', '42'], ['alex', '47'], ['Sopetón', '22'], ['simon', '37'], ['Pérez', '39'], ['simon', '47']]

    """

    if not isinstance(csv_file, str):
        raise TypeError("csv_file should be a string.")
    
    if not isinstance(names, list):
        raise TypeError("names should be a list.")
    
    if not isinstance(latin_names, list):
        raise TypeError("latin_names should be a list.")

    if rng_seed is not None:
        random.seed(rng_seed)

    with open(csv_file, 'w', newline='', encoding=encoding) as csvfile:
        fieldnames = ['Name', 'Age']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for _ in range(50):
            if latin_names:
                writer.writerow({'Name': random.choice(latin_names), 'Age': random.randint(20, 50)})
            if names:
                writer.writerow({'Name': random.choice(names), 'Age': random.randint(20, 50)})

    return csv_file


import unittest
import os
import csv
from faker import Faker
from pathlib import Path


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):
    def test_case_1(self):
        'default params'

        latin_names = ['Sopetón', 'Méndez', 'Gómez', 'Pérez', 'Muñoz']
        names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones']

        file_name = f_655(rng_seed=1)
        self.assertEqual(file_name, 'names.csv')
        self.assertTrue(os.path.isfile(file_name))

        with open(file_name, 'r', newline='', encoding='latin-1') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
            self.assertEqual(len(rows), 101)
            self.assertEqual(rows[0], ['Name', 'Age'])
            csv_names = [row[0] for row in rows[1:]]
            for name in csv_names:
                self.assertIn(name, latin_names+names)
            ages = [int(row[1]) for row in rows[1:]]
            for age in ages:
                self.assertTrue(20 <= age <= 50)

        # remove file
        Path(file_name).unlink()

    def test_rng(self):
        'test rng reproducability'
        file_name1 = f_655(csv_file='test1.csv', rng_seed=12)
        file_name2 = f_655(csv_file='test2.csv', rng_seed=12)

        self.assertEqual(file_name1, 'test1.csv')
        self.assertEqual(file_name2, 'test2.csv')
        self.assertTrue(os.path.isfile(file_name1))
        self.assertTrue(os.path.isfile(file_name2))

        with open(file_name1, 'r', newline='', encoding='latin-1') as file1:
            with open(file_name2, 'r', newline='', encoding='latin-1') as file2:
                reader1 = csv.reader(file1)
                rows1 = list(reader1)
                reader2 = csv.reader(file2)
                rows2 = list(reader2)

                self.assertEqual(rows1, rows2)

        # remove files
        Path(file_name1).unlink()
        Path(file_name2).unlink()

    def test_case_2(self):
        'different encoding'
        custom_file = 'custom_names.csv'
        latin_names = ['Méndez']
        names = ['Simon']
        file_name = f_655(csv_file=custom_file, names=names, encoding='utf-8',
                          latin_names=latin_names, rng_seed=1)
        self.assertEqual(file_name, custom_file)
        self.assertTrue(os.path.isfile(custom_file))

        with open(file_name, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
            self.assertEqual(len(rows), 101)
            self.assertEqual(rows[0], ['Name', 'Age'])
            csv_names = [row[0] for row in rows[1:]]
            for name in csv_names:
                self.assertIn(name, latin_names+names)
            ages = [int(row[1]) for row in rows[1:]]
            for age in ages:
                self.assertTrue(20 <= age <= 50)

        # remove file
        Path(file_name).unlink()

    def test_case_3(self):
        latin_names = [Faker().first_name() for _ in range(5)]
        names = [Faker().first_name() for _ in range(5)]
        file_name = f_655(latin_names=latin_names, names=names, rng_seed=1)

        self.assertEqual(file_name, file_name)
        self.assertTrue(os.path.isfile(file_name))

        with open(file_name, 'r', newline='', encoding='latin-1') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
            self.assertEqual(len(rows), 101)
            self.assertEqual(rows[0], ['Name', 'Age'])
            csv_names = [row[0] for row in rows[1:]]
            for name in csv_names:
                self.assertIn(name, latin_names+names)
            ages = [int(row[1]) for row in rows[1:]]
            for age in ages:
                self.assertTrue(20 <= age <= 50)

        # remove file
        Path(file_name).unlink()

    def test_case_4(self):
        'emtpy name lists'
        file_name = f_655(latin_names=[], names=[], rng_seed=1)

        self.assertEqual(file_name, file_name)
        self.assertTrue(os.path.isfile(file_name))

        with open(file_name, 'r', newline='', encoding='latin-1') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0], ['Name', 'Age'])
        # remove file
        Path(file_name).unlink()

    def test_case_5(self):
        'edge cases'
        self.assertRaises(Exception, f_655, {'csv_file': 1, 'rng_seed': 12})
        self.assertRaises(Exception, f_655, {'latin_names': 'test', 'rng_seed': 12})
        self.assertRaises(Exception, f_655, {'names': 24, 'rng_seed': 12})

        # remove file if generated
        if os.path.isfile('names.csv'):
            Path('names.csv').unlink()

if __name__ == "__main__":
    run_tests()