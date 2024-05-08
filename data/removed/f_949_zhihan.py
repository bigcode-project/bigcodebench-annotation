import subprocess
import os
import shutil
from datetime import datetime

def f_949(r_script_path='/pathto/MyrScript.r', backup_path='/backup/'):
    """Executes the provided R script and then backs it up to the specified backup directory with the current date appended to its name.
    
    Parameters:
    - r_script_path (str): The path to the R script that needs to be executed. Default is '/pathto/MyrScript.r'.
    - backup_path (str): The directory where the R script will be backed up. Default is '/backup/'.
    
    Returns:
    int: The subprocess.call return value (0 for success, non-zero for failure).
    
    Requirements:
    - subprocess
    - os
    - shutil
    - datetime
    
    Example:
    >>> f_949(r_script_path='/pathto/MyrScript1.r', backup_path='/backup_folder/')
    0
    >>> f_949()
    0
    """
    ret_val = subprocess.call('/usr/bin/Rscript --vanilla ' + r_script_path, shell=True)

    today = datetime.now().strftime('%Y%m%d')
    backup_file = os.path.join(backup_path, 'MyrScript_' + today + '.r')
    shutil.copy(r_script_path, backup_file)

    return ret_val

import unittest
import os
from unittest.mock import patch
from datetime import datetime

# Including the refined function definition for testing

import subprocess
import os
import shutil
from datetime import datetime

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    
    @patch('subprocess.call', return_value=0)
    def test_case_1(self, mock_subprocess):
        # Testing with default parameters
        result = f_949()
        self.assertEqual(result, 0)
        backup_file = os.path.join('/backup/', 'MyrScript_' + datetime.now().strftime('%Y%m%d') + '.r')
        self.assertTrue(os.path.exists(backup_file))
    
    @patch('subprocess.call', return_value=1)
    def test_case_2(self, mock_subprocess):
        # Testing with a failure return from subprocess and custom paths
        result = f_949(r_script_path='/pathto/AnotherScript.r', backup_path='/custom_backup/')
        self.assertEqual(result, 1)
        backup_file = os.path.join('/custom_backup/', 'MyrScript_' + datetime.now().strftime('%Y%m%d') + '.r')
        self.assertTrue(os.path.exists(backup_file))

    @patch('subprocess.call', return_value=0)
    def test_case_3(self, mock_subprocess):
        # Testing with a different R script path
        result = f_949(r_script_path='/different_path/Script.r')
        self.assertEqual(result, 0)
        backup_file = os.path.join('/backup/', 'MyrScript_' + datetime.now().strftime('%Y%m%d') + '.r')
        self.assertTrue(os.path.exists(backup_file))
        
    @patch('subprocess.call', return_value=0)
    def test_case_4(self, mock_subprocess):
        # Testing with a different backup path
        result = f_949(backup_path='/another_backup/')
        self.assertEqual(result, 0)
        backup_file = os.path.join('/another_backup/', 'MyrScript_' + datetime.now().strftime('%Y%m%d') + '.r')
        self.assertTrue(os.path.exists(backup_file))
        
    @patch('subprocess.call', return_value=0)
    def test_case_5(self, mock_subprocess):
        # Testing with both R script and backup path changed
        result = f_949(r_script_path='/path/ToScript.r', backup_path='/new_backup/')
        self.assertEqual(result, 0)
        backup_file = os.path.join('/new_backup/', 'MyrScript_' + datetime.now().strftime('%Y%m%d') + '.r')
        self.assertTrue(os.path.exists(backup_file))
if __name__ == "__main__":
    run_tests()