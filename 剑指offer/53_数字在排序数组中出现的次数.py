#!/usr/bin/python
#coding:utf-8

# // 面试题53（一）：数字在排序数组中出现的次数
# // 题目：统计一个数字在排序数组中出现的次数。例如输入排序数组{1, 2, 3, 3,
# // 3, 3, 4, 5}和数字3，由于3在这个数组中出现了4次，因此输出4。

class Solution:
    def GetNumberOfK(self, nums, k):
        n = len(nums)
        if n==0 or k<=0:return False
        first = self.getFirstK(nums, k, 0, n-1)
        print(first)
        last = self.getLastK(nums, k, 0, n-1)
        if first>=0 and last>=0:
            return last-first+1

    def getFirstK(self, nums, k, start, end):
        if start>end:
            return -1
        mid = (start+end)//2
        if nums[mid] == k:
            if (mid>0 and nums[mid-1] != k) or (mid==0):        #最左边
                return mid
            else:
                end = mid -1
        elif nums[mid]>k:
            end = mid-1
        else:
            start = mid+1
        # print(mid,start,end )
        return self.getFirstK(nums, k, start, end)

    def getLastK(self, nums, k, start, end):
        if start>end:
            return -1
        mid = (start+end)//2
        if nums[mid] == k:
            if (mid<len(nums) and nums[mid+1] != k) or (mid==(len(nums)-1)):#最右边
                return mid
            else:
                start = mid +1
        elif nums[mid]>k:
            end = mid-1
        else:
            start = mid+1
        return self.getLastK(nums, k, start, end)
    
    def search(self, nums, target):
        if not nums:
            return 0

        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if left == len(nums) or nums[left] != target:
            return 0 # 没有找到, 直接返回0
        idx1 = left
        
        # 如果这里能够运行, 肯定是找到了target的
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            # note that change to <=
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        # upper bound 应该是 right - 1
        # 返回 right - 1 - idx1 + 1
        return left - idx1

# 作者：lih
# 链接：https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/solution/python-lower-bound-he-upper-bound-by-lih/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

nums = [1,2,3,3,3,3,4,5]
k = 3
obj = Solution()
print(obj.search(nums, k))