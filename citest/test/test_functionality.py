import unittest

from citest import functionality

class TestFunctionality(unittest.TestCase):

    def test_square(self):
        x = 2.0
        y = functionality.square(x)

if __name__ == "__main__":
    unittest.main()
