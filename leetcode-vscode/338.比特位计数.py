#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#
# https://leetcode-cn.com/problems/counting-bits/description/
#
# algorithms
# Medium (74.67%)
# Likes:    273
# Dislikes: 0
# Total Accepted:    33.1K
# Total Submissions: 44.1K
# Testcase Example:  '2'
#
# 给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。
# 
# 示例 1:
# 
# 输入: 2
# 输出: [0,1,1]
# 
# 示例 2:
# 
# 输入: 5
# 输出: [0,1,1,2,1,2]
# 
# 进阶:
# 
# 
# 给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？
# 要求算法的空间复杂度为O(n)。
# 你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount）来执行此操作。
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    # https://leetcode-cn.com/problems/counting-bits/solution/hen-qing-xi-de-si-lu-by-duadua/
    def countBits(self, num: int) -> List[int]:
        dp = [0] * (num+1)
        for i in range(1, num+1):
            if i%2 == 1:                #奇数总比前面的偶数多一个1，就是最低位的1
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = dp[i//2]        #偶数时1的个数和i//2的一样多，最低位是0，相当于右移一位
        return dp        
# @lc code=end
num = 2
o = Solution()
print(o.countBits(num))

# 1    1
# 3   11

# 2     10
# 4    100
# 8   1000
