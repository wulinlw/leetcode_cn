#
# @lc app=leetcode.cn id=945 lang=python3
#
# [945] 使数组唯一的最小增量
#
# https://leetcode-cn.com/problems/minimum-increment-to-make-array-unique/description/
#
# algorithms
# Medium (42.58%)
# Likes:    37
# Dislikes: 0
# Total Accepted:    5.9K
# Total Submissions: 13.3K
# Testcase Example:  '[1,2,2]'
#
# 给定整数数组 A，每次 move 操作将会选择任意 A[i]，并将其递增 1。
# 
# 返回使 A 中的每个值都是唯一的最少操作次数。
# 
# 示例 1:
# 
# 输入：[1,2,2]
# 输出：1
# 解释：经过一次 move 操作，数组将变为 [1, 2, 3]。
# 
# 示例 2:
# 
# 输入：[3,2,1,2,1,7]
# 输出：6
# 解释：经过 6 次 move 操作，数组将变为 [3, 4, 1, 2, 5, 7]。
# 可以看出 5 次或 5 次以下的 move 操作是不能让数组的每个值唯一的。
# 
# 
# 提示：
# 
# 
# 0 <= A.length <= 40000
# 0 <= A[i] < 40000
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    # 排序后只需要把后面的数变成比前一个数大一即可
    # O(nlogn) 有sort
    def minIncrementForUnique2(self, A: List[int]) -> int:
        A.sort()
        res = 0
        for i in range(1, len(A)):
            if A[i] <= A[i-1]:
                res += A[i-1]-A[i]+1
                A[i] = A[i-1]+1
        print(A)
        return res

    # 线性探测法O(N) （含路径压缩）
    # https://leetcode-cn.com/problems/minimum-increment-to-make-array-unique/solution/ji-shu-onxian-xing-tan-ce-fa-onpai-xu-onlogn-yi-ya/
    def minIncrementForUnique(self, A: List[int]) -> int:
        def findPos(a):
            b = pos[a]
            if b==-1:           #如果a对应的位置pos[a]是空位，直接放入即可。
                pos[a] = a 
                return a
            b = findPos(b+1)    #否则向后寻址,因为pos[a]中标记了上次寻址得到的空位，因此从pos[a]+1开始寻址就行了（不需要从a+1开始）。
            pos[a] = b          #寻址后的新空位要重新赋值给pos[a]哦，路径压缩就是体现在这里。
            return b

        pos = [-1]*80000
        move = 0
        for a in A: 
            b = findPos(a)      #寻址后的新空位要重新赋值给pos[a]哦，路径压缩就是体现在这里。
            print(b,a)
            move += b-a
        return move


# @lc code=end

A = [1,2,2]
A = [3,2,1,2,1,7]
o = Solution()
print(o.minIncrementForUnique(A))