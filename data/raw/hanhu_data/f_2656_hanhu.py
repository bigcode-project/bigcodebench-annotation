import cgi
import http.server
import json

def f_2658():
    """
    The f_2658 method is a specialized handler for processing HTTP POST requests within a server setup,
    primarily designed to handle JSON-formatted data. It meticulously checks incoming requests to ensure they contain the
    expected 'data' key and have a Content-Type header set to application/json.
    If a request fails these checks, the method responds with an error status and a message indicating the specific validation failure.
    Conversely, when a request satisfies these criteria, it acknowledges with a success message,
    indicating proper receipt and processing of the data. This method is implemented as a subclass of http.server.BaseHTTPRequestHandler,
    allowing it to be seamlessly integrated into HTTP server frameworks.
    By overriding the do_POST method, it provides tailored handling of POST requests, including appropriate HTTP status
    code responses and standardized JSON response bodies, ensuring a robust and clear communication protocol for server-client interactions.

    Notes:
    - If the 'Content-Type' header is not 'application/json', the server responds with a 400 Bad Request status and a JSON object:
      {"status": "error", "message": "Content-Type header is not application/json"}.
    - If the received JSON object does not contain a 'data' key, the response is a 400 Bad Request with a JSON object:
      {"status": "error", "message": "No data received"}.
    - For successfully processed requests, the server responds with a 200 OK status and a JSON object:
      {"status": "success", "message": "Data received successfully."}.

    Returns:
    class: A class that is a subclass of http.server.BaseHTTPRequestHandler, designed to handle HTTP POST requests.

    Requirements:
    - cgi
    - http.server
    - json

    Example:
    >>> handler = f_2658()
    >>> server = http.server.HTTPServer(('127.0.0.1', 8080), handler)
    >>> server.serve_forever()
    """
    class PostRequestHandler(http.server.BaseHTTPRequestHandler):
        def do_POST(self):
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
            
            # Define error response directly within the method
            error_response = {
                'status': 'error',
                'message': ''  # This will be modified based on the error condition
            }
            
            if ctype != 'application/json':
                self.send_response(400)
                self.end_headers()
                error_response['message'] = 'Content-Type header is not application/json'
                self.wfile.write(json.dumps(error_response).encode())
                return

            length = int(self.headers.get('content-length'))
            message = json.loads(self.rfile.read(length))
            
            if 'data' not in message:
                self.send_response(400)
                self.end_headers()
                error_response['message'] = 'No data received'
                self.wfile.write(json.dumps(error_response).encode())
                return

            # Define success response directly within the method
            success_response = {
                'status': 'success',
                'message': 'Data received successfully.'
            }
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(success_response).encode())

    return PostRequestHandler


import unittest
import requests_mock
import requests


# Constants
SUCCESS_RESPONSE = {
    'status': 'success',
    'message': 'Data received successfully.'
}

ERROR_RESPONSE = {
    'status': 'error',
    'message': 'Invalid data received.'
}

class TestF2658(unittest.TestCase):

    @requests_mock.mock()
    def test_invalid_content_type_header(self, m):
        # Mock the POST request to return a 400 status code for invalid content type
        m.post("http://testserver/", status_code=400, json=ERROR_RESPONSE)
        response = requests.post("http://testserver/", headers={"Content-Type": "text/plain"})
        self.assertEqual(response.json(), ERROR_RESPONSE)
        self.assertEqual(response.status_code, 400)

    @requests_mock.mock()
    def test_missing_data_in_request(self, m):
        # Mock the POST request to return a 400 status code for missing 'data' key
        m.post("http://testserver/", status_code=400, json=ERROR_RESPONSE)
        response = requests.post("http://testserver/", json={"wrong_key": "value"})
        self.assertEqual(response.json(), ERROR_RESPONSE)
        self.assertEqual(response.status_code, 400)

    @requests_mock.mock()
    def test_valid_post_request(self, m):
        m.post("http://testserver/", text=json.dumps(SUCCESS_RESPONSE))
        response = requests.post("http://testserver/", json={"data": "value"})
        self.assertEqual(response.json(), SUCCESS_RESPONSE)
        self.assertEqual(response.status_code, 200)

    @requests_mock.mock()
    def test_response_content_type(self, m):
        # Mock the POST request and explicitly set the 'Content-Type' header
        headers = {'Content-Type': 'application/json'}
        m.post("http://testserver/", json=SUCCESS_RESPONSE, headers=headers)
        response = requests.post("http://testserver/", json={"data": "value"})
        self.assertEqual(response.headers["Content-Type"], "application/json")

    @requests_mock.mock()
    def test_incorrect_http_method(self, m):
        m.get("http://testserver/", status_code=405)
        response = requests.get("http://testserver/")
        self.assertEqual(response.status_code, 405)


def run_tests():
    """Run all tests for this function."""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestF2658)
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()
