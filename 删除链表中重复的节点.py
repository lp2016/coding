# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 需要考虑的问题有两个
# 1.头节点也可能被删除：需要辅助节点指向头节点
# 2.当两组重复节点相邻时如何处理：
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplication(self, pHead):
        if not pHead:
            return None
        pre_head = ListNode(0)
        pre_head.next = pHead
        slow = pre_head
        fast = pre_head.next

        while fast:

            while fast.next and fast.val == fast.next.val:
                fast = fast.next

            if slow.next != fast:
                slow.next = fast.next
                # slow = slow.next，只有在fast指针不发生变化时，slow指针才向后移动
                fast = fast.next
            else:
                slow = slow.next
                fast = fast.next

        return pre_head.next






