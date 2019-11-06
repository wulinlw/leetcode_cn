#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/featured/card/top-interview-quesitons-in-2018/266/heap-stack-queue/1158/
# 滑动窗口最大值
# 给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口 k 内的数字。滑动窗口每次只向右移动一位。
# 返回滑动窗口最大值。
# 示例:
# 输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7] 
# 解释: 

#   滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# 注意：
# 你可以假设 k 总是有效的，1 ≤ k ≤ 输入数组的大小，且输入数组不为空。
# 进阶：
# 你能在线性时间复杂度内解决此题吗？

# https://blog.csdn.net/fulongxu/article/details/80978243
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 每次滑动窗口都把最大值左边小的数给杀死，也就是出队，后面再滑动窗口进行维护，这样相当于就是每一个数走过场
        # 存放可能是最大值的下标
        maxqueue = []
        # 存放窗口中最大值
        maxlist = []
        n = len(nums)
        # 参数检验
        if n == 0 or k == 0 or k > n:
            return maxlist
        for i in range(n):
            if len(maxqueue) > 0 and i - k >= maxqueue[0]:# 判断队首下标对应的元素是否已经滑出窗口，划出了就去掉maxqueue第一个元素
                maxqueue.pop(0)
            while len(maxqueue) > 0 and nums[i] > nums[maxqueue[-1]]:#如果当前数字大于队列尾，则删除队列尾，直到当前数字小于等于队列尾，或者队列空，然后当前数字入队列 
                maxqueue.pop()
            maxqueue.append(i)#index放入队列
            if i >= k - 1:#窗口第一次移动时，开始记录每一步的最大值
                maxlist.append(nums[maxqueue[0]])#nums[maxqueue[0]]队列中第一位
        return maxlist



nums = [1,3,-1,-3,5,3,6,7]
k = 3
s = Solution()
res = s.maxSlidingWindow(nums, k)
print(res)







