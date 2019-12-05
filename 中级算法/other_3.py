#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/54/others/121/
# 求众数
# 给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
# 你可以假设数组是非空的，并且给定的数组总是存在众数。

# 示例 1:
# 输入: [3,2,3]
# 输出: 3
# 示例 2:

# 输入: [2,2,1,1,1,2,2]
# 输出: 2

# https://blog.csdn.net/qq_17550379/article/details/83788426
# https://blog.csdn.net/qq_17550379/article/details/83818965
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 摩尔投票算法
        res = cnt = 0
        for num in nums:
            if cnt == 0:
                res = num
                cnt += 1
            elif res == num:
                cnt += 1
            else:
                cnt -= 1
            print(res,cnt)
        return res

    def majorityElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)//2]

nums = [3,2,3,2,2]
s = Solution()
n = s.majorityElement(nums)
print(n)









