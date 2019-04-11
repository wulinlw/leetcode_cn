#!/usr/bin/python
#coding:utf-8

# 递增的三元子序列
# 给定一个未排序的数组，判断这个数组中是否存在长度为 3 的递增子序列。

# 数学表达式如下:

# 如果存在这样的 i, j, k,  且满足 0 ≤ i < j < k ≤ n-1，
# 使得 arr[i] < arr[j] < arr[k] ，返回 true ; 否则返回 false 。
# 说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1) 。

# 示例 1:

# 输入: [1,2,3,4,5]
# 输出: true
# 示例 2:

# 输入: [5,4,3,2,1]
# 输出: false

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 如果小于等于first,赋值给first，
        # 如果小于等于second，赋值给second，
        # 如果没地方赋值了，说明递增序列中的第三个找到了
        if len(nums) < 3 or nums is None:
            return False
        one = pow(2, 32) -1
        second = pow(2, 32) - 1
 
        for num in nums:
            if num <= one:
                one = num
            elif num <= second and num > one:
                second = num
            else:
                return True
        return False


nums = [1,2,3,4,5]
s = Solution()
n = s.increasingTriplet(nums)
print(n)
