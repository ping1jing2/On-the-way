# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/add-two-numbers/description/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)

Output: 7 -> 0 -> 8

Explanation: 342 + 465 = 807.
"""

"""
注释：
result是返回的链表，ret是为了得到result而进行中间操作的链表结点

当L1, L2均不为None时，利用value将L1, L2的当前结点val相加，然后通过ret.next = ListNode(value % 10)生成新结点，

最后都利用node = node.next来准备进行下一步遍历操作

因为result的头结点是ListNode(0)初始化的，所以最后的结果应该是不包含头结点的，故返回result.next
"""



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ret = ListNode(0)
        value = 0
        while l1 or l2:
            if l1:
                value += l1.val
                l1 = l1.next
            if l2:
                value += l2.val
                l2 = l2.next
            ret.next = ListNode(value % 10)
            ret = ret.next
            value //= 10
        if value:
            ret.next = ListNode(value)
        return result.next