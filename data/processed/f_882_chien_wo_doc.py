from datetime import datetime
import json

SERVER_ADDRESS = "localhost"
BUFFER_SIZE = 1024


def f_76(client_socket):
    """
    Responds to a client's request by sending a JSON-formatted message containing
    the current server time and a greeting.

    Parameters:
    - client_socket (socket.socket): The client socket from which the request is received.

    Requirements:
    - datetime.datetime
    - json

    Returns:
    - None

    Example:
    >>> import socket
    >>> server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    >>> server_socket.bind((SERVER_ADDRESS, 0))  # Bind to a free port
    >>> server_socket.bind((SERVER_ADDRESS, 8080))
    >>> server_socket.listen(1)
    >>> try:
    ...     client_socket, _ = server_socket.accept()
    ...     f_76(client_socket)
    ... finally:
    ...     server_socket.close()
    """
    response_data = {"message": "Hello", "time": str(datetime.now())}
    response = json.dumps(response_data) + "\n"
    client_socket.send(response.encode("utf-8"))
    client_socket.close()

import unittest
import socket
import threading
class TestCases(unittest.TestCase):
    """Test cases for f_76."""
    def setUp(self):
        """Set up a server socket for testing."""
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((SERVER_ADDRESS, 0))  # Bind to a free port
        self.server_socket.listen(1)
        self.port = self.server_socket.getsockname()[1]
    def tearDown(self):
        """Close the server socket after each test."""
        self.server_socket.close()
    def client_thread_function(self, responses, request_message):
        """Function to simulate a client sending a request and receiving a response."""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((SERVER_ADDRESS, self.port))
            client_socket.send(request_message + b"\n")  # Append end-of-message marker
            response = client_socket.recv(BUFFER_SIZE).decode()
            responses.append(response)
    def test_response_contains_greeting(self):
        """Test if the response from the server contains a greeting."""
        responses = []
        client_thread = threading.Thread(
            target=self.client_thread_function, args=(responses, b"Test request")
        )
        client_thread.start()
        client_socket, _ = self.server_socket.accept()
        f_76(client_socket)
        client_thread.join()
        # Ensure that responses is not empty before accessing it
        self.assertTrue(responses)  # Check that responses is not empty
        self.assertIn("Hello", responses[0])
    def test_handle_large_request(self):
        """
        Test how the function handles a request larger than the buffer size.
        """
        responses = []
        client_thread = threading.Thread(
            target=self.client_thread_function,
            args=(responses, b"a" * (BUFFER_SIZE + 1)),
        )
        client_thread.start()
        client_socket, _ = self.server_socket.accept()
        f_76(client_socket)
        client_thread.join()
        # Expecting a normal response despite a large request
        self.assertIn("Hello", responses[0])
    def test_response_format(self):
        """
        Test if the response format from the server is correct.
        """
        responses = []
        client_thread = threading.Thread(
            target=self.client_thread_function, args=(responses, b"Format request")
        )
        client_thread.start()
        client_socket, _ = self.server_socket.accept()
        f_76(client_socket)
        client_thread.join()
        response_data = json.loads(responses[0])
        self.assertIn("time", response_data)
    def test_handle_special_characters_request(self):
        """
        Test how the function handles a request with special characters.
        """
        special_request = b"!@#$%^&*()_+"
        responses = []
        client_thread = threading.Thread(
            target=self.client_thread_function, args=(responses, special_request)
        )
        client_thread.start()
        client_socket, _ = self.server_socket.accept()
        f_76(client_socket)
        client_thread.join()
        # Expecting a normal response despite a request with special characters
        self.assertIn("Hello", responses[0])
    def test_handle_json_request(self):
        """
        Test how the function handles a JSON-formatted request.
        """
        json_request = {"request": "time"}
        json_request_encoded = json.dumps(json_request).encode("utf-8")
        responses = []
        client_thread = threading.Thread(
            target=self.client_thread_function, args=(responses, json_request_encoded)
        )
        client_thread.start()
        client_socket, _ = self.server_socket.accept()
        f_76(client_socket)
        client_thread.join()
        # Expecting a normal response despite the JSON request
        self.assertIn("Hello", responses[0])
