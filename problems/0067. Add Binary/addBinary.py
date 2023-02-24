import unittest

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2) + int(b,2))[2:]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.addBinary('11', '1'), '100')

    def test_2(self):
        self.assertEqual(self.solution.addBinary('1010', '1011'), '10101')

if __name__ == '__main__':
    unittest.main()