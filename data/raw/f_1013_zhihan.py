import subprocess
from ftplib import FTP
import os
import sys

def f_1013(ftp_server='ftp.dlptest.com', ftp_user='dlpuser', ftp_password='rNrKYTX9g7z3RgJRmxWuGHbeu', ftp_dir='/ftp/test'):
    """
    Download all files from a specific directory on an FTP server using wget in a subprocess.
    
    Args:
    - ftp_server (str): The FTP server address. Default is 'ftp.dlptest.com'.
    - ftp_user (str): The FTP server username. Default is 'dlpuser'.
    - ftp_password (str): The FTP server password. Default is 'rNrKYTX9g7z3RgJRmxWuGHbeu'.
    - ftp_dir (str): The directory path on the FTP server from which files need to be downloaded. Default is '/ftp/test'.
    
    Returns:
    - List[str]: A list of filenames downloaded from the FTP server.
    
    Requirements:
    - subprocess
    - ftplib
    - os
    - sys

    Example:
    >>> f_1013()
    ['file1.txt', 'file2.jpg', ...]
    """
    try:
        ftp = FTP(ftp_server)
        ftp.login(ftp_user, ftp_password)
        ftp.cwd(ftp_dir)
    except Exception as e:
        print(f'Failed to connect to FTP server: {str(e)}')
        sys.exit(1)

    # Directory to store downloaded files
    download_dir = "downloaded_files"
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    downloaded_files = []
    for filename in ftp.nlst():
        command = f'wget ftp://{ftp_user}:{ftp_password}@{ftp_server}{ftp_dir}/{filename} -P {download_dir}'
        subprocess.call(command, shell=True)
        downloaded_files.append(filename)

    ftp.quit()
    return downloaded_files

import unittest
import os
import subprocess
from ftplib import FTP
import sys


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def setUp(self):
        # Cleanup before each test
        if os.path.exists("downloaded_files"):
            for filename in os.listdir("downloaded_files"):
                os.remove(os.path.join("downloaded_files", filename))
            os.rmdir("downloaded_files")

    def test_case_1(self):
        # Default parameters
        downloaded_files = f_1013()
        self.assertTrue(isinstance(downloaded_files, list))
        self.assertTrue(len(downloaded_files) > 0)
        for file in downloaded_files:
            self.assertTrue(os.path.exists(os.path.join("downloaded_files", file)))

    def test_case_2(self):
        # Invalid FTP server
        with self.assertRaises(SystemExit):
            f_1013(ftp_server="invalid_server")

    def test_case_3(self):
        # Invalid FTP user
        with self.assertRaises(SystemExit):
            f_1013(ftp_user="invalid_user")

    def test_case_4(self):
        # Invalid FTP password
        with self.assertRaises(SystemExit):
            f_1013(ftp_password="invalid_password")

    def test_case_5(self):
        # Invalid FTP directory
        with self.assertRaises(SystemExit):
            f_1013(ftp_dir="/invalid_directory")
if __name__ == "__main__":
    run_tests()