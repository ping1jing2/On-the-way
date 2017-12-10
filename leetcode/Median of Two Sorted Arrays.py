# -*- coding: utf-8 -*-
"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
    
nums1 = [1, 3]

nums2 = [2]

The median is 2.0

Example 2:
    
nums1 = [1, 2]

nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()
        length = len(nums1)
        return nums1[length // 2] if length % 2 else (nums1[length // 2 - 1] + nums1[length // 2]) / 2