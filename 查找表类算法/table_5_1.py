#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/orignial/card/all-about-lockup-table/240/lookup-table-and-sliding-window/1005/
# 存在重复元素 II
# 给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。

# 示例 1:
# 输入: nums = [1,2,3,1], k = 3
# 输出: true

# 示例 2:
# 输入: nums = [1,0,1,1], k = 1
# 输出: true

# 示例 3:
# 输入: nums = [1,2,3,1,2,3], k = 2
# 输出: false
import collections
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hash={}
        for i in range(len(nums)):
            if(nums[i] not in hash):
                hash[nums[i]]=i
            else:
                if(i-hash[nums[i]]<=k):
                    return True
                else:
                    hash[nums[i]]=i#更新最新的下标
        return False



nums = [1,2,3,1]
k = 3
ss = Solution()
re = ss.containsNearbyDuplicate(nums, k)
print(re)

