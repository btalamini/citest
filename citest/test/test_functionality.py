import unittest

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
        c = a | b
        print(c)

if __name__ == "__main__":
    unittest.main()
