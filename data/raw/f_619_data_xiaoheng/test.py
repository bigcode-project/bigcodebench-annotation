
import unittest
from configparser import ConfigParser
from function import f_103

class TestCases(unittest.TestCase):
    def setUp(self):
        # Create a temporary configuration file for testing
        self.temp_config_file = 'temp_config.ini'
        config = ConfigParser()
        config['DEFAULT'] = {'setting1': 'value1', 'setting2': 'value2'}
        with open(self.temp_config_file, 'w') as file:
            config.write(file)

    def tearDown(self):
        # Clean up the temporary configuration file after testing
        import os
        os.remove(self.temp_config_file)

    def test_append_path_and_update_config(self):
        new_path = '/path/to/test/directory'
        updated_config, config_file_path = f_103(new_path, self.temp_config_file)
        
        # Check if the new path is in sys.path
        self.assertIn(new_path, sys.path)
        
        # Check if the configuration file has been updated correctly
        self.assertEqual(updated_config['DEFAULT']['path_to_append'], new_path)
        self.assertEqual(config_file_path, self.temp_config_file)

    # Additional test cases can be added here

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)
