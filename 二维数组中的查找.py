#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param target int整型
# @param array int整型二维数组
# @return bool布尔型
#
class Solution:
    def Find(self , target, array) -> bool:
        m = len(array)
        n = len(array[0])
        if m == 0 or n == 0:
            return False
        i = 0
        j = n - 1

        while i < m and j >= 0:
            if array[i][j] == target:
                return True
            if array[i][j] > target and i == m - 1:
                return False
            if array[i][j] < target and j == 0:
                return False
            if array[i][j] > target:
                j -= 1
            else:
                i += 1

        while j >= 0:
            if array[i-1][j] == target:
                return True
            j -= 1

        while i < m:
            if array[i][j+1] == target:
                return True
            i += 1

        return False


if __name__ == '__main__':
    print(Solution().Find(2,[[1,1]]))

