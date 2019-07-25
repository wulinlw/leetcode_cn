#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/featured/card/top-interview-quesitons-in-2018/270/sort-search/1170/
# 摆动排序 II
# 给定一个无序的数组 nums，将它重新排列成 nums[0] < nums[1] > nums[2] < nums[3]... 的顺序。
# 示例 1:
# 输入: nums = [1, 5, 1, 1, 6, 4]
# 输出: 一个可能的答案是 [1, 4, 1, 5, 1, 6]
# 示例 2:

# 输入: nums = [1, 3, 2, 2, 3, 1]
# 输出: 一个可能的答案是 [2, 3, 1, 3, 1, 2]
# 说明:
# 你可以假设所有输入都会得到有效的结果。

# 进阶:
# 你能用 O(n) 时间复杂度和 / 或原地 O(1) 额外空间来实现吗？


class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 我们可以先给数组排序，
        # 找到数组的中间的数，相当于把有序数组从中间分成两部分，
        # 然后从前半段的末尾取一个，在从后半的末尾去一个，这样保证了第一个数小于第二个数，
        # 然后从前半段取倒数第二个，从后半段取倒数第二个，这保证了第二个数大于第三个数，且第三个数小于第四个数，
        # 以此类推直至都取完
        nums.sort()
        half = len(nums[::2])
        # print nums
        # print nums[::2],nums[1::2]
        # print nums[:half][::-1], nums[half:][::-1]
        # 奇数位，偶数位 = 前半段倒序，后半段倒序
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
        print nums



nums = [1, 5, 1, 1, 6, 4]
s = Solution()
res = s.wiggleSort(nums)
print(res)

