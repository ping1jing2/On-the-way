# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/two-sum/description/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
    
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,

return [0, 1].
"""

"""
注释：

遍历nums列表，获取列表值number及其下标i

将target - number 作为ret的键，下标i作为值

判断number值是否在ret中，是则返回下标列表，否则循环
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ret = {}
        for i, number in enumerate(nums):
            if number in ret:
                return [ret[number], i]
            ret[target - number] = i