import unittest

'''
numRows = 3

P   A   H   N
A P L S I I G
Y   I   R

1 -> 1,5,9,13
2 -> 2,4,6,8,10
3 -> 3,7,11,15

numRows = 4

P     I    N
A   L S  I G
Y A   H R
P     I

1 -> 1,7,13
2 -> 2,6,8,12,14
3 -> 3,5,9,11,15
4 -> 4,10,16

numRows = 5

P       H
A     S I
Y   I   R
P L     I G
A       N

1 -> 1,9,17
2 -> 2,8,10,16,18
3 -> 3,7,11,15,19
4 -> 4,6,12,14,20
5 -> 5,13,21

numRows = 6

P         R
A       I I
Y     H   N
P   S     G
A I
L

1 -> 1,11,21
2 -> 2,10,12,20,22
3 -> 3,9,13,19,23
4 -> 4,8,14,18,24
5 -> 5,7,15,17,25
6 -> 6,16,26
'''


class Solution:
    '''
    It's my solution that iterates over the rows and passes ranges. Passes is maximum
    characters in any row. It calculates character index in the s string and put its
    character to a set. Then it converts the set to the list, sorts it and combines all
    sets one by one to the rows list. In the end, it converts the rows list to string and
    returns it.
    '''
    def convert(self, s: str, numRows: int) -> str:
        rows = []
        if len(s) <= numRows or numRows == 1:
            return s
        else:
            passes = (len(s) + numRows - 3) // (numRows - 1)
        # print('passes =', passes)
        for m in range(1, numRows + 1):
            row = set()

            for i in range(passes):
                index = (m * ((i + 1) % 2) + (2 * numRows - m) * (i % 2) + 2 *
                    (numRows - 1) * (i // 2) - 1)
                if index < len(s):
                    row.add(index)

            row = [s[j] for j in sorted(list(row))]
            rows.extend(row)
            # print('rows =', rows)
        return ''.join(rows)

### EXAMPLE
# class Solution:
#     '''
#     Simple and great solution. It forms the answer string in iteration over characters of
#     s string with help of 2 integers: row and step. Step shows the way zigzag goes:
#     forward or backward, and equals 1 or -1 respectively. Row equals the current row
#     index, and it increments every iteration by step.
#     '''    
#     def convert(self, s: str, numRows: int) -> str:
#         if numRows == 1:
#             return s
#         zigzag = ['' for _ in range(numRows)]
#         row = 0
#         step = 1
#         for c in s:
#             zigzag[row] += c
#             if row == numRows-1:
#                 step = -1
#             elif row == 0:
#                 step = 1
#             row += step
#         return ''.join(zigzag)

### EXAMPLE
# class Solution:
#     '''
#     This solution also uses zigzag filling of strings in a list of rows, but in different
#     way. It creates a helper list of indexes of move forward and backward and uses it as
#     a pattern-filter for indexes of characters in the s string.
#     '''
#     def convert(self, s: str, numRows: int) -> str:
#         temp=list(range(numRows))+list(range(numRows-2,0,-1))
#         res=[""]*numRows
#         for i,c in enumerate(s):
#             res[temp[i%len(temp)]]+=c
#         return("".join(res))


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.convert('PAYPALISHIRING', 3), 'PAHNAPLSIIGYIR')

    def test_2(self):
        self.assertEqual(self.solution.convert('PAYPALISHIRING', 4), 'PINALSIGYAHRPI')

    def test_3(self):
        self.assertEqual(self.solution.convert('A', 1), 'A')

    def test_4(self):
        self.assertEqual(self.solution.convert('AB', 1), 'AB')

if __name__ == '__main__':
    unittest.main()