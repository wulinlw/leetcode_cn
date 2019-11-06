#!/usr/bin/python
#coding:utf-8


# https://leetcode-cn.com/explore/featured/card/top-interview-quesitons-in-2018/270/sort-search/1173/
# 计算右侧小于当前元素的个数
# 给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。
# 示例:
# 输入: [5,2,6,1]
# 输出: [2,1,1,0] 
# 解释:
# 5 的右侧有 2 个更小的元素 (2 和 1).
# 2 的右侧仅有 1 个更小的元素 (1).
# 6 的右侧有 1 个更小的元素 (1).
# 1 的右侧有 0 个更小的元素.

# https://blog.csdn.net/AGrapier/article/details/80683490
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from bisect import bisect_left
        ans=[]
        tmp = []
        for i in nums[::-1]:
            pos = bisect_left(tmp, i)
            ans.append(pos)#插入的位置，由于是排序的，所以index值就是第几个  等于前面有index个
            tmp.insert(pos, i)
        return list(reversed(ans))


nums = [5,2,6,1]
s = Solution()
res = s.countSmaller(nums)
print(res)