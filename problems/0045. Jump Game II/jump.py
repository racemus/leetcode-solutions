from typing import List
import unittest

class Solution:
    '''
    It is a greedy solution. It iterates over the nums list and updates left and right
    integer variables, which represent the previous and next farthest jumps from current
    position. Every time it finds a new farthest position, it updates the right variable.
    When the current position comes to the left variable, it makes a jump to the farthest
    position. This position becomes left and the result counter increases.
    '''
    def jump(self, nums: List[int]) -> int:
        left = 0
        right = 0
        result = 0

        for i in range(len(nums)-1):
            # print('#1', ' i =', i, ' left =', left, ' right =', right, ' result =', result)
            right = max(i + nums[i], right)
            if i == left:
                left = right
                result += 1
            # print('#2', ' i =', i, ' left =', left, ' right =', right, ' result =', result)
        return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.jump([2,3,1,1,4]), 2)

    def test_2(self):
        self.assertEqual(self.solution.jump([2,3,0,1,4]), 2)

    def test_3(self):
        self.assertEqual(self.solution.jump([2,3,1,0,2,2,3]), 3)

if __name__ == '__main__':
    unittest.main()