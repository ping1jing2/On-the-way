# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/range-addition-ii/description/

Given an m * n matrix M initialized with all 0's and several update operations.

Operations are represented by a 2D array, and each operation is represented by an array with two positive integers a and b, which means M[i][j] should be added by one for all 0 <= i < a and 0 <= j < b.

You need to count and return the number of maximum integers in the matrix after performing all the operations.
"""

"""
注释：

如果ops为空，最大数为0，共有m * n个0

因为是将a x b的区域内所有数加1，所有最后最大的数肯定是ops所有子列表中a x b的最小区域，只有最小区域内的值才能保证每次加1操作都执行

所以将ops的所有行值组成一个列表，所有列值组成一个列表，最后将两个列表中的最小值相乘并返回
"""
class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not len(ops):
            return m * n
        row = []
        column = []
        for operation in ops:
            a, b = tuple(operation)
            row.append(a)
            column.append(b)
        return min(row) * min(column)