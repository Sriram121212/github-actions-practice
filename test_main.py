
import unittest
from main import add

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10, 20), 30)

if __name__ == "__main__":
    unittest.main()
