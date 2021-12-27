#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param num int整型一维数组
# @param size int整型
# @return int整型一维数组
#
# 思路：利用双端队列，存放可能成为滑动窗口最大值的下标。队列长度等于滑动窗口大小。
# 滑动窗口进行滑动，滑到num[i]时：
# 如果num[i]大于队尾元素，则队尾元素出队（说明队尾元素不可能成为接下来窗口内的最大值了）
# 如果nums[i]小于队尾元素，则num[i]入队（nums[i]还可能成为接下来窗口内的最大值）
# 滑动过程中，要先判断队列是不是满了，满了的话，队首元素要先出队
# 队首元素一直是当前滑动窗口的最大值，直接输出就行

from collections import deque
class Solution:
    def maxInWindows(self , num, size):
        if size >= len(num):
            return [max(num)]

        help = deque(num[0])
        res = []
        window_size = 1
        for i in range(0,size):
            while len(help) > 0:
                if num[i] >= help[-1]:
                    help.pop()
                else:
                    break
            help.append(i)

        res.append(help[0])

        for i in range(size, len(num)):
            if window_size >= size:
                help.popleft()

            while len(help) > 0:
                if num[i] > help[-1]:
                    help.pop()
                else:
                    break

            help.append(num[i])

            res.append(help[0])
        return res

if __name__ == '__main__':
    print(Solution().maxInWindows(
[9,10,9,-7,-3,8,2,-6],5))

