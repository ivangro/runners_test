import unittest
from hello import add, substract


class TestHello(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_substract(self):
        self.assertEqual(substract(2, 1), 1)

if __name__ == '__main__':
    unittest.main()