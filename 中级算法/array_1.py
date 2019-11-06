#!/usr/bin/python
#coding:utf-8

# 三数之和
# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

# 注意：答案中不可以包含重复的三元组。
# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 题目要求不可包含重复的解，
        # 对于排序后的数组，如果num[i] = num[i+1]，那么他们获得的nums[j]和nums[k]肯定是相同的（如果解存在的话），所以应该跳过这种情况。
        # 同理，如果num[j] = num[j+1], 那么也会找到相同的nums[k]。这种情况也应该跳过。
        nums.sort()
        L, res = len(nums), []
        for i in range(L-2):
            #2个挨着的一样就前进一步
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -1 * nums[i]#当前元素变化正负
            j,k = i + 1, L - 1#j：当前的下一个元素， k：最后一个元素
            while j<k:
                if nums[j]+nums[k] == target:#找到2个想加等于target的
                    res.append([nums[i], nums[j], nums[k]])
                    j = j + 1
                    while j<k and nums[j] == nums[j-1]:#继续排除挨着的一样的情况
                        j = j + 1
                elif nums[j] + nums[k] < target:
                    j = j + 1
                else:#j+k>target，则k太大，需要-1
                    k = k - 1
        return res

nums = [-1, 0, 1, 2, -1, -4]
nums = [-4, -1, -1, 0, 1, 2]#sort
s = Solution()
n = s.threeSum(nums)
print(n)