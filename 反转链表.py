# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类
# @return ListNode类
#
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def ReverseList(self , head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p = head
        q = p.next
        r = q.next
        p.next = None

        while r:
            q.next = p
            p = q
            q = r
            r = r.next
        q.next = p
        return q

if __name__ == '__main__':
    test = [1,2,3]
    pHead = ListNode(test[0])
    p = pHead
    for i in range(1,len(test)):
        new_listNode = ListNode(test[i])
        p.next = new_listNode
        p = p. next
    print(Solution().ReverseList(pHead))



