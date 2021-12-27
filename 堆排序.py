#coding:utf-8
# 以大根堆为例
# 1.将待排序数组看成一个平衡二叉树
# 2.建堆：从最后一个非叶子节点开始（n / 2），不断调整二叉树，使其根节点的值大于左右孩子的值
# 3.交换数组未排序部分的最后一个元素和堆顶元素
# 4.交换后，数组未排序部分不再是堆了,需要调整成堆，重复步骤3、4

class Solution(object):

    # 建堆
    def build_heap(self, nums):
        n = len(nums)
        for i in range(int(n/2), -1, -1):
            self.modify_heap(nums, i, n)

    # 调整堆
    def modify_heap(self, nums, i, n):

        while 2 * i + 1 < n:
            left = 2 * i + 1
            right = 2 * i + 2
            if right >= n or nums[left] > nums[right]:
                large_index = left
            else:
                large_index = right
            if nums[i] < nums[large_index]:
                nums[i], nums[large_index] = nums[large_index], nums[i]
                i = large_index
            else:
                break

    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        self.build_heap(nums)

        # 交换堆顶元素
        n = len(nums)
        for i in range(n-1, -1, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.modify_heap(nums, 0, i)

        return nums


if __name__ == '__main__':
    print(Solution().sortArray([5,2,3,1]))