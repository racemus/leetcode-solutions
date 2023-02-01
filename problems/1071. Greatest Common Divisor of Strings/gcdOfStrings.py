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