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
            # print('#1', ' i =', i, ' left =', left, ' right =', right, ' result =',
            #     result)
            right = max(i + nums[i], right)
            if i == left:
                left = right
                result += 1
            # print('#2', ' i =', i, ' left =', left, ' right =', right, ' result =',
            #     result)
        return result

### EXAMPLE
# class Solution:
#     '''
#     It's one of the fastest solutions on leetcode. It's uses similar algorithm to mine,
#     but with while loop. It iterates till the right variable moves to the end of the nums
#     list. Also, it uses for loop inside that iterates in window between left and right
#     positions of the nums list to find the next right variable.
#     '''
#     def jump(self, nums: List[int]) -> int:
#         layer = 0
#         left, right = 0, 0

#         while right < len(nums) - 1:
#             left, right = right + 1, max(idx + nums[idx] for idx in range(left, right + 1))
#             layer += 1
        
#         return layer

### EXAMPLE
# class Solution:
#     '''
#     It's one of the least consumable solutions on leetcode. I think it's because of fewer
#     variables. It also uses while loop and for loop inside that iterates backwards.
#     What is interesting is that this solution exploits the statement in problem
#     description which said "The test cases are generated such that you can reach
#     nums[n - 1]". So it goes from the end of the nums list, searching the way it can be
#     reached.
#     ''' 
#     def jump(self, nums: List[int]) -> int:
#         goal = len(nums) - 1

#         jumps = 0
#         while goal > 0:
#             # print('#1', ' goal =', goal, ' jumps =', jumps)
#             temp = goal
#             for i in range(goal-1,-1,-1):
#                 # print('#2', ' goal =', goal, ' jumps =', jumps, ' temp =', temp)
#                 if i + nums[i] >= goal:
#                     temp = i
#                     # print('#3', ' goal =', goal, ' jumps =', jumps, ' temp =', temp)
#             goal = temp
#             jumps += 1
#             # print('\n#4', ' goal =', goal, ' jumps =', jumps)
        
#         return jumps


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