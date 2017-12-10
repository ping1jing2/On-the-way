# -*- coding: utf-8 -*-
"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = len(s)
        if max_len > 1:             #len(s) < 2时直接返回len(s)
            temp_max = 0            #最大长度的中间变量
            first, last = 0, 1      #最大子串的首尾位置
            while last != max_len:
                while s[last] in s[first : last]:   #当前last位置repeat则更新
                    if last - first > temp_max:
                        temp_max = last - first
                    first += 1
                    last = first
                last += 1                           #last一直向后移动
            else:
                if last - first > temp_max:
                    temp_max = last - first
            max_len = temp_max
        return max_len