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
    names.csv

    >>> file_name = f_655(csv_file='test.csv', names=['simon', 'alex'], rng_seed=1)
    >>> with open(file_name, 'r', newline='', encoding='latin-1') as csvfile:
    ...     reader = csv.reader(csvfile)
    ...     rows = list(reader)
    ...     print(rows)
    [['Name', 'Age'], ['Méndez', '38'], ['simon', '28'], ['Sopetón', '35'], ['alex', '35'], ['Pérez', '45'], ['simon', '23'], ['Pérez', '20'], ['alex', '33'], ['Muñoz', '44'], ['simon', '42'], ['Pérez', '28'], ['simon', '38'], ['Sopetón', '48'], ['alex', '20'], ['Sopetón', '20'], ['simon', '50'], ['Pérez', '41'], ['simon', '33'], ['Sopetón', '36'], ['simon', '44'], ['Pérez', '50'], ['alex', '37'], ['Méndez', '31'], ['simon', '41'], ['Méndez', '44'], ['alex', '50'], ['Gómez', '49'], ['simon', '33'], ['Muñoz', '49'], ['simon', '25'], ['Gómez', '23'], ['alex', '48'], ['Muñoz', '49'], ['alex', '36'], ['Méndez', '29'], ['alex', '38'], ['Pérez', '47'], ['alex', '38'], ['Sopetón', '35'], ['simon', '43'], ['Pérez', '33'], ['simon', '31'], ['Muñoz', '48'], ['alex', '22'], ['Pérez', '41'], ['simon', '44'], ['Méndez', '36'], ['alex', '31'], ['Pérez', '43'], ['simon', '35'], ['Sopetón', '29'], ['alex', '40'], ['Méndez', '25'], ['simon', '20'], ['Méndez', '37'], ['simon', '32'], ['Muñoz', '31'], ['alex', '34'], ['Gómez', '41'], ['simon', '32'], ['Muñoz', '45'], ['simon', '36'], ['Muñoz', '26'], ['alex', '50'], ['Sopetón', '35'], ['alex', '38'], ['Muñoz', '26'], ['alex', '35'], ['Gómez', '33'], ['alex', '20'], ['Muñoz', '37'], ['alex', '34'], ['Muñoz', '20'], ['simon', '40'], ['Méndez', '37'], ['simon', '47'], ['Sopetón', '45'], ['alex', '21'], ['Sopetón', '22'], ['simon', '34'], ['Sopetón', '44'], ['alex', '27'], ['Gómez', '23'], ['simon', '31'], ['Gómez', '22'], ['simon', '25'], ['Gómez', '36'], ['simon', '41'], ['Gómez', '40'], ['alex', '34'], ['Gómez', '35'], ['alex', '23'], ['Sopetón', '29'], ['alex', '30'], ['Pérez', '45'], ['simon', '28'], ['Sopetón', '28'], ['simon', '50'], ['Muñoz', '33'], ['simon', '27']]
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
