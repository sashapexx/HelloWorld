import unittest
from src.main import hello_world

class TestHelloWorld(unittest.TestCase):
    def test_default(self):
        self.assertEqual(hello_world(), "Hello World!")

    def test_custom_name(self):
        self.assertEqual(hello_world("Alice"), "Hello Alice!")

if __name__ == "__main__":
    unittest.main()
