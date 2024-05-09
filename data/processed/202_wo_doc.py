import subprocess
from multiprocessing import Pool

def execute_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, _ = process.communicate()
    return output

def task_func(commands):
    """
    Executes a list of shell commands in parallel using multiprocessing, and collects their outputs.
    
    Parameters:
        commands (list): A list of shell commands to be executed.

    Returns:
        list: A list of byte strings, each representing the output of a command. Returns an empty list if `commands` is empty.

    Requirements:
    - subprocess
    - multiprocessing.Pool

    Notes:
    - If `commands` is an empty list, the function returns an empty list without attempting to execute any commands.
    
    Examples:
    >>> result = task_func(['ls', 'pwd', 'date'])
    >>> isinstance(result, list)
    True
    >>> all(isinstance(output, bytes) for output in result)
    True
    """
    if not commands:  # Handle case where commands list is empty
        return []
    with Pool(processes=len(commands)) as pool:
        outputs = pool.map(execute_command, commands)
    return outputs

import unittest
from unittest.mock import patch
class TestCases(unittest.TestCase):
    @patch('subprocess.Popen')
    def test_return_type(self, mock_popen):
        """Test that the function returns a list of byte strings."""
        mock_popen.return_value.communicate.return_value = (b'output', b'')
        commands = ['ls']
        result = task_func(commands)
        self.assertIsInstance(result, list)
        self.assertTrue(all(isinstance(output, bytes) for output in result))
    @patch('subprocess.Popen')
    def test_empty_command_list(self, mock_popen):
        """Test the function with an empty command list."""
        mock_popen.return_value.communicate.return_value = (b'', b'')
        result = task_func([])
        self.assertEqual(result, [])
        mock_popen.assert_not_called()
    @patch('subprocess.Popen')
    def test_return_type_with_mocked_commands(self, mock_popen):
        """Test that the function returns a list with mocked commands."""
        mock_popen.return_value.communicate.return_value = (b'Hello', b''), (b'World', b'')
        commands = ['echo "Hello"', 'echo "World"']
        result = task_func(commands)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)
    @patch('subprocess.Popen')
    def test_handling_specific_number_of_commands(self, mock_popen):
        """Test the function with a specific number of commands."""
        mock_popen.return_value.communicate.side_effect = [(b'output1', b''), (b'output2', b'')]
        commands = ['ls', 'pwd']
        result = task_func(commands)
        self.assertEqual(len(result), 2)
    @patch('subprocess.Popen')
    def test_handling_empty_string_command(self, mock_popen):
        """Test the function with an empty string as a command."""
        mock_popen.return_value.communicate.return_value = (b'', b'')
        commands = ['']
        result = task_func(commands)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], b'')
