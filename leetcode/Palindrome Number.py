# -*- coding: utf-8 -*-
"""
Determine whether an integer is a palindrome. Do this without extra space.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
"""

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        trans, length = str(x), len(str(x))
        if length == 1:
            return True
        else:
            temp1 = trans[ : length // 2]
            temp2 = trans[::-1][ : length // 2]
            return temp1 == temp2