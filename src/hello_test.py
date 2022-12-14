import unittest
import requests
from hello import add, substract


class TestHello(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_substract(self):
        self.assertEqual(substract(2, 1), 1)

    def test_server(self):
        r = requests.get('http://localhost:3000')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.content, b'Hello World!')
    
    def test_server_fail(self):
        r = requests.get('http://localhost:3000')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.content, b'Another text!')
