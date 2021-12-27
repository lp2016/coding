
class Solution(object):

    def merge_sort(self, nums, left, right):
        if left >= right:
            return

        mid = int((left + right) / 2)
        self.merge_sort(nums, left, mid)
        self.merge_sort(nums, mid + 1, right)

        i = left
        j = mid + 1
        tmp = []
        while i <= mid and j <= right:
            if nums[i] > nums[j]:
                tmp.append(nums[j])
                j += 1
            else:
                tmp.append(nums[i])
                i += 1

        while i <= mid:
            tmp.append(nums[i])
            i += 1

        while j <= right:
            tmp.append(nums[j])
            j += 1
        nums[left:right+1] = tmp[:]
        return

    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.merge_sort(nums, 0, len(nums) - 1)
        return nums


if __name__ == '__main__':
    print(Solution().sortArray([5,2,3,1]))