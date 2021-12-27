# -*- coding:utf-8 -*-
# 思路：不需要递归，只需要分情况循环遍历即可
# 1.如果右孩子不为空，下一节点是右孩子的最左节点
# 2.如果右孩子为空，向上回退，找到第一个节点r，满足当前节点位于r的左子树，则r是当前节点的下一个节点


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    def GetNext(self, pNode):
        if not pNode:
            return None

        # 如果右孩子不为空，下一个节点是：右孩子的最左节点
        if pNode.right:
            p = pNode.right
            while p:
                if not p.left:
                    return p
                p = p.left

        # 如果右孩子为空，向上查找，找到第一个节点r，满足当前节点在r的右子树
        p = pNode
        if not pNode.right:
            while p.next:
                if p.next.left == p:
                    return p.next
                p = p.next
        return None




