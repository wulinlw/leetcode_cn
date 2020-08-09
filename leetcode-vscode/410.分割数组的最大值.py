#
# @lc app=leetcode.cn id=410 lang=python3
#
# [410] 分割数组的最大值
#
# https://leetcode-cn.com/problems/split-array-largest-sum/description/
#
# algorithms
# Hard (43.18%)
# Likes:    192
# Dislikes: 0
# Total Accepted:    8.9K
# Total Submissions: 19.7K
# Testcase Example:  '[7,2,5,10,8]\n2'
#
# 给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。设计一个算法使得这 m 个子数组各自和的最大值最小。
# 
# 注意:
# 数组长度 n 满足以下条件:
# 
# 
# 1 ≤ n ≤ 1000
# 1 ≤ m ≤ min(50, n)
# 
# 
# 示例: 
# 
# 
# 输入:
# nums = [7,2,5,10,8]
# m = 2
# 
# 输出:
# 18
# 
# 解释:
# 一共有四种方法将nums分割为2个子数组。
# 其中最好的方式是将其分为[7,2,5] 和 [10,8]，
# 因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    # //类似的题目有1014,875,774
    # 动态规划
    # https://leetcode-cn.com/problems/split-array-largest-sum/solution/fen-ge-shu-zu-de-zui-da-zhi-by-leetcode-solution/
    def splitArray2(self, nums: List[int], m: int) -> int:
        n = len(nums)
        f = [[10**18] * (m + 1) for _ in range(n + 1)]
        sub = [0]
        for elem in nums:
            sub.append(sub[-1] + elem)
        
        f[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, min(i, m) + 1):
                for k in range(i):
                    f[i][j] = min(f[i][j], max(f[k][j - 1], sub[i] - sub[k]))
        
        return f[n][m]

    #二分+贪心
    # 子数组的最大值是有范围的，即在区间 [max(nums),sum(nums)][max(nums),sum(nums)] 之中。
    # 令 l=max(nums)，h=sum(nums)l=max(nums)，h=sum(nums)，mid=(l+h)/2mid=(l+h)/2，计算数组和最大值不大于mid对应的子数组个数 cnt(这个是关键！)
    # 如果 cnt>m，说明划分的子数组多了，即我们找到的 mid 偏小，故 l=mid+1l=mid+1；
    # 否则，说明划分的子数组少了，即 mid 偏大(或者正好就是目标值)，故 h=midh=mid。

    # 作者：coder233
    # 链接：https://leetcode-cn.com/problems/split-array-largest-sum/solution/er-fen-cha-zhao-by-coder233-2/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    def splitArray(self, nums: List[int], m: int) -> int:
        def check(x: int) -> bool:
            total, cnt = 0, 1
            for num in nums:
                if total + num > x:
                    cnt += 1
                    total = num
                else:
                    total += num
            return cnt <= m


        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left



# @lc code=end

