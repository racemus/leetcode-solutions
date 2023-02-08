from typing import List
import unittest

class Solution:
    '''
    My first try. Doesn't work!
    '''
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) <= 2:
            return len(fruits)
        global_result = fruits[:2]
        local_result = fruits[:2]

        for i in range(2, len(fruits)):
            # print('#1', ' i =', i, ' local_result =', local_result, ' global_result =',
            #     global_result)
            if fruits[i] in local_result or (local_result.count(local_result[0]) ==
                len(local_result)):
                local_result.append(fruits[i])
                # print('#2', ' i =', i, ' local_result =', local_result,
                #     ' global_result =', global_result)
            else:
                for j in range(len(local_result) - 1, -1, -1):
                    # print('##', ' j =', j)
                    if local_result[j] != local_result[-1]:
                        local_result = local_result[j+1:]
                        break
                local_result.append(fruits[i])
                # print('#3', ' i =', i, ' local_result =', local_result,
                #     ' global_result =', global_result)
            # print('#4', ' i =', i, ' local_result =', local_result, ' global_result =',
            #     global_result)
            if len(global_result) < len(local_result):
                global_result = local_result.copy()

        return len(global_result)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.totalFruit([1,2,1]), 3)

    def test_2(self):
        self.assertEqual(self.solution.totalFruit([0,1,2,2]), 3)

    def test_3(self):
        self.assertEqual(self.solution.totalFruit([1,2,3,2,2]), 4)

    def test_4(self):
        self.assertEqual(self.solution.totalFruit([1]), 1)

    def test_5(self):
        self.assertEqual(self.solution.totalFruit([1,1]), 2)

    def test_6(self):
        self.assertEqual(self.solution.totalFruit([1,2]), 2)

    def test_7(self):
        self.assertEqual(self.solution.totalFruit([1,2,3,2,3]), 4)

    def test_8(self):
        self.assertEqual(self.solution.totalFruit([3,3,3,1,2,1,1,2,3,3,4]), 5)

    def test_9(self):
        self.assertEqual(self.solution.totalFruit([0,0,1,1]), 4)

    def test_10(self):
        self.assertEqual(self.solution.totalFruit([3,3,3,1,4]), 4)

    def test_11(self):
        self.assertEqual(self.solution.totalFruit([0,1,6,6,4,4,6]), 5)

if __name__ == '__main__':
    unittest.main()