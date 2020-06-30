#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (25.70%)
# Likes:    2228
# Dislikes: 0
# Total Accepted:    241.9K
# Total Submissions: 874.9K
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0
# ？请你找出所有满足条件且不重复的三元组。
# 
# 注意：答案中不可以包含重复的三元组。
# 
# 
# 
# 示例：
# 
# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 
# 满足要求的三元组集合为：
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    # 特判，对于数组长度 nn，如果数组为 nullnull 或者数组长度小于 33，返回 [][]。
    # 对数组进行排序。
    # 遍历排序后数组：
    # 若 nums[i]>0nums[i]>0：因为已经排序好，所以后面不可能有三个数加和等于 00，直接返回结果。
    # 对于重复元素：跳过，避免出现重复解
    # 令左指针 L=i+1L=i+1，右指针 R=n-1R=n−1，当 L<RL<R 时，执行循环：
    # 当 nums[i]+nums[L]+nums[R]==0nums[i]+nums[L]+nums[R]==0，执行循环，判断左界和右界是否和下一位置重复，去除重复解。并同时将 L,RL,R 移到下一位置，寻找新的解
    # 若和大于 00，说明 nums[R]nums[R] 太大，RR 左移
    # 若和小于 00，说明 nums[L]nums[L] 太小，LL 右移
    # https://leetcode-cn.com/problems/3sum/solution/pai-xu-shuang-zhi-zhen-zhu-xing-jie-shi-python3-by/
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=[]
        if(not nums or n<3):
            return []
        nums.sort()                                             #先排序
        res=[]
        for i in range(n):
            if(nums[i]>0):                                      #当前大于0，后面的都大于他，和不可能为0，直接返回结果
                return res
            if(i>0 and nums[i]==nums[i-1]):                     #连续相同的跳过
                continue
            L=i+1                                               #初始化l为下一个，r为最右
            R=n-1
            while(L<R):
                if(nums[i]+nums[L]+nums[R]==0):                 
                    res.append([nums[i],nums[L],nums[R]])       #找到了，下面跳过左右指针的相同值
                    while(L<R and nums[L]==nums[L+1]):
                        L=L+1
                    while(L<R and nums[R]==nums[R-1]):
                        R=R-1
                    L=L+1
                    R=R-1
                elif(nums[i]+nums[L]+nums[R]>0):                #大于0右边-1，反之左边+1
                    R=R-1
                else:
                    L=L+1
        return res

# @lc code=end

