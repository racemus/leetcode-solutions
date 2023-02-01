import unittest

class Solution:
    '''
    It's my solution. First, it finds common factors of both strings length and put them
    to list sorted descending. Then it loops over it and checks substrings with length of
    these factor in both strings. The first result is the answer or no result returns as
    an empty string.
    '''
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        factors = []
        minStr = min((str1, str2), key=len)

        for i in range(1, len(minStr) + 1):
            # print('#1', 'i =', ' min(len(str1), len(str2)) =', min(len(str1), len(str2)))
            if len(str1) % i == 0 and len(str2) % i == 0:
                factors.append(i)
            # print('#2', ' factors =', factors)
        factors.sort(reverse = True)
        # print('#3', 'factors =', factors)
        for factor in factors:
            for j in range(factor, len(minStr) + 1):
                divisor = minStr[j-factor:j]
                if (divisor * (len(str1) // factor) == str1 and
                    divisor * (len(str2) // factor) == str2):
                    return divisor

        return ''

### EXAMPLE
# class Solution:
#     '''
#     Fastest solution using ready method gcn from math library to find the greatest common
#     divisor. Also, It compares the sum of strings in the beginning by adding them to each
#     other in both ways. If they both are divisible by the same divisor, their sum must be
#     the same.
#     '''
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
#         if (str1 + str2 != str2 + str1):
#             return ''
#         return str1[:math.gcd(len(str1),len(str2))]

### EXAMPLE
# class Solution:
#     '''
#     It's a recursive solution. It cuts a smaller string from a bigger one and repeats
#     itself with the remainder of the bigger string. In the end, strings become the same
#     and also equals to the answer.
#     '''
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
#         if len(str1) == len(str2):
#             return str1 if str1==str2 else ''
#         else:
#             if len(str1) < len(str2):
#                 str1,str2 = str2,str1
#             if str1[:len(str2)] == str2:
#                 return self.gcdOfStrings(str1[len(str2):],str2)
#             else:
#                 return ''

### EXAMPLE
# class Solution:
#     '''
#     This solution uses the same approach as mine when it works with substrings, but its
#     calculation of greatest common divisor is much simpler and overall it has less memory
#     consumption.
#     '''
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
#         for i in range(min(len(str1), len(str2)), 0, -1):
#             if (len(str1) % i) == 0 and (len(str2) % i) == 0:
#                 if str1[:i] * (len(str1) // i) == str1 and str1[:i] * (len(str2) // i) == str2:
#                     return str1[:i]
#         return ''


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.gcdOfStrings('ABCABC', 'ABC'), 'ABC')

    def test_2(self):
        self.assertEqual(self.solution.gcdOfStrings('ABABAB', 'ABAB'), 'AB')

    def test_3(self):
        self.assertEqual(self.solution.gcdOfStrings('LEET', 'CODE'), '')

    def test_4(self):
        self.assertEqual(self.solution.gcdOfStrings('ABABABAB', 'ABAB'), 'ABAB')

    def test_5(self):
        self.assertEqual(self.solution.gcdOfStrings('TAUXXTAUXXTAUXXTAUXXTAUXX',
            'TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX'), 'TAUXX')

if __name__ == '__main__':
    unittest.main()