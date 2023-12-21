import unittest
from unittest.mock import patch, Mock
from io import StringIO
import os
import yaml
from health_check import send_request, calculate_availability

class TestHealthCheck(unittest.TestCase):
    def test_send_request_up(self):
        # Prepare mock data
        mock_data = {
            'url': 'https://fetch.com/',
            'method': 'GET',
            'headers': {},
            'body': None
        }
        mock_response = Mock()
        mock_response.status_code = 200

        # Mock the requests library
        with patch('health_check.requests.get') as mock_get:
            mock_get.return_value = mock_response
            send_request(mock_data, {})
            mock_get.assert_called_once_with('https://fetch.com/', headers={}, timeout=5)

    def test_send_request_down(self):
        mock_data = {
            'url': 'https://fetch.com/',
            'method': 'GET',
            'headers': {},
            'body': None
        }
        mock_response = Mock()
        mock_response.status_code = 404

        with patch('health_check.requests.get') as mock_get:
            mock_get.return_value = mock_response
            send_request(mock_data, {})
            mock_get.assert_called_once_with('https://fetch.com/', headers={}, timeout=5)

    def test_calculate_availability(self):
        url = 'https://fetch.com/'
        method = 'GET'

        up_count, req_count = calculate_availability(url, method, 1, 1)
        self.assertEqual(up_count, 1)
        self.assertEqual(req_count, 1)

if __name__ == '__main__':
    unittest.main()