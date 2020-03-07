#!/usr/bin/python
#coding:utf-8

# // 面试题31：栈的压入、弹出序列
# // 题目：输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是
# // 否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1、2、3、4、
# // 5是某栈的压栈序列，序列4、5、3、2、1是该压栈序列对应的一个弹出序列，但
# // 4、3、5、1、2就不可能是该压栈序列的弹出序列。
class Solution:
    def is_pop_order(self, push_order, pop_order):
        pushLen = len(push_order)
        popLen = len(pop_order)
        if pushLen != popLen:
            return False
        stack = []
        pushIndex = 0
        popIndex = 0
        while popIndex<popLen:
            while not stack or stack[-1] != pop_order[popIndex]:    #push_order中不相等的入栈
                if pushIndex >= pushLen:
                    break
                stack.append(push_order[pushIndex])
                pushIndex += 1
            if stack[-1] != pop_order[popIndex]:                    #前面入栈完了，顶部和pop_order还是不一样，false
                return False
            stack.pop()                                             #如果一样就pop，pop_order指针后移
            popIndex += 1
        print(popIndex,stack)
        if popIndex==popLen and not stack:                          #跑完popIndex,stack也空了
            return True
        return False


obj = Solution()
print(obj.is_pop_order([1,2,3,4,5], [5,4,3,2,1]))#True
print(obj.is_pop_order([1,2,3,4,5], [4,5,3,2,1]))#True
print(obj.is_pop_order([1,2,3,4,5], [5,4,3,1,2]))#False
