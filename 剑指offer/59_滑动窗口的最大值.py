#!/usr/bin/python
#coding:utf-8

# // 面试题59（一）：滑动窗口的最大值
# // 题目：给定一个数组和滑动窗口的大小，请找出所有滑动窗口里的最大值。例如，
# // 如果输入数组{2, 3, 4, 2, 6, 2, 5, 1}及滑动窗口的大小3，那么一共存在6个
# // 滑动窗口，它们的最大值分别为{4, 4, 6, 6, 6, 5}，
from typing import List
class Solution:  
    def maxSlidingWindow(self, num: List[int], k: int) -> List[int]:
        window = []     #窗口，放每次的最小值
        res = []
        for i in range(len(num)):
            while window and num[window[-1]]<num[i]:#小于当前的都弹出去
                window.pop()
            window.append(i)
            if window[0] + k==i:                    #已超出窗口左端，过时数据丢弃
                window.pop(0)
            if i >=k-1:                             #超过窗口才记录结果
                res.append(num[window[0]])
        return res

# 作者：keyianpai
# 链接：https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/solution/zui-da-zhi-gai-bian-de-liang-chong-qing-kuang-by-k/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

nums = [2, 3, 4, 2, 6, 2, 5, 1]
size = 3
# nums = [1,-1]
# size = 1
# nums = [7,2,4]
# size = 2
obj = Solution()
print(obj.maxSlidingWindow(nums, size))
