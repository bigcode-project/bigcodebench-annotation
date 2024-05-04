import json
import smtplib

# Constants
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your.email@gmail.com"
EMAIL_PASSWORD = "your.password"

def f_95(input_data=None, smtp_server=SMTP_SERVER, smtp_port=SMTP_PORT, email_address=EMAIL_ADDRESS, email_password=EMAIL_PASSWORD, smtp=None):
    """
    Extract recepient email address and names from JSON-formatted string and send the names in an email. The sent message should be in the format 'Subject: Extracted Names\n\nName1\nName2\n...'.

    Parameters:
    input_data (str): JSON-formatted string containing the recipient email address and the list of names.
    smtp_server (str): The SMTP server to use for sending the email.
    smtp_port (int): The port to use for the SMTP server.
    email_address (str): The email address from which to send the email.
    email_password (str): The password for the email address.
    
    Returns:
    list: A list of extracted names.
    
    Requirements:
    - re
    - smtplib

    Example:
    >>> from unittest.mock import MagicMock
    >>> mock_smtp_instance = MagicMock()
    >>> mock_smtp = MagicMock(return_value=mock_smtp_instance)
    >>> f_95('{"recipient": "recipient@example.com", "names": ["Josie Smith", "Mugsy Dog Smith"]}', smtp=mock_smtp)
    ['Josie Smith', 'Mugsy Dog Smith']
    """
    if input_data is None:
        return []
    try:
        data = json.loads(input_data)
        recipient_email = data.get('recipient')
        names = data.get('names', [])
    except (json.JSONDecodeError, ValueError):
        return []
    if not recipient_email or not names:
        return []
    message = 'Subject: Extracted Names\n\n' + '\n'.join(names)
    if smtp:
        server = smtp(smtp_server, smtp_port)
    else:
        server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(email_address, email_password)
    server.sendmail(email_address, recipient_email, message)
    server.quit()
    return names

import unittest
from unittest.mock import patch, MagicMock
import smtplib
class TestCases(unittest.TestCase):
    @patch('smtplib.SMTP')
    def test_f225(self, mock_smtp):
        mock_smtp_instance = MagicMock()
        mock_smtp.return_value = mock_smtp_instance
        
        # Call the function
        result = f_95('{"recipient": "recipient@example.com", "names": ["Josie Smith", "Mugsy Dog Smith"]}')
        
        # Assert that SMTP was called with the right parameters
        mock_smtp.assert_called_once_with('smtp.gmail.com', 587)
        # Assert the return value
        self.assertEqual(result, ['Josie Smith', 'Mugsy Dog Smith'])
    @patch('smtplib.SMTP')
    def test_f225_subject(self, mock_smtp):
        # Create a MagicMock instance to replace the SMTP instance
        mock_smtp_instance = MagicMock()
        mock_smtp.return_value = mock_smtp_instance
        
        # Call the function
        result = f_95('{"recipient": "names@gmail.com", "names": ["Josie Smith", "Mugsy Dog Smith"]}')
        
        # Assert that SMTP was called with the right parameters
        mock_smtp.assert_called_once_with('smtp.gmail.com', 587)
        # Assert that starttls, login, sendmail, and quit were called on the SMTP instance
        mock_smtp_instance.login.assert_called_once_with('your.email@gmail.com', 'your.password')
        mock_smtp_instance.sendmail.assert_called_once_with('your.email@gmail.com', 'names@gmail.com', 'Subject: Extracted Names\n\nJosie Smith\nMugsy Dog Smith')
        
        # Assert the return value
        self.assertEqual(result, ['Josie Smith', 'Mugsy Dog Smith'])
    
    @patch('smtplib.SMTP')
    def test_no_names(self, mock_smtp):
        # Create a MagicMock instance to replace the SMTP instance
        mock_smtp_instance = MagicMock()
        mock_smtp.return_value = mock_smtp_instance
        # Custom input text with no names
        custom_text = '{"recipient": "names@gmail.com", "names": []}'
        
        # Call the function with custom input
        result = f_95(input_data=custom_text)
        # Assert the return value
        self.assertEqual(result, [])
    @patch('smtplib.SMTP')
    def test_recepient(self, mock_smtp):
        # Create a MagicMock instance to replace the SMTP instance
        mock_smtp_instance = MagicMock()
        mock_smtp.return_value = mock_smtp_instance
        # Custom input text with no names
        custom_text = '{"recipient": "change@gmail.com", "names": []}'
        
        # Call the function with custom input
        result = f_95(input_data=custom_text)
        
        # Assert the return value
        self.assertEqual(result, [])
    @patch('smtplib.SMTP')
    def test_login(self, mock_smtp):
        # Create a MagicMock instance to replace the SMTP instance
        mock_smtp_instance = MagicMock()
        mock_smtp.return_value = mock_smtp_instance
        # Custom input text with no names
        custom_text = '{"recipient": "change@gmail.com", "names": ["Name 1", "Name 2"]}'
        
        # Call the function with custom input
        result = f_95(input_data=custom_text, email_address="your.email.change@gmail.com", email_password="your.password.change")
        
        # Assert that SMTP was called with the right parameters
        mock_smtp.assert_called_once_with('smtp.gmail.com', 587)
        # Assert that starttls, login, sendmail, and quit were called on the SMTP instance
        mock_smtp_instance.login.assert_called_once_with('your.email.change@gmail.com', 'your.password.change')
        # Assert the return value
        self.assertEqual(result, ["Name 1", "Name 2"])
