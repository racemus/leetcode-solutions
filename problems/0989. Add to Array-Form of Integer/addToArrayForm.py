from typing import List
import unittest

class Solution:
    '''
    It converts list of integers to list of digits as strings, then joins digits to
    number as a string, converts it to integer and add k integer to it. Then it converts
    the sum to string and creates the new list of integers via iterating over the
    characters of the string.
    '''
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        return [int(i) for i in str(int(''.join(map(str, num))) + k)]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.addToArrayForm([1,2,0,0], 34), [1,2,3,4])

    def test_2(self):
        self.assertEqual(self.solution.addToArrayForm([2,7,4], 181), [4,5,5])

    def test_3(self):
        self.assertEqual(self.solution.addToArrayForm([2,1,5], 806), [1,0,2,1])

if __name__ == '__main__':
    unittest.main()