from flask import Flask, render_template, request
import json
import logging

logging.basicConfig(filename="out.log", level=logging.INFO)

def f_1713(template_folder):
    """
    Creates a Flask application with a specified templates folder. It defines a route at the root ('/')
    which handles POST requests, logs the information request data as a JSON in a file called "out.log", and renders an 'index.html' template using
    the data provided in POST requests.

    Parameters:
    template_folder (str): The folder containing the Flask application's templates.

    Returns:
    flask.app.Flask: A Flask application instance configured with a root route that handles POST requests.
    The route logs incoming request data as JSON and serves the 'index.html' template with the provided data.

    Requirements:
    - Flask
    - json
    - logging

    Example:
    # Example 1: Create an instance of the Flask app with custom parameters
    >>> app = f_1713('my_templates')
    >>> isinstance(app, Flask)
    True

    # Example 2: Check the route configuration
    >>> 'POST' in app.url_map.bind('').match('/', method='POST')
    False
    """

    app = Flask(__name__, template_folder=template_folder)

    @app.route('/', methods=['POST'])
    def home():
        data = request.json
        logging.info(json.dumps(data))
        return render_template('index.html', data=data)
    return app

import unittest
from unittest.mock import patch
from flask import Flask, request
import logging
import os
import tempfile

class TestF1713(unittest.TestCase):

    def setUp(self):
        self.template_folder = tempfile.mkdtemp()
        self.index_html_path = os.path.join(self.template_folder, 'index.html')
        with open(self.index_html_path, 'w') as f:
            f.write('<html><body>{{ data }}</body></html>')
        self.log_file = "out.log"
        
    def tearDown(self):
        os.remove(self.index_html_path)
        os.rmdir(self.template_folder)

    def test_app_creation(self):
        """Test if the function properly creates an app with given parameters."""
        app = f_1713(self.template_folder)
        app.config['TESTING'] = True
        self.assertIsInstance(app, Flask, "The function should return a Flask app instance.")
        self.assertEqual(app.template_folder, self.template_folder, "The template folder should be set correctly.")

    def test_app_instance(self):
        """Test if the function returns a Flask app instance."""
        app = f_1713(self.template_folder)
        app.config['TESTING'] = True
        self.assertIsInstance(app, Flask)

    def test_template_folder_configuration(self):
        """Test if the template folder is correctly configured."""
        app = f_1713(self.template_folder)
        app.config['TESTING'] = True
        self.assertEqual(app.template_folder, self.template_folder, "The template folder should be set correctly.")

    def test_log_file_creation_and_content(self):
        """Test if the log file is created and contains the expected log after a loggable action occurs."""
        app = f_1713(self.template_folder)
        app.config['TESTING'] = True
        client =app.test_client()

        # Trigger a loggable action
        test_data = {"test": "data"}
        with app.test_client() as client:
            client.post('/', json=test_data)

        # Check if the log file is created and contains the expected content
        self.assertTrue(os.path.exists(self.log_file), "Log file should be created.")
        with open(self.log_file, "r") as f:
            logs = f.read()
        self.assertIn(json.dumps(test_data), logs)

    @patch('logging.info')
    def test_logging_request_data(self, mock_logging):
        """Test if logging correctly logs POST request data."""
        app = f_1713(self.template_folder)
        app.config['TESTING'] = True
        test_data = {"test": "data"}
        client =app.test_client()
        client.post('/', json=test_data)
        # Ensure that logging.info was called with the JSON-dumped test data
        mock_logging.assert_called_once_with(json.dumps(test_data))

    @patch('flask.Flask.url_for')
    def test_home_route(self, mock_url_for):
        """Test if the '/' route is defined correctly."""
        app = f_1713(self.template_folder)
        app.config['TESTING'] = True
        with app.test_request_context('/'):
            mock_url_for.return_value = '/'
            self.assertEqual(request.path, mock_url_for('home'))



if __name__ == '__main__':
    unittest.main()

