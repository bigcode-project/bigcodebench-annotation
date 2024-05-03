import subprocess
import csv
import os

def f_1015(commands_file_path, output_dir_path):
    """
    Read a list of shell commands from a given CSV file and execute them using subprocess.
    Save the output of each command to a separate file in the specified output directory.

    Parameters:
    - commands_file_path (str): Path to the CSV file containing the shell commands. The file should not have headers.
    - output_dir_path (str): Path to the directory where the command outputs will be saved.

    Requirements:
    - subprocess
    - csv
    - os

    Returns:
    - list: A list of filenames present in the output directory.

    Example:
    >>> f_1015("commands.csv", "/path/to/output_directory")
    ['command_1_output.txt', 'command_2_output.txt', ...]
    """
    # Check if commands_file_path exists
    if not os.path.exists(commands_file_path):
        raise FileNotFoundError(f"File '{commands_file_path}' not found.")
    
    # Check if output_dir_path exists, if not, create it
    if not os.path.exists(output_dir_path):
        os.makedirs(output_dir_path)
    
    # Read commands from the CSV file
    with open(commands_file_path, 'r') as f:
        reader = csv.reader(f)
        commands = [cmd[0] for cmd in list(reader)]
    
    # Execute each command and save its output
    for i, command in enumerate(commands):
        output_file = f'{output_dir_path}/command_{i+1}_output.txt'
        with open(output_file, 'w') as f:
            try:
                subprocess.call(command, shell=True, stdout=f, stderr=f)
            except Exception as e:
                f.write(f"Error executing command: {e}")
    
    return os.listdir(output_dir_path)

import unittest
import shutil
import os
import csv


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    
    # Path for saving outputs
    output_dir_path = "/mnt/data/test_output_dir"
    
    def setUp(self):
        # Cleanup any existing output directory before each test
        if os.path.exists(self.output_dir_path):
            shutil.rmtree(self.output_dir_path)
    
    def test_case_1(self):
        result = f_1015(mock_csv_path, self.output_dir_path)
        self.assertEqual(len(result), 3)
        expected_files = ['command_1_output.txt', 'command_2_output.txt', 'command_3_output.txt']
        self.assertCountEqual(result, expected_files)
        
    def test_case_2(self):
        with self.assertRaises(FileNotFoundError):
            f_1015("invalid_path.csv", self.output_dir_path)

    def test_case_3(self):
        with open("/mnt/data/invalid_command.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["invalid_command_xyz"])
        
        result = f_1015("/mnt/data/invalid_command.csv", self.output_dir_path)
        self.assertEqual(len(result), 1)
        with open(f"{self.output_dir_path}/{result[0]}", "r") as f:
            content = f.read()
            self.assertIn("Error executing command:", content)
    
    def test_case_4(self):
        with open("/mnt/data/empty.csv", "w", newline='') as file:
            pass
        
        result = f_1015("/mnt/data/empty.csv", self.output_dir_path)
        self.assertEqual(len(result), 0)
    
    def test_case_5(self):
        with open("/mnt/data/mixed_commands.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["echo Mixed Commands"])
            writer.writerow(["invalid_command_abc"])
        
        result = f_1015("/mnt/data/mixed_commands.csv", self.output_dir_path)
        self.assertEqual(len(result), 2)
        with open(f"{self.output_dir_path}/{result[1]}", "r") as f:
            content = f.read()
            self.assertIn("Error executing command:", content)
if __name__ == "__main__":
    run_tests()