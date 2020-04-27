#
# @lc app=leetcode.cn id=315 lang=python3
#
# [315] 计算右侧小于当前元素的个数
#
# https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/description/
#
# algorithms
# Hard (37.35%)
# Likes:    207
# Dislikes: 0
# Total Accepted:    14.8K
# Total Submissions: 39.4K
# Testcase Example:  '[5,2,6,1]'
#
# 给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于
# nums[i] 的元素的数量。
# 
# 示例:
# 
# 输入: [5,2,6,1]
# 输出: [2,1,1,0] 
# 解释:
# 5 的右侧有 2 个更小的元素 (2 和 1).
# 2 的右侧仅有 1 个更小的元素 (1).
# 6 的右侧有 1 个更小的元素 (1).
# 1 的右侧有 0 个更小的元素.
# 
# 
#
from typing import List
import bisect
# @lc code=start
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # 注1
        # [5, 3, 6, 1]  => 最后一次合并时的情况: 左数组left = [ [5, 0] ], 右数组right = [ [1, 3], [6, 2] ] (其中第二维为数组原下标)
        # 当 5 < 6 时，因为合并时左右数组均是排序好的，且j初始为mid+1，故j的左边均比5小，所以加 j - mid - 1
        def merge(nums, start, mid, end):
            temp = []
            i, j = start, mid + 1               #分别从起点，中点开始向后对比
            while i <= mid and j <= end:
                if nums[i][0] <= nums[j][0]:
                    temp.append(nums[i])
                    re[nums[i][1]] += j-mid-1   #见函数说明，注1
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            while i <= mid:
                temp.append(nums[i])
                re[nums[i][1]] += j-mid-1
                i += 1
            while j <= end:
                temp.append(nums[j])
                j += 1
            for i in range(len(temp)):
                nums[start + i] = temp[i]       #交换了顺序，num变成从小到大排列

        def mergeSort(nums, start, end):
            if start >= end: return
            mid = (start + end) >> 1
            mergeSort(nums, start, mid)
            mergeSort(nums, mid + 1, end)
            merge(nums, start, mid, end)        #合并的时候，因为要算逆序对，会从起点和中点开始向右走，所以要传mid

        re = [0] * len(nums)
        index = []
        for i in range(len(nums)):              #数组每个元素带上自己的索引
            index.append((nums[i], i))
        mergeSort(index, 0, len(nums) - 1)
        return re

   
    def countSmaller2(self, nums: List[int]) -> List[int]:
        arr = []
        re = []
        for num in nums[::-1]:
            idx = bisect.bisect_left(arr, num)
            re.append(idx)
            bisect.insort(arr, num)
        return re[::-1]                         #倒序排列的，结果需要翻转一下


# @lc code=end

nums = [5,2,6,1]
obj = Solution()
print(obj.countSmaller(nums))