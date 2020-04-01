#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#
# https://leetcode-cn.com/problems/sort-an-array/description/
#
# algorithms
# Medium (53.09%)
# Likes:    68
# Dislikes: 0
# Total Accepted:    29.9K
# Total Submissions: 52.7K
# Testcase Example:  '[5,2,3,1]'
#
# 给你一个整数数组 nums，将该数组升序排列。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [5,2,3,1]
# 输出：[1,2,3,5]
# 
# 
# 示例 2：
# 
# 输入：nums = [5,1,1,2,0,0]
# 输出：[0,0,1,1,2,5]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 50000
# -50000 <= nums[i] <= 50000
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #冒泡排序
        def bubble(nums):
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if nums[i]<nums[j]:
                        nums[i],nums[j] = nums[j],nums[i]
            return nums
        
        #选择排序
        def select(nums):
            for i in range(len(nums)):
                idx = i
                for j in range(i, len(nums)):
                    if nums[i]>nums[j]:
                        idx = j
                nums[i],nums[idx] = nums[idx],nums[i]
            return nums
        
        #插入排序
        def insert(nums):
            for i in range(len(nums)):
                pre = i-1
                cur = nums[i]
                while pre>=0 and nums[pre]>cur:
                    nums[pre+1] = nums[pre]
                    pre -= 1
                nums[pre+1] = cur
            return nums

        #快速排序
        def quick(nums, l, r):
            if l<r:
                pivot = postition(nums, l, r)
                quick(nums, l, pivot-1)                 #不包含pivot
                quick(nums, pivot+1, r)
            return nums

        def postition(nums, l, r):
            i = l-1
            pivot = nums[r]
            for j in range(l, r):
                if nums[j] < pivot:
                    i += 1
                    nums[i],nums[j] = nums[j],nums[i]
            nums[i+1],nums[r] = nums[r],nums[i+1]
            return i+1
        
        #归并排序
        def merge(nums):
            if len(nums)==1:return nums
            mid = len(nums)//2
            return _merge(merge(nums[:mid]), merge(nums[mid:]))

        def _merge(n1, n2):
            re = []
            while n1 and n2:
                if n1[0]<n2[0]:
                    re.append(n1.pop(0))
                else:
                    re.append(n2.pop(0))
            while n1:
                re.append(n1.pop(0))
            while n2:
                re.append(n2.pop(0))
            return re

        #桶排序
        def bucket(nums):
            maxval = max(nums)
            bucket = [0] * (maxval+1)
            for i in nums: 
                bucket[i] += 1
            re = []
            for i in range(len(bucket)):
                while bucket[i]>0:
                    re.append(i)
                    bucket[i] -= 1
            return re

        #奇数排序
        def count(nums):
            re = [0] * len(nums)
            for i in range(len(nums)):
                cnt = 0
                dup = 0
                for j in range(len(nums)):
                    if nums[i] > nums[j]:
                        cnt += 1
                    elif nums[i] == nums[j]:
                        dup += 1
                for k in range(cnt, cnt+dup):
                    re[k] = nums[i]
            return re

        #希尔排序
        def shell(nums):
            gap = len(nums)//2
            while gap>0:
                for i in range(len(nums)):
                    j = i
                    cur = nums[i]
                    while j-gap>=0 and nums[j-gap]>cur:
                        nums[j] = nums[j-gap]
                        j -= gap
                    nums[j] = cur
                gap //=2
            return nums
        
        def heapify(nums, n, i):
            largest = i
            l = 2*i + 1
            r = 2*i + 2
            if l<n and nums[i] < nums[l]:
                largest = l
            if r<n and nums[largest] < nums[r]:
                largest = r
            if largest != i:
                nums[i],nums[largest] = nums[largest],nums[i]
                heapify(nums, n, largest)

        #堆排序
        def heap(nums):
            n = len(nums)
            for i in range(n, -1, -1):
                heapify(nums, n, i)
            for i in range(n-1, 0, -1):
                nums[i],nums[0] = nums[0],nums[i]
                heapify(nums, i, 0)
            return nums

        #基数排序
        def radix_sort(s):
            i = 0                                               # 记录当前正在排拿一位，最低位为1
            max_num = max(s)                                    # 最大值
            j = len(str(max_num))                               # 记录最大值的位数
            while i < j:
                bucket_list =[[] for _ in range(10)]            # 初始化桶数组
                for x in s:
                    bucket_list[int(x / (10**i)) % 10].append(x)# 找到位置放入桶数组
                s.clear()
                # print(bucket_list)
                for x in bucket_list:                           # 放回原序列
                    for y in x:
                        s.append(y)
                # print(s)
                i += 1
            return s


        # return bubble(nums)
        # return select(nums)
        # return insert(nums)
        # return quick(nums, 0, len(nums)-1)
        # return merge(nums)
        # return bucket(nums)
        # return count(nums)
        # return shell(nums)
        return heap(nums)
        # return radix(nums)

        
# @lc code=end

nums = [5,1,1,2,0,0]
o = Solution()
print(o.sortArray(nums))