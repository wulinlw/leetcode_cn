#!/usr/bin/python
#coding:utf-8

# // 面试题59（一）：滑动窗口的最大值
# // 题目：给定一个数组和滑动窗口的大小，请找出所有滑动窗口里的最大值。例如，
# // 如果输入数组{2, 3, 4, 2, 6, 2, 5, 1}及滑动窗口的大小3，那么一共存在6个
# // 滑动窗口，它们的最大值分别为{4, 4, 6, 6, 6, 5}，

class Solution:
    def maxInWindows(self, nums, size):
        n = len(nums)
        if n == 0 or n<size or size<1:return False
        maxWindow = []
        queue = []                                  #最大值对列,存nums的索引，大->小
        for i in range(size):                               #创建初始窗口最大值队列
            while len(queue)>0 and nums[i] > nums[queue[-1]]:
                queue.pop()
            queue.append(i)
        for i in range(size, n):                            
            maxWindow.append(nums[queue[0]])                    #每次滑动，写入结果集
            while len(queue)>0 and nums[i] > nums[queue[-1]]:   #弹出队列中所有比当前小的
                queue.pop()
            while len(queue)>0 and queue[0] <= i-size:          #窗口向右滑动了，最左边的值（最大）去掉
                queue.pop(0)
            queue.append(i)                                     #写入下表，后面用于判断窗口是否滑动过去了i-size
        maxWindow.append(nums[queue[0]])                        #最后一个值写入

        return maxWindow
    
    def maxSlidingWindow(self, num: List[int], k: int) -> List[int]:
        window ,res = [],[]
        for i in range(len(num)):
            while window and num[window[-1]]<num[i]: #why =,面试题59-II队列最大值好像没有等号,有没有等号皆可以
                window.pop()
            window.append(i)
            if window[0] == i-k:#已超出窗口左端，过时数据丢弃
                window.pop(0)
            if i >=k-1:#要从第k个数据开始输出答案，前面冷启动准备阶段
                res.append(num[window[0]])
        return res

# 作者：keyianpai
# 链接：https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/solution/zui-da-zhi-gai-bian-de-liang-chong-qing-kuang-by-k/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

nums = [2, 3, 4, 2, 6, 2, 5, 1]
size = 3
nums = [1,-1]
size = 1
nums = [7,2,4]
size = 2
obj = Solution()
print(obj.maxInWindows(nums, size))
