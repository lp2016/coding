# coding=utf-8
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pHead ListNode类
# @param k int整型
# @return ListNode类
#
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def FindKthToTail(self , pHead: ListNode, k: int) -> ListNode:
        n = 0
        p = pHead
        while p:
            n += 1
            p = p.next
        if n < k:
            return None

        i = 0
        p = pHead
        while p:
            i += 1
            if i == n - k + 1:
                return p
            p = p.next
        return None

class Solution2:
    def FindKthToTail(self , pHead: ListNode, k: int) -> ListNode:
        p = pHead
        q = pHead
        i = 1

        while p and i < k:
            i += 1
            p = p.next
        if not p:
            return None
        while p.next:
            p = p.next
            q = q.next
        return q




if __name__ == '__main__':
    test = [1,2,3,4,5]
    pHead = ListNode(test[0])
    p = pHead
    for i in range(1,len(test)):
        new_listNode = ListNode(test[i])
        p.next = new_listNode
        p = p. next
    print(Solution2().FindKthToTail(pHead, 6))






