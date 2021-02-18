from django.test import TestCase, Client

class AmericaLineTest(TestCase):
    def test_homepage(self):
        client = Client()
        response = client.get('')
        self.assertEqual(response.status_code, 200)

# Create your tests here.
