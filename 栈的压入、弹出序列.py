#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pushV int整型一维数组
# @param popV int整型一维数组
# @return bool布尔型
#
from collections import deque
class Solution:
    def IsPopOrder(self , pushV, popV) -> bool:
        pop_stack = deque(popV)
        push_stack = deque([pushV[0]])
        i = 1
        n = len(pushV)
        while len(pop_stack) > 0 and i < n:
            if len(push_stack) == 0:
                push_stack.append(pushV[i])
                i += 1
            if push_stack[-1] == pop_stack[0]:
                pop_stack.popleft()
                push_stack.pop()
                if len(pop_stack) == 0:
                    return True
            else:
                push_stack.append(pushV[i])
                i += 1

        while len(push_stack) > 0:
            if push_stack[-1] == pop_stack[0]:
                pop_stack.popleft()
                push_stack.pop()
                if len(pop_stack) == 0:
                    return True
            else:
                return False
        return False

class Solution2:
    def IsPopOrder(self , pushV, popV) -> bool:
        push_stack = [pushV[0]]
        i = 0
        n = len(pushV)
        while i < n:
            flag = False
            if len(push_stack) == 0:
                push_stack.append(pushV[i])
                i += 1
                flag = True
            if push_stack[i] == popV[-1]:
                popV.pop()
                if len(popV) == 0:
                    return True
            else:
                if not flag:
                    i += 1
                    push_stack.append(pushV[i])

        return False

if __name__ == '__main__':
    print(Solution().IsPopOrder([2,1,0],[1,2,0]))


