from typing import List
import unittest

class Solution:
    '''
    My simple solution. Not so fast, though. It uses sorted function for words list with
    key as a list of charecter indicies from order, which is created with lambda.
    '''
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        return sorted(words, key=lambda word: [order.index(ch) for ch in word]) == words


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.isAlienSorted(['hello','leetcode'],
            'hlabcdefgijkmnopqrstuvwxyz'), True)

    def test_2(self):
        self.assertEqual(self.solution.isAlienSorted(['word','world','row'],
            'worldabcefghijkmnpqstuvxyz'), False)

    def test_3(self):
        self.assertEqual(self.solution.isAlienSorted(['apple','app'],
            'abcdefghijklmnopqrstuvwxyz'), False)

if __name__ == '__main__':
    unittest.main()