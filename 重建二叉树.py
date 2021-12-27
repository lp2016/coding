# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pre int整型一维数组
# @param vin int整型一维数组
# @return TreeNode类
#

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def build_tree(self, pre, vin):
        if len(pre) == 1:
            return TreeNode(pre[0])
        root_node = TreeNode(pre[0])
        vin_index = vin.index(pre[0])

        root_node.left = self.build_tree(pre[1:vin_index+1], vin[0:vin_index])
        root_node.right = self.build_tree(pre[vin_index+1:], vin[vin_index+1:])



    def reConstructBinaryTree(self , pre, vin) -> TreeNode:
        if len(pre) == 0:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        root_node = TreeNode(pre[0])
        vin_index = vin.index(pre[0])

        root_node.left = self.reConstructBinaryTree(pre[1:vin_index+1], vin[0:vin_index])
        root_node.right = self.reConstructBinaryTree(pre[vin_index+1:], vin[vin_index+1:])

        return root_node


if __name__ == '__main__':
    print(Solution().reConstructBinaryTree([1,2,4,7,3,5,6,8],[4,7,2,1,5,3,8,6]))


