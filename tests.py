import unittest
from functions import add, reverse_string, is_even

class TestFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("Python"), "nohtyP")

    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertFalse(is_even(3))

if __name__ == "__main__":
    unittest.main()
