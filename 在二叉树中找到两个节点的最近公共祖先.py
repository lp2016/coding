# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param root TreeNode类
# @param o1 int整型
# @param o2 int整型
# @return int整型
#
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def dfs(self, root, o1, o2):
        if not root:
            return False, False, None
        o1_flag, o2_flag, ancestor_node_l = self.dfs(root.left, o1, o2)
        o3_flag, o4_flag, ancestor_node_r = self.dfs(root.right, o1, o2)

        if o1_flag and o2_flag:
            return o1_flag, o2_flag, ancestor_node_l
        if o3_flag and o4_flag:
            return o3_flag, o4_flag, ancestor_node_r

        if (o1_flag and o4_flag) or (o2_flag and o3_flag):
            return True, True, root

        if root.val == o1:
            o1_flag = True
        if root.val == o2:
            o2_flag = True

        return o1_flag or o3_flag, o2_flag or o4_flag, root

    def lowestCommonAncestor(self , root: TreeNode, o1: int, o2: int) -> int:
        o1_flag, o2_flag, root = self.dfs(root, o1, o2)
        return root.val

if __name__ == '__main__':
    a = [TreeNode(i) for i in range(9)]
    a[3].left = a[5]
    a[3].right = a[1]
    a[5].left = a[6]
    a[5].right = a[2]
    a[2].left = a[7]
    a[2].right = a[4]
    a[3].right = a[1]
    a[1].left = a[0]
    a[1].right = a[8]
    print(Solution().lowestCommonAncestor(a[3], 5, 1))