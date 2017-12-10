# -*- coding: utf-8 -*-
"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123

Output:  321

Example 2:

Input: -123

Output: -321

Example 3:

Input: 120

Output: 21

Note:
    
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        sign = 1 if x > 0 else -1
        ret = int(str(x).strip('-0')[::-1])
        return sign * ret if ret < 2 ** 31 else 0