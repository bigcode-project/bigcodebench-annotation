import os
import csv
import random
from faker import Faker


def f_696(file_path, num_rows, random_seed=None):
    """
    Generate a CSV file on a specific file path with fake personal data.
    The personal data consists of the following columns:
    - Name: random names generated with faker
    - Age: random age values: 20<=age<=60
    - Address: random adresses generated with faker
    - Email: random email adresses generated with faker

    Newlines '\n' in the generated addresses get replaced with ', '.
    The number of rows in the CSV file is determined by num_rows.

    Parameters:
    file_path (str): The file path where the CSV file should be created.
    num_rows (int): The number of rows of random data to generate.
    random_seed (int, optional): Seed used random generation. Same seed used for faker and random module.
                                 Defaults to None.
    
    Returns:
    str: The file path of the generated CSV file.

    Raises:
    ValueError: If num_rows is not an integer >= 0.

    Requirements:
    - os: For handling file-related operations.
    - csv: For writing data to a CSV file.
    - random: For generating random age values.
    - faker: For generating fake personal data.

    Example:
    >>> f_696('/tmp/people.csv', 100)
    '/tmp/people.csv'

    >>> path = f_696('test.csv', 5, random_seed=12)
    >>> with open(path, 'r') as file:
    >>>     reader = csv.reader(file)
    >>>     rows = list(reader)
    >>> print(rows)
    [
        ['Name', 'Age', 'Address', 'Email'], 
        ['Matthew Estrada', '50', '7479 Angela Shore, South Michael, MA 28059', 'johnstonjames@example.net'],
        ['Gabrielle Sullivan', '37', '83167 Donna Dale, Nicoleside, GA 91836', 'peterswilliam@example.org'],
        ['Jason Carlson', '53', '013 Kelly Lake Suite 414, West Michael, NY 75635', 'anthonycarson@example.com'],
        ['Alexander Lowe', '42', '183 Christian Harbor, South Joshuastad, PA 83984', 'palmermicheal@example.com'],
        ['John Benjamin', '29', '8523 Rhonda Avenue, Rosemouth, HI 32166', 'masonjohn@example.org']
    ]
    """

    if num_rows < 0 or not isinstance(num_rows, int):
        raise ValueError('num_rows should be an integer >=0.')

    fake = Faker()
    fake.seed_instance(random_seed)
    random.seed(random_seed)
    with open(file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Name', 'Age', 'Address', 'Email'])
        for _ in range(num_rows):
            name = fake.name()
            age = random.randint(20, 60)
            address = fake.address().replace('\n', ', ')
            email = fake.email()
            writer.writerow([name, age, address, email])
    return file_path

import unittest
import csv
import os
from faker import Faker
import tempfile
import pandas as pd

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):
    def setUp(self):
        self.fake = Faker()
        self.folder_path = tempfile.mkdtemp()
        self.file_path = os.path.join(self.folder_path, 'test.csv')

    def test_rng(self):
        res_path1 = f_696(os.path.join(self.folder_path, 'test1.csv'), 45, random_seed=42)
        res_path2 = f_696(os.path.join(self.folder_path, 'test2.csv'), 45, random_seed=42)
        with open(res_path1, 'r') as file:
            reader = csv.reader(file)
            rows1 = list(reader)

        with open(res_path2, 'r') as file:
            reader = csv.reader(file)
            rows2 = list(reader)

        self.assertEqual(rows1, rows2)

    def test_case_1(self):
        num_rows = 10
        result_path = f_696(self.file_path, num_rows, random_seed=12)
        self.assertTrue(os.path.exists(result_path))
        with open(result_path, 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            self.assertEqual(len(rows), num_rows + 1)
        
        expected = [['Name', 'Age', 'Address', 'Email'],
            ['Matthew Estrada',
            '50',
            '7479 Angela Shore, South Michael, MA 28059',
            'johnstonjames@example.net'],
            ['Gabrielle Sullivan',
            '37',
            '83167 Donna Dale, Nicoleside, GA 91836',
            'peterswilliam@example.org'],
            ['Jason Carlson',
            '53',
            '013 Kelly Lake Suite 414, West Michael, NY 75635',
            'anthonycarson@example.com'],
            ['Alexander Lowe',
            '42',
            '183 Christian Harbor, South Joshuastad, PA 83984',
            'palmermicheal@example.com'],
            ['John Benjamin',
            '29',
            '8523 Rhonda Avenue, Rosemouth, HI 32166',
            'masonjohn@example.org'],
            ['Dr. Kathy Johnson',
            '44',
            '138 Burns Knoll Suite 727, Christinaton, KY 43754',
            'nbush@example.net'],
            ['David Vega',
            '20',
            '462 James Mountains, New Ashleyview, WV 05639',
            'freynolds@example.com'],
            ['Lauren Bailey',
            '43',
            '202 Lauren Cliffs Suite 836, Lake Michaelport, KY 90824',
            'hhowell@example.org'],
            ['Mercedes Long',
            '50',
            '5152 Jennifer Inlet Apt. 652, East Tonymouth, NM 24011',
            'contrerasmatthew@example.org'],
            ['Anne Walker', '37', 'USNV Ramirez, FPO AE 90740', 'hphillips@example.org']
        ]
        self.assertEqual(rows, expected)

        os.remove(result_path)

    def test_case_2(self):
        # 0 rows
        num_rows = 0
        result_path = f_696(self.file_path, num_rows)
        self.assertTrue(os.path.exists(result_path))
        with open(result_path, 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            self.assertEqual(len(rows), num_rows + 1)
        os.remove(result_path)

    def test_case_3(self):
        # large amount of rows
        num_rows = 1000
        result_path = f_696(self.file_path, num_rows)
        self.assertTrue(os.path.exists(result_path))
        df = pd.read_csv(result_path)
        self.assertTrue(df['Age'].between(20, 60, inclusive='both').all())
        self.assertTrue(df.shape == (1000, 4))
        os.remove(result_path)

    def test_case_4(self):
        #negative rows
        self.assertRaises(Exception, f_696, self.file_path, -2)
        self.assertRaises(Exception, f_696, self.file_path, 1.2)


if __name__ == "__main__":#
    run_tests()