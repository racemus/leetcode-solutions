from typing import List
import unittest

class Solution:
    '''
    My simple solution. Not so fast, though. It uses sorted function for words list with
    key as a list of charecter indicies from order, which is created with lambda.
    '''
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        return sorted(words, key=lambda word: [order.index(ch) for ch in word]) == words

### EXAMPLE
# class Solution:
#     '''
#     Here is rightly noticed that order string has no repeated characters as any alphabet.
#     It creates the dictionary with character as a key and its index in order as a value.
#     Next it creates a list with indexes of the first word in the words list and then
#     compares it with each next one in the words list over the loop using python native
#     approach in comparing lists element by element. First discrepancy returns False. It's
#     possible to compare a list in a simple way, but not strings. This solution solved it.
#     '''
#     def isAlienSorted(self, words: List[str], order: str) -> bool:
#         h = {ch: i for i, ch in enumerate(order)}
#         prev = list(h[ch] for ch in words[0])
#         for i in range(1, len(words)):
#             cur = list(h[ch] for ch in words[i])
#             if cur < prev:
#                 return False
#             prev = cur
#         return True

### EXAMPLE
# class Solution:
#     '''
#     It is the fastest solution on leetcode. Strange though. It repeats the logic of
#     sorted with indexes as keys, but it's Python, not C++, so it should not be so fast.
#     '''
#     def isAlienSorted(self, words: List[str], order: str) -> bool:
#         """
#         we will iterate through all word in words then how to check the order:
#         """
#         mydict = {}
#         i = 0
#         for letter in order:
#             mydict[letter] = i
#             i+=1
#         #print(mydict)
#         x = 0
#         first, second = 0, 1
#         while second < len(words):
#             idx = 0
#             f = words[first]
#             s = words[second]
#             # print(f, s)
#             while idx < min(len(f), len(s)):
                
#                 if mydict[f[idx]] > mydict[s[idx]]:
#                     return False
#                 elif mydict[f[idx]] < mydict[s[idx]]:
#                     x = 1
#                     break
#                 idx += 1
#             if x == 0 and idx < max(len(f),len(s)) and len(f)>len(s):
#                 return False

#             first += 1 
#             second += 1
            
#         return True


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