# -*- coding: utf-8 -*-
"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);

convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""
"""
注释
zigzag pattern：

n=numRows
        1                           2n-1                         4n-3
        2                     2n-2  2n                    4n-4   4n-2
        3               2n-3        2n+1              4n-5       .
        .           .               .               .            .
        .       n+2                 .           3n               .
        n-1 n+1                     3n-3    3n-1                 5n-5
        n                           3n-2                         5n-4


"""

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or len(s) < numRows:
            return s
        ret = [''] * numRows
        index, step = 0, 1
        for letter in s:
            ret[index] += letter
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        return ''.join(ret)