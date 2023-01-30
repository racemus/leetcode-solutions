# from typing import Optional, List, Tuple, Dict, Set
import unittest

class Solution:
    '''
    My first try with recursion. It's really slow for larger numbers. Causes LTE.
    '''
    def tribonacci(self, n: int) -> int:
        if n < 0:
            return 0
        if n in {0, 1}:
            return n
        return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci (n - 3)


# [0,1,1,2,4,7,13,24,44,81,149,274,504,927,1705,3136]

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.tribonacci(4), 4)

    def test_2(self):
        self.assertEqual(self.solution.tribonacci(5), 7)

    def test_3(self):
        self.assertEqual(self.solution.tribonacci(6), 13)

    def test_4(self):
        self.assertEqual(self.solution.tribonacci(7), 24)

    def test_5(self):
        self.assertEqual(self.solution.tribonacci(8), 44)

    def test_6(self):
        self.assertEqual(self.solution.tribonacci(9), 81)

    def test_7(self):
        self.assertEqual(self.solution.tribonacci(10), 149)

    def test_8(self):
        self.assertEqual(self.solution.tribonacci(11), 274)

    def test_9(self):
        self.assertEqual(self.solution.tribonacci(12), 504)

    def test_10(self):
        self.assertEqual(self.solution.tribonacci(13), 927)

    def test_11(self):
        self.assertEqual(self.solution.tribonacci(14), 1705)

    def test_12(self):
        self.assertEqual(self.solution.tribonacci(15), 3136)

    # def test_13(self):
    #     self.assertEqual(self.solution.tribonacci(25), 1389537)

    # def test_14(self):
    #     self.assertEqual(self.solution.tribonacci(29), 15902591)

if __name__ == '__main__':
    unittest.main()