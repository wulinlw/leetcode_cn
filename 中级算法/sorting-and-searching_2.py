#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/50/sorting-and-searching/97/
# 前K个高频元素
# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

# 示例 1:
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
# 示例 2:

# 输入: nums = [1], k = 1
# 输出: [1]
# 说明：

# 你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
# 你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。


# http://www.cnblogs.com/xugenpeng/p/9950007.html#python-%E5%AE%9E%E7%8E%B0
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 桶排序（bucket sort）
        # 统计元素的频率
        freq_dict = dict()
        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1
        print(freq_dict)

        # 桶排序
        bucket = [[] for _ in range(len(nums) + 1)]#创建一个桶数组
        for key, value in freq_dict.items():
            bucket[value].append(key)#越多的元素越是排在后面，bucket中index元素存储的是出现index次数的元素 
        print(bucket)

        # 逆序取出前k个元素，从后往前即可
        ret = list()
        for i in range(len(nums), -1, -1):
            print(i)
            if bucket[i]:
                ret.extend(bucket[i])
            if len(ret) >= k:
                break
        return ret[:k]

nums = [1,1,1,2,2,3,3,3]
k = 2
s = Solution()
r = s.topKFrequent(nums,k)
print(r)




