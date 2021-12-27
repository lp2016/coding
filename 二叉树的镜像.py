# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pRoot TreeNode类
# @return TreeNode类
#
class Solution:
    def tree_mirror(self, pRoot):
        if not pRoot:
            return
        tmp = pRoot.left
        pRoot.left = pRoot.right
        pRoot.right = tmp

        self.tree_mirror(pRoot.left)
        self.tree_mirror(pRoot.right)

        return pRoot


    def Mirror(self , pRoot: TreeNode) -> TreeNode:
        return self.tree_mirror(pRoot)


