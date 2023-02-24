import unittest

class Solution:
    '''
    It is a simple mathematical solution. It calculates the difference between given
    integers and adds 1 if at least one of them is even.
    '''
    def countOdds(self, low: int, high: int) -> int:
        result = (high - low) // 2
        if high % 2 != 0 or low % 2 != 0:
            result += 1
        return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.countOdds(3, 7), 3)

    def test_2(self):
        self.assertEqual(self.solution.countOdds(8, 10), 1)

if __name__ == '__main__':
    unittest.main()
