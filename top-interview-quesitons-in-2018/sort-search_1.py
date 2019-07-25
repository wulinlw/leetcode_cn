#!/usr/bin/python
#coding:utf-8


# https://leetcode-cn.com/explore/featured/card/top-interview-quesitons-in-2018/270/sort-search/1169/
# 最大数
# 给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

# 示例 1:
# 输入: [10,2]
# 输出: 210
# 示例 2:

# 输入: [3,30,34,5,9]
# 输出: 9534330
# 说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。

# https://blog.csdn.net/qq_39843857/article/details/85263280
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # 假设两个数a和b，若a连b得到的整数比b连a大，则a的权重>b的权重
        if max(nums) == 0:
            return '0'
        nums = list(map(str, nums))
        from functools import cmp_to_key
        nums.sort(key=cmp_to_key(lambda a,b: int(a+b)-int(b+a)), reverse=True)
        # 可以写成
        # cmp = lambda a, b: 1 if (a + b) > (b + a) else -1 if (a + b) < (b + a) else 0
        # nums.sort(key=cmp_to_key(cmp), reverse=True)
        return ''.join(nums)

        

nums = [10,2]
nums = [3,30,34,5,9]
s = Solution()
res = s.largestNumber(nums)
print(res)