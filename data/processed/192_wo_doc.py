import re
import smtplib

# Constants
TEXT = "Josie Smith [3996 COLLEGE AVENUE, SOMETOWN, MD 21003]Mugsy Dog Smith [2560 OAK ST, GLENMEADE, WI 14098]"
RECEPIENT_ADDRESS = "names@gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your.email@gmail.com"
EMAIL_PASSWORD = "your.password"

def task_func(text=TEXT, smtp_server=SMTP_SERVER, smtp_port=SMTP_PORT, email_address=EMAIL_ADDRESS, email_password=EMAIL_PASSWORD, recepient_address=RECEPIENT_ADDRESS, smtp=None):
    """
    Extract all names from a string that is not enclosed by square brackets and send the names in an email.

    Parameters:
    text (str): The text from which to extract names.
    smtp_server (str): The SMTP server to use for sending the email.
    smtp_port (int): The port to use for the SMTP server.
    email_address (str): The email address from which to send the email.
    email_password (str): The password for the email address.
    recepient_address (str): The recepient email adress.
    
    Returns:
    list: A list of extracted names.
    
    Note:
    - The message in the email is formatted in "Subject: Extracted Names\n\n" with the extracted name "\nJosie Smith\nMugsy Dog Smith".

    Requirements:
    - re
    - smtplib

    Example:
    >>> from unittest.mock import MagicMock
    >>> mock_smtp_instance = MagicMock()
    >>> mock_smtp = MagicMock(return_value=mock_smtp_instance)
    >>> task_func(text="Josie Smith [3996 COLLEGE AVENUE, SOMETOWN, MD 21003]Mugsy Dog Smith [2560 OAK ST, GLENMEADE, WI 14098]", smtp=mock_smtp)
    ['Josie Smith', 'Mugsy Dog Smith']
    """
    names = re.findall('(.*?)(?:\\[.*?\\]|$)', text)
    names = [name.strip() for name in names if name != ""]
    message = 'Subject: Extracted Names\n\n' + '\n'.join(names)
    if smtp:
        server = smtp(smtp_server, smtp_port)
    else:
        server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(email_address, email_password)
    server.sendmail(email_address, recepient_address, message)
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
        result = task_func()
        
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
        result = task_func()
        
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
        custom_text = "[No names enclosed by square brackets]"
        
        # Call the function with custom input
        result = task_func(text=custom_text)
        
        # Assert that SMTP was called with the right parameters
        mock_smtp.assert_called_once_with('smtp.gmail.com', 587)
        # Assert that starttls, login, sendmail, and quit were called on the SMTP instance
        mock_smtp_instance.login.assert_called_once_with('your.email@gmail.com', 'your.password')
        mock_smtp_instance.sendmail.assert_called_once_with('your.email@gmail.com', 'names@gmail.com', 'Subject: Extracted Names\n\n')
        # Assert the return value
        self.assertEqual(result, [])
    @patch('smtplib.SMTP')
    def test_recepient(self, mock_smtp):
        # Create a MagicMock instance to replace the SMTP instance
        mock_smtp_instance = MagicMock()
        mock_smtp.return_value = mock_smtp_instance
        # Custom input text with no names
        custom_text = "[No names enclosed by square brackets]"
        
        # Call the function with custom input
        result = task_func(text=custom_text, recepient_address='change@gmail.com')
        
        # Assert that SMTP was called with the right parameters
        mock_smtp.assert_called_once_with('smtp.gmail.com', 587)
        # Assert that starttls, login, sendmail, and quit were called on the SMTP instance
        mock_smtp_instance.login.assert_called_once_with('your.email@gmail.com', 'your.password')
        mock_smtp_instance.sendmail.assert_called_once_with('your.email@gmail.com', 'change@gmail.com', 'Subject: Extracted Names\n\n')
        # Assert the return value
        self.assertEqual(result, [])
    @patch('smtplib.SMTP')
    def test_login(self, mock_smtp):
        # Create a MagicMock instance to replace the SMTP instance
        mock_smtp_instance = MagicMock()
        mock_smtp.return_value = mock_smtp_instance
        # Custom input text with no names
        custom_text = "[No names enclosed by square brackets]"
        
        # Call the function with custom input
        result = task_func(text=custom_text, email_address="your.email.change@gmail.com", email_password="your.password.change")
        
        # Assert that SMTP was called with the right parameters
        mock_smtp.assert_called_once_with('smtp.gmail.com', 587)
        # Assert that starttls, login, sendmail, and quit were called on the SMTP instance
        mock_smtp_instance.login.assert_called_once_with('your.email.change@gmail.com', 'your.password.change')
        # Assert the return value
        self.assertEqual(result, [])
