#!/usr/bin/python
#coding:utf-8
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


nums1 = [1, 2, 2, 1]
nums2 = [2, 2, 1]

s = Solution()
n = s.intersect(nums1, nums2)
print('return', n)
