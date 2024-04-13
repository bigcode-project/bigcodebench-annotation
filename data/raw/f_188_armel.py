import pandas as pd
import os
import hashlib
import base64

def f_188(directory_path: str) -> pd.DataFrame:
    """
    Create a Pandas DataFrame that contains the file names and their encoded hash values for all files in a specified directory.
    
    Parameters:
    - directory_path (str): The path to the directory containing the files.
    
    Returns:
    - pandas.DataFrame: A pandas DataFrame with two columns: 'File Name' and 'Encoded Hash', containing file names (not the paths) and their respective encoded hash values.
    
    Requirements:
    - pandas
    - os
    - hashlib
    - base64
    
    Example:
    >>> df = f_188("/path/to/directory")
    >>> print(df)
        File Name    Encoded Hash
    0   sample.txt   AbCdEf1234567...
   """
    file_list = os.listdir(directory_path)
    data = []
    
    for file in file_list:
        with open(os.path.join(directory_path, file), 'rb') as f:
            bytes_ = f.read()
            readable_hash = hashlib.sha256(bytes_).digest()
            encoded_hash = base64.b64encode(readable_hash).decode('ascii')
            data.append([os.path.basename(file), encoded_hash])
    
    df = pd.DataFrame(data, columns=['File Name', 'Encoded Hash'])
    return df

import unittest
import pandas as pd
import os
import hashlib
import base64
from unittest.mock import patch

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    """Test cases for the f_188 function.""" 
    def setUp(self):
        self.test_dir = "data/f_188"
        os.makedirs(self.test_dir, exist_ok=True)

        self.dir_1 = os.path.join(self.test_dir, "dir_1")
        os.makedirs(self.dir_1, exist_ok=True)
        # 4 files
        for i in range(4):
            with open(os.path.join(self.dir_1, f"file_{i+1}.txt"), "w") as f:
                f.write(f"This is the content of file {i+1}")

        self.dir_2 = os.path.join(self.test_dir, "dir_2")
        os.makedirs(self.dir_2, exist_ok=True)
        # 4 files
        for i in range(2):
            with open(os.path.join(self.dir_2, f"file_{i+1}.txt"), "w") as f:
                f.write(f"Different content for file {i+1}")

        self.dir_3 = os.path.join(self.test_dir, "dir_3")
        os.makedirs(self.dir_3, exist_ok=True)
        with open(os.path.join(self.dir_3, "image_1.jpg"), "w") as f :
            f.write("Some binary data representing an image")
        
        self.dir_4 = os.path.join(self.test_dir, "dir_4")
        os.makedirs(self.dir_4, exist_ok=True)
        with open(os.path.join(self.dir_4, "note_1.md"), "w") as f :
            f.write("# This is a markdown note")
        
        self.dir_5 = os.path.join(self.test_dir, "dir_5")
        os.makedirs(self.dir_5, exist_ok=True)
        
    def test_case_1(self):
        df = f_188(self.dir_1)
        self.assertEqual(len(df), 4, "Number of rows in the DataFrame should be 4.")
        self.assertListEqual(list(df.columns), ['File Name', 'Encoded Hash'], "Column names mismatch.")
        file_content = "This is the content of file 1".encode('utf-8')
        expected_hash = base64.b64encode(hashlib.sha256(file_content).digest()).decode('ascii')
        computed_hash = df[df['File Name'] == "file_1.txt"]['Encoded Hash'].values[0]
        self.assertEqual(expected_hash, computed_hash, f"Hash values mismatch for {os.path.join(self.dir_1, 'file_1.txt')}")
    
    def test_case_2(self):
        df = f_188(self.dir_2)
        file_content = "Different content for file 2".encode('utf-8')
        expected_hash = base64.b64encode(hashlib.sha256(file_content).digest()).decode('ascii')
        computed_hash = df[df['File Name'] == "file_2.txt"]['Encoded Hash'].values[0]
        self.assertEqual(expected_hash, computed_hash, "Hash values mismatch for f_188_data_jean/file2.txt")
    
    def test_case_3(self):
        df = f_188(self.dir_3)
        file_content = "Some binary data representing an image".encode('utf-8')
        expected_hash = base64.b64encode(hashlib.sha256(file_content).digest()).decode('ascii')
        computed_hash = df[df['File Name'] == "image_1.jpg"]['Encoded Hash'].values[0]
        self.assertEqual(expected_hash, computed_hash, f"Hash values mismatch for {os.path.join(self.dir_1, 'image_1.jpg')}")
    
    def test_case_4(self):
        df = f_188(self.dir_4)
        file_content = "# This is a markdown note".encode('utf-8')
        expected_hash = base64.b64encode(hashlib.sha256(file_content).digest()).decode('ascii')
        computed_hash = df[df['File Name'] == "note_1.md"]['Encoded Hash'].values[0]
        self.assertEqual(expected_hash, computed_hash, "Hash values mismatch for f_188_data_jean/note.md")
    
    def test_case_5(self):
        df = f_188(self.dir_5)
        self.assertEqual(len(df), 0, "DataFrame should be empty for an empty directory.")

if __name__ == "__main__" :
    run_tests()