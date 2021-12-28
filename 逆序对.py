
class Solution(object):

    def merge_sort(self, nums, left, right):
        if left >= right:
            return 0

        mid = int((left + right) / 2)
        ans_l = self.merge_sort(nums, left, mid)
        ans_r = self.merge_sort(nums, mid + 1, right)

        ans = 0
        i = left
        j = mid + 1
        tmp = []
        while i <= mid and j <= right:
            if nums[i] > nums[j]:
                tmp.append(nums[j])
                j += 1
                ans += mid - i + 1
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
        return ans + ans_l + ans_r

    def InversePairs(self, data):
        # write code here
        ans = self.merge_sort(data, 0, len(data) - 1) % 1000000007

        return ans


if __name__ == '__main__':
    print(Solution().sortArray([5,2,3,1]))