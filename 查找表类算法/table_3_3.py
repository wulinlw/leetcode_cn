#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/orignial/card/all-about-lockup-table/238/lookup-table-related-sum-questions/995/
# 四数之和
# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

# 注意：
# 答案中不可以包含重复的四元组。
# 示例：
# 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

# 满足要求的四元组集合为：
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]
import collections
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 使用双循环固定两个数，用双指针找另外两个数，通过比较与target 的大小，移动指针。
        # 里面有一些优化，可以直接看代码，很好理解！
        # 所以时间复杂度不超过O(n^3)
        n = len(nums)
        if n < 4: return []
        nums.sort()
        res = []
        for i in range(n-3):
            # 防止重复 数组进入 res
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # 当数组最小值和都大于target 跳出
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            # 当数组最大值和都小于target,说明i这个数还是太小,遍历下一个
            if nums[i] + nums[n-1] + nums[n-2] + nums[n-3] < target:
                continue
            for j in range(i+1,n-2):
                # 防止重复 数组进入 res
                if j - i > 1 and nums[j] == nums[j-1]:
                    continue
                # 同理
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                # 同理
                if nums[i] + nums[j] + nums[n-1] + nums[n-2] < target:
                    continue
                # 双指针
                left = j + 1
                right = n - 1
                while left < right:
                    tmp = nums[i] + nums[j] + nums[left] + nums[right]
                    if tmp == target:
                        res.append([nums[i],nums[j],nums[left],nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif tmp > target:
                        right -= 1
                    else:
                        left += 1
        return res

# 作者：powcai
# 链接：https://leetcode-cn.com/problems/4sum/solution/gu-ding-liang-ge-shu-yong-shuang-zhi-zhen-zhao-lin/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

nums = [1, 0, -1, 0, -2, 2]
target = 0
ss = Solution()
re = ss.fourSum(nums, target)
print(re)

