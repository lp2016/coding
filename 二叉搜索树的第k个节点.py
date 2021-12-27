# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param proot TreeNode类
# @param k int整型
# @return int整型
#
class Solution:
    def cal_kthNode(self, proot, k):
        if not proot:
            return None, k

        kthNode, k = self.cal_kthNode(proot.left, k)
        if k == 1 and kthNode:
            return kthNode, k
        if k == 1:
            return proot, k
        k = k - 1
        kthNode, k = self.cal_kthNode(proot.right, k)
        return kthNode, k


    def KthNode(self , proot: TreeNode, k: int) -> int:
        if not proot:
            return -1
        p, k = self.cal_kthNode(proot, k)
        if not p:
            return -1
        return p.val

