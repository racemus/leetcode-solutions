from typing import Optional, List, Tuple, Dict, Set
from itertools import permutations
from math import factorial
import unittest

class Solution:
	'''
	My first try. Doesn't work
	'''
    def distinctNames(self, ideas: List[str]) -> int:
        ideas_decap = set([word[1:] for word in ideas])
        first_letters = set([word[0] for word in ideas])

        if len(first_letters) > len(ideas_decap):
            x = len(first_letters) - len(ideas_decap) + 1
            print('#1', ' x =', x)
            return (len(list(permutations(first_letters, 2))) -
                factorial(x) // factorial(x-2))
        elif len(first_letters) < len(ideas_decap):
            x = len(ideas_decap) - len(first_letters) + 1
            print('#2', ' x =', x)
            return (len(list(permutations(ideas_decap, 2))) -
                factorial(x) // factorial(x-2))
        else:
            return len(list(permutations(ideas_decap, 2)))


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.distinctNames(["coffee","donuts","time","toffee"]), 6)

    def test_2(self):
        self.assertEqual(self.solution.distinctNames(["lack","back"]), 0)

    def test_3(self):
        self.assertEqual(self.solution.distinctNames(["phhrrjjcm","zjfkpps","pm","fnpduelfe","mxtvjnq"]), 18)

    def test_4(self):
        self.assertEqual(self.solution.distinctNames(["abcd","ayz"]), 0)

    def test_5(self):
        self.assertEqual(self.solution.distinctNames(["coppee","donuts","time","toffee"]), 10)

    def test_6(self):
        self.assertEqual(self.solution.distinctNames(["coffee","donuts","lime","toffee"]), 10)

    def test_7(self):
        self.assertEqual(self.solution.distinctNames(["alrgtxxdj","illqfngl","rlrgtxxdj"]), 4)

    def test_8(self):
        self.assertEqual(self.solution.distinctNames(["r","lycdkjdnoy","wzlu","wxkyjgwc","qtaqnbi","m","x","jhvdzr","rquzz"]), 58)

    def test_9(self):
        self.assertEqual(self.solution.distinctNames(["aaa","baa","caa","bbb","cbb","dbb"]), 2)

if __name__ == '__main__':
    unittest.main()