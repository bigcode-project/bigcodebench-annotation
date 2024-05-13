import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from python_http_client.exceptions import HTTPError

def task_func(dir, api_key, recipient_email):
    """
    Get a list of files in a directory and send that list by e-mail to a specific recipient using a provided SendGrid API key.

    Parameters:
    - dir (str): The directory to list.
    - api_key (str): The SendGrid API key for authentication.
    - recipient_email (str): The email address of the recipient.

    Returns:
    - bool: True if the email was sent successfully. Specifically, a successful send is indicated by an HTTP status code in the 2xx range, which denotes success. False is returned if the directory does not exist.

    Raises:
    - FileNotFoundError: If the specified directory does not exist.
    - HTTPError: If an HTTP error occurs during the sending process.
    - Exception: For any other exceptions that may occur during the execution.

    Requirements:
    - os
    - sendgrid.SendGridAPIClient
    - sendgrid.helpers.mail.Mail
    - python_http_client.exceptions.HTTPError

    Example:
    >>> isinstance(task_func('./test_directory', 'YOUR_SENDGRID_API_KEY', 'YOUR_EMAIL'), bool)
    True
    >>> task_func('/nonexistent_directory', 'YOUR_SENDGRID_API_KEY', 'YOUR_EMAIL')  # This will return False, as the directory does not exist.
    False
    """
    try:
        file_list = os.listdir(dir)
    except:
        raise FileNotFoundError(f"Directory '{dir}' does not exist.")
    file_list_str = ', '.join(file_list)
    message = Mail(
        from_email='from_email@example.com',
        to_emails=recipient_email,
        subject=f'Directory Listing for {dir}',
        plain_text_content=file_list_str)
    try:
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)
        return 200 <= response.status_code < 300
    except HTTPError as e:
        print(f"HTTP error occurred: {e}")
        raise
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

import unittest
from unittest.mock import patch, MagicMock, Mock
import os
from python_http_client.exceptions import HTTPError
class TestCases(unittest.TestCase):
    @patch('os.path.exists')
    @patch('sendgrid.SendGridAPIClient.send')
    @patch('os.listdir')
    def test_successful_email_send(self, mock_listdir, mock_send, mock_exists):
        """Test successful email sending with a valid directory."""
        mock_listdir.return_value = ['file1.gz', 'file2.gz']
        mock_exists.return_value = True
        mock_send.return_value = MagicMock(status_code=202)
        
        api_key = 'test_api_key'
        recipient_email = 'test@example.com'
        result = task_func('./valid_directory', api_key, recipient_email)
        self.assertTrue(result)
    def test_invalid_directory(self):
        """Test the handling of an invalid directory."""
        api_key = 'test_api_key'
        recipient_email = 'test@example.com'
        with self.assertRaises(FileNotFoundError):
            task_func('/nonexistent_directory', api_key, recipient_email)
        
    @patch('os.path.exists')
    @patch('os.listdir')
    @patch('sendgrid.SendGridAPIClient.send')
    def test_failed_email_send(self, mock_send, mock_listdir, mock_exists):
        """Test handling of a failed email send by ensuring HTTPError is raised."""
        mock_listdir.return_value = ['file1.gz', 'file2.gz']
        mock_response = Mock(status_code=400, body='Bad Request')
        mock_exists.return_value = True
        mock_send.side_effect = HTTPError(mock_response, 'Failed to send')
        api_key = 'test_api_key'
        recipient_email = 'test@example.com'
        with self.assertRaises(HTTPError):
            task_func('./valid_directory', api_key, recipient_email)
    @patch('os.path.exists')
    @patch('sendgrid.SendGridAPIClient.send')
    @patch('os.listdir')
    def test_empty_directory(self, mock_listdir, mock_send, mock_exists):
        """Test sending an email with an empty directory."""
        mock_listdir.return_value = []
        mock_send.return_value = MagicMock(status_code=202)
        mock_exists.return_value = True
        api_key = 'test_api_key'
        recipient_email = 'test@example.com'
        result = task_func('./empty_directory', api_key, recipient_email)
        self.assertTrue(result)
    @patch('os.path.exists')
    @patch('sendgrid.SendGridAPIClient.send')
    @patch('os.listdir')
    def test_generic_exception_handling(self, mock_listdir, mock_send, mock_exists):
        """Test handling of generic exceptions during email sending."""
        mock_listdir.return_value = ['file1.gz', 'file2.gz']
        mock_send.side_effect = Exception('Generic error')
        mock_exists.return_value = True
        api_key = 'test_api_key'
        recipient_email = 'test@example.com'
        with self.assertRaises(Exception):
            task_func('./valid_directory', api_key, recipient_email)
