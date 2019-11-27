#!/usr/bin/python
#coding:utf-8
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/26/
# 两个数组的交集 II
# 给定两个数组，编写一个函数来计算它们的交集。

# 示例 1:

# 输入: nums1 = [1,2,2,1], nums2 = [2,2]
# 输出: [2,2]
# 示例 2:

# 输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出: [4,9]
# 说明：

# 输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
# 我们可以不考虑输出结果的顺序。
# 进阶:

# 如果给定的数组已经排好序呢？你将如何优化你的算法？
# 如果 nums1 的大小比 nums2 小很多，哪种方法更优？
# 如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        使用hash对比
        """
        hash1 = {}
        hash2 = {}
        intersect = []
        for i in nums1:
            if hash1.has_key(i):
                hash1[i] += 1
            else:
                hash1[i] = 1
        for i in nums2:
            if hash2.has_key(i):
                hash2[i] += 1
            else:
                hash2[i] = 1
        for i in hash1.keys():
            if hash2.has_key(i):
                less = (hash2[i] if (hash1[i] > hash2[i]) else hash1[i])
                for k in range(less):
                    intersect.append(i)
        return intersect

    # 排序，双指针
    def intersect_best(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        nums1.sort()
        nums2.sort()
        i = j = 0
        while i<len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                ans.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i] < nums2[j]:
                i+=1
            else:
                j+=1
        return ans

    def intersect3(self, nums1, nums2):
        re = []
        nums1.sort()
        nums2.sort()
        while nums1 and nums2:
            if nums1[0]>=nums2[0]:
                re.append(nums2.pop(0))
            else:
                re.append(nums1.pop(0))
        while nums1:
            re.append(nums1.pop(0))
        while nums2:
            re.append(nums2.pop(0))
        return re

nums1 = [1, 2, 2, 1]
nums2 = [2, 2, 1]

s = Solution()
n = s.intersect(nums1, nums2)
print('return', n)
