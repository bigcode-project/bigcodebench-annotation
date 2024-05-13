import xlwt
import os

# Constants
FIELDS = ['ID', 'Name', 'Age']

def task_func(values, filename):
    """
    Writes a list of OrderedDicts to an Excel file. Each OrderedDict in the list represents a row in the Excel sheet,
    and each key in the OrderedDict corresponds to a column defined in the FIELDS constant comprising column names 
    'ID', 'Name', and 'Age'.

    Parameters:
    values (list of OrderedDict): A list where each element is an OrderedDict with keys matching the FIELDS constant.
    filename (str): The filename for the Excel file to be created. It should include the '.xls' extension.

    Returns:
    str: The absolute path of the created Excel file.

    Requirements:
    - xlwt
    - os

    Examples:
    Create an Excel file with data from a list of OrderedDicts.
    >>> data = [OrderedDict([('ID', 1), ('Name', 'John Doe'), ('Age', 30)]),
    ...         OrderedDict([('ID', 2), ('Name', 'Jane Doe'), ('Age', 28)])]
    >>> path = task_func(data, 'test_data.xls')
    >>> os.path.exists(path) and 'test_data.xls' in path
    True

    Create an Excel file with no data.
    >>> empty_data = []
    >>> path = task_func(empty_data, 'empty_data.xls')
    >>> os.path.exists(path) and 'empty_data.xls' in path
    True
    """

    book = xlwt.Workbook()
    sheet1 = book.add_sheet("persons")
    for col_index, col in enumerate(FIELDS):
        sheet1.write(0, col_index, col)
    for row_index, row_values in enumerate(values, 1):
        for col_index, col in enumerate(FIELDS):
            value = row_values.get(col, "")
            sheet1.write(row_index, col_index, value)
    book.save(filename)
    return os.path.abspath(filename)

import unittest
import os
import tempfile
from collections import OrderedDict
# Assume task_func is imported or defined elsewhere
class TestCases(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory to store test files
        self.test_dir = tempfile.TemporaryDirectory()
    def tearDown(self):
        # Cleanup the temporary directory after tests
        self.test_dir.cleanup()
    def test_ordered_dict_to_excel(self):
        values = [OrderedDict([('ID', 1), ('Name', 'John Doe'), ('Age', 30)]),
                  OrderedDict([('ID', 2), ('Name', 'Jane Doe'), ('Age', 28)])]
        filename = os.path.join(self.test_dir.name, 'test_data.xls')
        result_path = task_func(values, filename)
        self.assertTrue(os.path.isfile(result_path))
    def test_empty_data_to_excel(self):
        values = []
        filename = os.path.join(self.test_dir.name, 'empty_data.xls')
        result_path = task_func(values, filename)
        self.assertTrue(os.path.isfile(result_path))
    def test_incomplete_data_to_excel(self):
        values = [OrderedDict([('ID', 1), ('Name', 'John Doe')])]
        filename = os.path.join(self.test_dir.name, 'incomplete_data.xls')
        result_path = task_func(values, filename)
        self.assertTrue(os.path.isfile(result_path))
    def test_mismatched_fields(self):
        values = [OrderedDict([('ID', 1), ('Name', 'John Doe'), ('Gender', 'Male')])]
        filename = os.path.join(self.test_dir.name, 'mismatched_fields.xls')
        result_path = task_func(values, filename)
        self.assertTrue(os.path.isfile(result_path))
    def test_multiple_rows(self):
        values = [OrderedDict([('ID', i), ('Name', f'Name {i}'), ('Age', 20+i)]) for i in range(5)]
        filename = os.path.join(self.test_dir.name, 'multiple_rows.xls')
        result_path = task_func(values, filename)
        self.assertTrue(os.path.isfile(result_path))
