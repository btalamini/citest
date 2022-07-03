import unittest
import sys

from citest import functionality

class TestFunctionality(unittest.TestCase):

    def test_square(self):
        x = 2
        y = functionality.square(x)
        self.assertEqual(y, 4)

    def test_power4(self):
        x = 2
        y = functionality.power4(x)
        self.assertEqual(y, 16)

    def test_dict_union(self):
        a = {'color': 'red', 'number': 2}
        b = {'flavor': 'cherry'}
        v = sys.version_info 
        if v.major >= 3 and v.minor >= 9:
            c = a | b
        else:
            c = {**a, **b}
        print(c)

if __name__ == "__main__":
    unittest.main()
