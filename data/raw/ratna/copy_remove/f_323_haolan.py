import json
from django.http import HttpResponse
from django.conf import settings
import uuid

if not settings.configured:
    settings.configure(DEBUG=True)

def f_323(data):
    """
    Create a Django HttpResponse with JSON data, including a UUID in the HTTP headers to track requests.
    
    Parameters:
    data (str): The data to be included in the response body.
    
    Returns:
    HttpResponse: A Django HttpResponse with JSON data and UUID.
    
    Requirements:
    - django
    - json
    - uuid

    Example:
    >>> f_323(json.dumps({"Sample-Key": "Sample-Value"}))
    """

    response = HttpResponse(data, content_type='application/json')

    # Generate a UUID
    request_uuid = uuid.uuid4()

    # Add the UUID to the response headers
    response['UUID'] = str(request_uuid)

    return response

import unittest
import json

class TestF1366(unittest.TestCase):
    
    def test_case_1(self):
        # Testing with a simple JSON data
        input_data = json.dumps({"key": "value"})
        response = f_323(input_data)
        self.assertEqual(response.content.decode('utf-8'), input_data)
        self.assertIn('UUID', response)
        
    def test_case_2(self):
        # Testing with an empty JSON data
        input_data = json.dumps({})
        response = f_323(input_data)
        self.assertEqual(response.content.decode('utf-8'), input_data)
        self.assertIn('UUID', response)
        
    def test_case_3(self):
        # Testing with a more complex JSON data
        input_data = json.dumps({"users": [{"name": "John", "age": 30}, {"name": "Doe", "age": 25}]})
        response = f_323(input_data)
        self.assertEqual(response.content.decode('utf-8'), input_data)
        self.assertIn('UUID', response)

    def test_case_4(self):
        # Testing with JSON data containing special characters
        input_data = json.dumps({"description": "This is a sample data with special characters: !@#%^&*()_-+={[]}"})
        response = f_323(input_data)
        self.assertEqual(response.content.decode('utf-8'), input_data)
        self.assertIn('UUID', response)

    def test_case_5(self):
        # Testing with JSON data containing numeric values
        input_data = json.dumps({"numbers": [1, 2, 3, 4, 5]})
        response = f_323(input_data)
        self.assertEqual(response.content.decode('utf-8'), input_data)
        self.assertIn('UUID', response)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestF1366))
    runner = unittest.TextTestRunner()
    runner.run(suite)
if __name__ == "__main__":
    run_tests()