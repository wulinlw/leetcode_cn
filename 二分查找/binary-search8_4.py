#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/learn/card/binary-search/215/more-practices-ii/861/
# 分割数组的最大值
# 给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。设计一个算法使得这 m 个子数组各自和的最大值最小。

# 注意:
# 数组长度 n 满足以下条件:
# 1 ≤ n ≤ 1000
# 1 ≤ m ≤ min(50, n)
# 示例:
# 输入:
# nums = [7,2,5,10,8]
# m = 2
# 输出:
# 18

# 解释:
# 一共有四种方法将nums分割为2个子数组。
# 其中最好的方式是将其分为[7,2,5] 和 [10,8]，
# 因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        # 首先分析题意，可以得出结论，结果必定落在【max（nums）， sum（nums）】这个区间内，因为左端点对应每个单独的元素构成一个子数组，右端点对应所有元素构成一个子数组。
        # 然后可以利用二分查找法逐步缩小区间范围，当区间长度为1时，即找到了最终答案。
        # 每次二分查找就是先算一个mid值，这个mid就是代表当前猜测的答案，然后模拟一下划分子数组的过程，可以得到用这个mid值会一共得到的子区间数cnt，然后比较cnt和m的关系，来更新区间范围。
        # 本题跟1014 875 非常类似。
        if len(nums) == m:
            return max(nums)
        
        lo, hi = max(nums), sum(nums)
        while(lo < hi):
            mid = (lo + hi) // 2 # 最大和
            
            #------以下在模拟划分子数组的过程
            temp, cnt = 0, 1
            for num in nums:
                temp += num
                # cnt += 1
                if temp > mid:#说明当前这个子数组的和已经超过了允许的最大值mid，需要把当前元素放在下一个子数组里
                    temp = num
                    cnt += 1
            # print temp, cnt, mid
            #------以上在模拟划分子数组的过程
            
            if cnt > m: #说明分出了比要求多的子数组，多切了几刀，说明mid应该加大，这样能使子数组的个数减少
                lo = mid + 1
            elif cnt <= m:
                hi = mid

                
        return lo




nums = [7,2,5,10,8]
m = 2
ss = Solution()
re = ss.splitArray(nums,m)
print(re)

