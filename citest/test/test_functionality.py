import unittest

from citest import functionality

class TestFunctionality(unittest.TestCase):

    def test_square(self):
        x = 2
        y = functionality.square(x)
        self.assertEqual(y, 4)

if __name__ == "__main__":
    unittest.main()
