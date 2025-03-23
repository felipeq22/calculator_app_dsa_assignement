import unittest

#THIS WAS MADE WITH THE HELP OF CHATGPT

from flask import Flask, request, render_template
from flask_app import app  # Replace with the actual name of your app

class TestCircleCalculator(unittest.TestCase):

    def setUp(self):

        self.client = app.test_client()
        self.client.testing = True 

    def test_post_request_valid_radius(self):
        # Test POST request with valid input (radius and operation)
        response = self.client.post('/circle_calculator', data={'radius': '5', 'operation': 'area'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'78.54', response.data)

    def test_post_request_valid_perimeter(self):
        # Test POST request with valid input (radius and operation)
        response = self.client.post('/circle_calculator', data={'radius': '7', 'operation': 'perimeter'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'43.98', response.data)

    def test_post_request_invalid_radius_area(self):
        # Test POST request with invalid input (non-numeric radius)
        response = self.client.post('/circle_calculator', data={'radius': 'invalid', 'operation': 'area'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Cannot perform operation with this input', response.data)

    def test_post_request_invalid_radius_perimeter(self):
        # Test POST request with invalid input (non-numeric radius)
        response = self.client.post('/circle_calculator', data={'radius': 'invalid', 'operation': 'perimeter'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Cannot perform operation with this input', response.data)

    def test_post_request_no_radius_area(self):
        # Test POST request without radius
        response = self.client.post('/circle_calculator', data={'radius': '', 'operation': 'area'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Cannot perform operation with this input', response.data)

    def test_post_request_no_radius_perimeter(self):
        # Test POST request without radius
        response = self.client.post('/circle_calculator', data={'radius': '', 'operation': 'perimeter'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Cannot perform operation with this input', response.data)

if __name__ == '__main__':
    unittest.main()