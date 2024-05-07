import pandas as pd
import re

# Function to replace acronyms in DataFrame
def f_385(data, mapping):
    """
    Replace all acronyms in a DataFrame with their full words according to a provided dictionary.
    
    Requirements:
    - pandas
    - re

    Parameters:
    - data (dict): A dictionary where keys are column names and values are lists of strings.
    - mapping (dict): A dictionary where keys are acronyms and values are the full words.
    
    Returns:
    - pd.DataFrame: A DataFrame where all acronyms in string cells have been replaced with their full words.
    
    Examples:
    >>> data = {'text': ['NASA is great', 'I live in the USA']}
    >>> mapping = {'NASA': 'National Aeronautics and Space Administration', 'USA': 'United States of America'}
    >>> print(f_385(data, mapping))
                                                    text
    0  National Aeronautics and Space Administration ...
    1             I live in the United States of America
    """
    df = pd.DataFrame(data)
    pattern = re.compile(r'\b[A-Z]+\b')
    def replace_match(match):
        return mapping.get(match.group(0), match.group(0))
    df = df.applymap(lambda x: pattern.sub(replace_match, x) if isinstance(x, str) else x)
    return df

import unittest
# Unit tests for the f_385 function
class TestCases(unittest.TestCase):
    def test_acronyms_single_column(self):
        data = {'text': ['NASA rocks', 'Visit the USA']}
        mapping = {'NASA': 'National Aeronautics and Space Administration', 'USA': 'United States of America'}
        expected = pd.DataFrame({'text': ['National Aeronautics and Space Administration rocks', 'Visit the United States of America']})
        result = f_385(data, mapping)
        pd.testing.assert_frame_equal(result, expected)
    
    def test_acronyms_multiple_columns(self):
        data = {'col1': ['NASA exploration'], 'col2': ['Made in USA']}
        mapping = {'NASA': 'National Aeronautics and Space Administration', 'USA': 'United States of America'}
        expected = pd.DataFrame({'col1': ['National Aeronautics and Space Administration exploration'], 'col2': ['Made in United States of America']})
        result = f_385(data, mapping)
        pd.testing.assert_frame_equal(result, expected)
    
    def test_no_acronyms(self):
        data = {'text': ['A sunny day', 'A rainy night']}
        mapping = {'NASA': 'National Aeronautics and Space Administration'}
        expected = pd.DataFrame({'text': ['A sunny day', 'A rainy night']})
        result = f_385(data, mapping)
        pd.testing.assert_frame_equal(result, expected)
    
    def test_non_string_types(self):
        data = {'text': ['NASA mission', 2020, None]}
        mapping = {'NASA': 'National Aeronautics and Space Administration'}
        expected = pd.DataFrame({'text': ['National Aeronautics and Space Administration mission', 2020, None]})
        result = f_385(data, mapping)
        pd.testing.assert_frame_equal(result, expected)
    
    def test_empty_dataframe(self):
        data = {'text': []}
        mapping = {'NASA': 'National Aeronautics and Space Administration'}
        expected = pd.DataFrame({'text': []})
        result = f_385(data, mapping)
        pd.testing.assert_frame_equal(result, expected)
