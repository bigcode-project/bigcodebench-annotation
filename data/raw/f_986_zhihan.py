import re
import hashlib

def f_986(input_str):
    """
    Remove all special characters, punctuation marks, and spaces from a regular-expression input _ str string, 
    and then hash the cleaned string with SHA256.

    Parameters:
    input_str (str): The input string.

    Returns:
    str: The hashed string.

    Requirements:
    - re
    - hashlib

    Example:
    >>> f_986('Special $#! characters   spaces 888323')
    '6dcd4ce23d88e2ee9568ba546c007c63d9131f1b8b062b36c5bbf7bb0e0fda09'
    """
    cleaned_str = re.sub('[^A-Za-z0-9]+', '', input_str)
    hashed_str = hashlib.sha256(cleaned_str.encode()).hexdigest()

    return hashed_str

import unittest
import re
import hashlib

# Function f_986 definition
def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):

    def test_case_1(self):
        result = f_986('Special $#! characters   spaces 888323')
        expected = 'af30263c4d44d67917a4f0727191a4149e1ab615b772b2aeda859068178b146c'
        self.assertEqual(result, expected)

    def test_case_2(self):
        result = f_986('Hello World!')
        expected = '872e4e50ce9990d8b041330c47c9ddd11bec6b503ae9386a99da8584e9bb12c4'
        self.assertEqual(result, expected)

    def test_case_3(self):
        result = f_986('1234567890')
        expected = 'c775e7b757ede630cd0aa1113bd102661ab38829ca52a6422ab782862f268646'
        self.assertEqual(result, expected)

    def test_case_4(self):
        result = f_986('')
        expected = 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
        self.assertEqual(result, expected)

    def test_case_5(self):
        result = f_986('OpenAI')
        expected = '8b7d1a3187ab355dc31bc683aaa71ab5ed217940c12196a9cd5f4ca984babfa4'
        self.assertEqual(result, expected)
if __name__ == "__main__":
    run_tests()