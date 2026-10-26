from django.test import TestCase
from django.urls import reverse


class APITests(TestCase):

    def test_api_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_api_response_message(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(
            response.data['message'],
            'Welcome to my CSC325 Django REST API!'
        )

    def test_api_version(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.data['version'], '1.1')