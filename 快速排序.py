#coding:utf-8
import random
class Solution(object):

    def partition(self, nums, left, right):
        pivot = nums[left]

        # 用于确定小于等于基准值的范围
        pos = left

        for i in range(left+1, right+1):
            if nums[i] <= pivot:
                # pos值先加1，为新的小于等于基准值的数腾出位置
                pos += 1
                nums[i], nums[pos] = nums[pos], nums[i]
        # pos处的值调整为基准值
        nums[left],  nums[pos] = nums[pos], nums[left]

        return pos, nums

    def partition2(self, nums, left, right):
        random_index = random.randint(left, right)
        nums[left], nums[random_index] = nums[random_index], nums[left]
        pivot = nums[left]

        # 用于确定小于等于基准值的范围
        pos = left

        for i in range(left + 1, right + 1):
            if nums[i] <= pivot:
                # pos值先加1，为新的小于等于基准值的数腾出位置
                pos += 1
                nums[i], nums[pos] = nums[pos], nums[i]
        # pos处的值调整为基准值
        nums[left], nums[pos] = nums[pos], nums[left]

        return pos, nums

    def quick_sort(self, nums, left, right):
        if left >= right:
            return nums

        pivot_index, nums = self.partition2(nums, left, right)

        nums = self.quick_sort(nums, left, pivot_index - 1)
        nums = self.quick_sort(nums, pivot_index + 1, right)

        return nums

    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return self.quick_sort(nums, 0, len(nums) - 1)

if __name__ == '__main__':
    # print(sorted([-74,48,-20,2,10,-84,-5,-9,11,-24,-91,2,-71,64,63,80,28,-30,-58,-11,-44,-87,-22,54,-74,-10,-55,-28,-46,29,10,50,-72,34,26,25,8,51,13,30,35,-8,50,65,-6,16,-2,21,-78,35,-13,14,23,-3,26,-90,86,25,-56,91,-13,92,-25,37,57,-20,-69,98,95,45,47,29,86,-28,73,-44,-46,65,-84,-96,-24,-12,72,-68,93,57,92,52,-45,-2,85,-63,56,55,12,-85,77,-39]))
    print(Solution().sortArray([-74,48,-20,2,10,-84,-5,-9,11,-24,-91,2,-71,64,63,80,28,-30,-58,-11,-44,-87,-22,54,-74,-10,-55,-28,-46,29,10,50,-72,34,26,25,8,51,13,30,35,-8,50,65,-6,16,-2,21,-78,35,-13,14,23,-3,26,-90,86,25,-56,91,-13,92,-25,37,57,-20,-69,98,95,45,47,29,86,-28,73,-44,-46,65,-84,-96,-24,-12,72,-68,93,57,92,52,-45,-2,85,-63,56,55,12,-85,77,-39]))