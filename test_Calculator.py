import unittest
import Calculator

class testCalculator(unittest.TestCase):

    def testAdd(self):
        self.assertEqual(Calculator.add(2, 2), 4)

    def testSquared(self):
        self.assertEqual(Calculator.squared(9), 81)

    def testCubed(self):
        self.assertEqual(Calculator.cubed(3), 27)

    def testSquareRoot(self):
        self.assertEqual(Calculator.square_root(9), 3)

if __name__ == '__main__':
    unittest.main()