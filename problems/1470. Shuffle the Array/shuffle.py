from typing import List
import unittest

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            if len(result) == len(nums):
                return result
            result.append(nums[i])
            result.append(nums[i+n])


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.shuffle([2,5,1,3,4,7], 3), [2,3,5,4,1,7])

    def test_2(self):
        self.assertEqual(self.solution.shuffle([1,2,3,4,4,3,2,1], 4), [1,4,2,3,3,2,4,1])

    def test_3(self):
        self.assertEqual(self.solution.shuffle([1,1,2,2], 2), [1,2,1,2])

if __name__ == '__main__':
    unittest.main()