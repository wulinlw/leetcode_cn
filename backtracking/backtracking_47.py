#!/usr/bin/python
#coding:utf-8

# 47. 全排列 II
# 给定一个可包含重复数字的序列，返回所有不重复的全排列。
# 示例:

# 输入: [1,1,2]
# 输出:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/permutations-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        re = []
        def bt(nums,tmp):
            if not nums:
                re.append(tmp)
                return 
            for i in range(len(nums)):
                if i>0 and nums[i] == nums[i-1]:
                    continue
                bt(nums[:i]+nums[i+1:], tmp+[nums[i]])
        bt(nums,[])
        return re




nums = [1,1,2]
obj = Solution()
n = obj.permuteUnique(nums)
print('return', n)
