# -*- coding:utf-8 -*-
# 思路：利用双端队列，双端队列只存储可能成为窗口最大值的下标
# 滑动到第i个元素，当第i个元素大于队尾元素时，队尾元素出队，因为队尾元素不可能再成为接下来窗口的最大值了
# 当第i个元素小于队尾元素时，第i个元素入队
# 同时需要不断监测窗口的大小，当窗口满时，需要将队首元素出队

from collections import deque
class Solution:
    def maxInWindows(self, num, size):
        if size == 0 or size > len(num):
            return []

        d = deque()
        for i in range(size):
            while len(d) > 0 and num[i] > num[d[-1]]:
                d.pop()
            d.append(i)

        res = []

        for i in range(size, len(num)):
            res.append(num[d[0]])
            while len(d) > 0 and num[i] > num[d[-1]]:
                d.pop()
            d.append(i)
            while len(d) > 0 and d[0] + size == i:
                d.popleft()

        res.append(num[d[0]])
        return res

if __name__ == '__main__':
    print(Solution().maxInWindows(
[9,10,9,-7,-3,8,2,-6],5))

