import collections
import json
import requests

def task_func(user, API_URL = 'https://api.github.com/users/'):
    """
    Retrieves the names of the repositories of a specified GitHub user, sorted in ascending order by their creation date.

    The function queries the GitHub API for all repositories of a given user, parses the response to extract the names and creation dates, and returns the repository names sorted by the date they were created.

    Parameters:
    - user (str): The GitHub username whose repositories are to be retrieved.
    - API_URL (str): The base URL of the GitHub API. Default is 'https://api.github.com/users/'.

    Returns:
    - list of str: A list of repository names, sorted by their creation dates from oldest to newest.


    Requirements:
    - collections
    - json
    - requests

    Example:
    >>> task_func('octocat')
    ['Spoon-Knife', 'Hello-World', 'octocat.github.io']  # Example output, actual results may vary.
    """
    response = requests.get(API_URL + user + '/repos')
    data = json.loads(response.text)
    repos = {repo['name']: repo['created_at'] for repo in data}
    sorted_repos = collections.OrderedDict(sorted(repos.items(), key=lambda x: x[1]))
    return list(sorted_repos.keys())

import unittest
from unittest.mock import patch, Mock
import json
class TestCases(unittest.TestCase):
    def setUp(self):
        self.mock_response_with_multiple_repos = json.dumps([
        {"name": "Repo1", "created_at": "2021-01-01T00:00:00Z"},
        {"name": "Repo2", "created_at": "2021-01-02T00:00:00Z"}
    ])
        self.mock_response_with_single_repo = json.dumps([
        {"name": "SingleRepo", "created_at": "2021-01-01T00:00:00Z"}
    ])
        self.mock_response_with_no_repos = json.dumps([])
    @patch('requests.get')
    def test_case_1(self, mock_get):
        # Test if the function returns a list
        mock_get.return_value = Mock(status_code=200, text=self.mock_response_with_multiple_repos)
        result = task_func('octocat')
        self.assertIsInstance(result, list, "The returned value should be a list.")
    @patch('requests.get')
    def test_case_2(self, mock_get):
        # Test for a user with multiple repositories
        mock_get.return_value = Mock(status_code=200, text=self.mock_response_with_multiple_repos)
        result = task_func('octocat')
        self.assertTrue(len(result) > 1, "The user 'octocat' should have more than one repository.")
    @patch('requests.get')
    def test_case_3(self, mock_get):
        # Test for a user with no repositories
        mock_get.return_value = Mock(status_code=200, text=self.mock_response_with_no_repos)
        result = task_func('dummyuserwithnorepos')
        self.assertEqual(len(result), 0, "The user 'dummyuserwithnorepos' should have zero repositories.")
    @patch('requests.get')
    def test_case_4(self, mock_get):
        # Test for a non-existent user
        mock_get.return_value = Mock(status_code=404, text=self.mock_response_with_no_repos)
        result = task_func('nonexistentuserxyz')
        self.assertEqual(len(result), 0, "A non-existent user should have zero repositories.")
    @patch('requests.get')
    def test_case_5(self, mock_get):
        # Test for a user with a single repository
        mock_get.return_value = Mock(status_code=200, text=self.mock_response_with_single_repo)
        result = task_func('userwithonerepo')
        self.assertEqual(len(result), 1, "The user 'userwithonerepo' should have one repository.")
