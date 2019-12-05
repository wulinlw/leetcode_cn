#!/usr/bin/python
#coding:utf-8

# 414. 第三大的数
# 给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。

# 示例 1:
# 输入: [3, 2, 1]
# 输出: 1
# 解释: 第三大的数是 1.

# 示例 2:
# 输入: [1, 2]
# 输出: 2
# 解释: 第三大的数不存在, 所以返回最大的数 2 .

# 示例 3:
# 输入: [2, 2, 3, 1]
# 输出: 1
# 解释: 注意，要求返回第三大的数，是指第三大且唯一出现的数。
# 存在两个值为2的数，它们都排第二。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/third-maximum-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = [float('-inf')]*3
        for i in nums:
            if i in d:
                continue
            if i>d[0]:
                d[2]=d[1]
                d[1]=d[0]
                d[0]= i
            elif i>d[1]:
                d[2]=d[1]
                d[1] = i
            elif i>d[2]:
                d[2] = i
            # print(i,d)
        if d[2] == float('-inf'):
            return max(d)
        return d[2]




obj = Solution()
nums = [3, 2, 1]
# nums = [1,2]
# nums = [2,2,3,1]
# nums = [5,2,2]
# nums = [1,2,2,5,3,5]
n = obj.thirdMax(nums)
print('return', n)