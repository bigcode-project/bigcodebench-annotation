import pandas as pd
import re

# Function to replace acronyms in DataFrame
def f_760(df, mapping):
    """
    Replace all acronyms in a DataFrame with their full words according to a provided dictionary.
    
    Requirements:
    - pandas
    - re

    Parameters:
    - df (pd.DataFrame): The input DataFrame where each cell is either a string or non-string type.
    - mapping (dict): A dictionary where keys are acronyms and values are the full words.
    
    Returns:
    - pd.DataFrame: A DataFrame where all acronyms in string cells have been replaced with their full words.
    
    Examples:
    >>> df = pd.DataFrame({'text': ['NASA is great', 'I live in the USA']})
    >>> mapping = {'NASA': 'National Aeronautics and Space Administration', 'USA': 'United States of America'}
    >>> print(f_760(df, mapping))
                                                    text
    0  National Aeronautics and Space Administration ...
    1             I live in the United States of America
    """
    pattern = re.compile(r'\b[A-Z]+\b')
    
    def replace_match(match):
        return mapping.get(match.group(0), match.group(0))

    df = df.applymap(lambda x: pattern.sub(replace_match, x) if isinstance(x, str) else x)

    return df

import unittest
# Unit tests for the f_760 function
class ReplaceAcronymsTests(unittest.TestCase):
    def test_acronyms_single_column(self):
        df = pd.DataFrame({'text': ['NASA rocks', 'Visit the USA']})
        mapping = {'NASA': 'National Aeronautics and Space Administration', 'USA': 'United States of America'}
        expected = pd.DataFrame({'text': ['National Aeronautics and Space Administration rocks', 'Visit the United States of America']})
        result = f_760(df, mapping)
        pd.testing.assert_frame_equal(result, expected)
    
    def test_acronyms_multiple_columns(self):
        df = pd.DataFrame({'col1': ['NASA exploration'], 'col2': ['Made in USA']})
        mapping = {'NASA': 'National Aeronautics and Space Administration', 'USA': 'United States of America'}
        expected = pd.DataFrame({'col1': ['National Aeronautics and Space Administration exploration'], 'col2': ['Made in United States of America']})
        result = f_760(df, mapping)
        pd.testing.assert_frame_equal(result, expected)
    
    def test_no_acronyms(self):
        df = pd.DataFrame({'text': ['A sunny day', 'A rainy night']})
        mapping = {'NASA': 'National Aeronautics and Space Administration'}
        expected = pd.DataFrame({'text': ['A sunny day', 'A rainy night']})
        result = f_760(df, mapping)
        pd.testing.assert_frame_equal(result, expected)
    
    def test_non_string_types(self):
        df = pd.DataFrame({'text': ['NASA mission', 2020, None]})
        mapping = {'NASA': 'National Aeronautics and Space Administration'}
        expected = pd.DataFrame({'text': ['National Aeronautics and Space Administration mission', 2020, None]})
        result = f_760(df, mapping)
        pd.testing.assert_frame_equal(result, expected)
    
    def test_empty_dataframe(self):
        df = pd.DataFrame({'text': []})
        mapping = {'NASA': 'National Aeronautics and Space Administration'}
        expected = pd.DataFrame({'text': []})
        result = f_760(df, mapping)
        pd.testing.assert_frame_equal(result, expected)
