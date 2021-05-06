from django.test import TestCase, Client
import pytest
import logging as logger




def test_healthcheck(self):
    logger.info("Coming from logger")

def test_API_login_page(self):
    client = Client()
    response = client.get('')
    self.assertEqual(response.status_code, 200)
def test_API_homepage_without_login(self):
    client = Client()
    response = client.get('http://localhost:8000/homepage')
    self.assertEqual(response.status_code, 302)
def test_API_register(self):
    client = Client()
    response = client.post('http://localhost:8000/register',
    json={
        'name':'Barbosa',
        'email': 'junio@python.com',
        'password':'marceloarthur',
        'confirmPassword':'marceloarthur'
    }
    )
    assert response.status_code == 200