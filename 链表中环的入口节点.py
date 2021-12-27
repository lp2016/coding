# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def find_meeting_node(self, pHead):
        slow = pHead
        fast = pHead.next

        while fast:
            if fast.val == slow.val:
                return fast
            slow = slow.next
            if not fast or not fast.next:
                return None
            fast = fast.next.next

        return None

    def cal_circle_length(self, t):

        l = 1
        p = t.next
        while p:
            if p == t:
                return l
            p = p.next
            l += 1


    def EntryNodeOfLoop(self, pHead):
        meeting_node = self.find_meeting_node(pHead)
        if not meeting_node:
            return None
        circle_length = self.cal_circle_length(meeting_node)

        i = 0
        p = pHead
        q = pHead
        while i < circle_length:
            p = p.next
            i += 1

        while q:
            if q == p:
                return q
            q = q.next
            p = p.next


if __name__ == '__main__':
    test = [1,2,3]
    pHead = ListNode(test[0])
    p = pHead
    for i in range(1,len(test)):
        new_listNode = ListNode(test[i])
        p.next = new_listNode
        p = p. next
    new_listNode2 = ListNode(4)
    p.next = new_listNode2
    new_listNode3 = ListNode(5)
    new_listNode2.next = new_listNode3
    new_listNode3.next = p


    print(Solution().EntryNodeOfLoop(pHead))








