# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类
# @param val int整型
# @return ListNode类
#
class ListNode:
    def __int__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self , head: ListNode, val: int) -> ListNode:
        p = head
        if not p:
            return p
        if p.val == val:
            return p.next
        q = p.next

        while q:
            if q.val == val:
                p.next = q.next
                return head
            p = p.next
            q = q.next

        return head




