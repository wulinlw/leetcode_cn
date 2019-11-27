#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/orignial/card/all-about-lockup-table/240/lookup-table-and-sliding-window/1007/
# 存在重复元素 III
# 给定一个整数数组，判断数组中是否有两个不同的索引 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值最大为 t，并且 i 和 j 之间的差的绝对值最大为 ķ。

# 示例 1:
# 输入: nums = [1,2,3,1], k = 3, t = 0
# 输出: true

# 示例 2:
# 输入: nums = [1,0,1,1], k = 1, t = 2
# 输出: true

# 示例 3:
# 输入: nums = [1,5,9,1,5,9], k = 2, t = 3
# 输出: false
import collections
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0 or k < 0:
            return False
        all_buckets = {}
        bucket_size = t + 1                     # 桶的大小设成t+1更加方便
        for i in range(len(nums)):
            bucket_num = nums[i] // bucket_size # 放入哪个桶
            
            if bucket_num in all_buckets:       # 桶中已经有元素了
                return True
            
            all_buckets[bucket_num] = nums[i]   # 把nums[i]放入桶中
            
            if (bucket_num - 1) in all_buckets and abs(all_buckets[bucket_num - 1] - nums[i]) <= t: # 检查前一个桶
                return True
            
            if (bucket_num + 1) in all_buckets and abs(all_buckets[bucket_num + 1] - nums[i]) <= t: # 检查后一个桶
                return True
            
            # 如果不构成返回条件，那么当i >= k 的时候就要删除旧桶了，以维持桶中的元素索引跟下一个i+1索引只差不超过k
            if i >= k:
                all_buckets.pop(nums[i-k]//bucket_size)
                
        return False

    # 也是查找表与滑动窗口的思路：维持滑动窗的大小最大为 k，遍历每一个元素 nums[i]，
    # 在活动窗口中寻找 |one-nums[i]| < t，即窗口中的元素范围为：[one-t … one+t] 之间。
    def containsNearbyAlmostDuplicate2(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        n = len(nums)
        if n <= 1:
            return False
        recode = set()
        for i in range(n):
            if t == 0:
                if nums[i] in recode:
                    return True
            else:
                for one in recode:
                    if abs(nums[i] - one) <= t:
                        return True
            recode.add(nums[i])

            if (len(recode) > k):
                recode.remove(nums[i - k])
        return False


nums = [1,2,3,1]
k = 3
t = 0
ss = Solution()
re = ss.containsNearbyAlmostDuplicate(nums, k, t)
print(re)

