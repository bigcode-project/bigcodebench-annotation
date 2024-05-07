from django.http import HttpResponse
import uuid

def f_479(data):
    """
    Create a Django HttpResponse with JSON data, and include a UUID in the HTTP headers to track requests.

    Parameters:
    data (str): The JSON-formatted data to be included in the response body.

    Returns:
    HttpResponse: A Django HttpResponse with JSON data and UUID.
    
    Requirements:
    - django
    - uuid

    Example:
    >>> import json
    >>> response = f_479(json.dumps({"Sample-Key": "Sample-Value"}))
    >>> response.has_key('UUID')
    True
    """
    response = HttpResponse(data, content_type='application/json')
    request_uuid = uuid.uuid4()
    response['UUID'] = str(request_uuid)
    return response

import unittest
import json
from django.conf import settings
if not settings.configured:
    settings.configure(DEBUG=True)
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        # Testing with a simple JSON data
        input_data = json.dumps({"key": "value"})
        response = f_479(input_data)
        self.assertEqual(response.content.decode('utf-8'), input_data)
        self.assertIn('UUID', response)
        
    def test_case_2(self):
        # Testing with an empty JSON data
        input_data = json.dumps({})
        response = f_479(input_data)
        self.assertEqual(response.content.decode('utf-8'), input_data)
        self.assertIn('UUID', response)
        
    def test_case_3(self):
        # Testing with a more complex JSON data
        input_data = json.dumps({"users": [{"name": "John", "age": 30}, {"name": "Doe", "age": 25}]})
        response = f_479(input_data)
        self.assertEqual(response.content.decode('utf-8'), input_data)
        self.assertIn('UUID', response)
    def test_case_4(self):
        # Testing with JSON data containing special characters
        input_data = json.dumps({"description": "This is a sample data with special characters: !@#%^&*()_-+={[]}"})
        response = f_479(input_data)
        self.assertEqual(response.content.decode('utf-8'), input_data)
        self.assertIn('UUID', response)
    def test_case_5(self):
        # Testing with JSON data containing numeric values
        input_data = json.dumps({"numbers": [1, 2, 3, 4, 5]})
        response = f_479(input_data)
        self.assertEqual(response.content.decode('utf-8'), input_data)
        self.assertIn('UUID', response)
