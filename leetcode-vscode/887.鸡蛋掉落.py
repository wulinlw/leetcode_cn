#
# @lc app=leetcode.cn id=887 lang=python3
#
# [887] 鸡蛋掉落
#
# https://leetcode-cn.com/problems/super-egg-drop/description/
#
# algorithms
# Hard (20.97%)
# Likes:    205
# Dislikes: 0
# Total Accepted:    9.8K
# Total Submissions: 44.5K
# Testcase Example:  '1\n2'
#
# 你将获得 K 个鸡蛋，并可以使用一栋从 1 到 N  共有 N 层楼的建筑。
# 
# 每个蛋的功能都是一样的，如果一个蛋碎了，你就不能再把它掉下去。
# 
# 你知道存在楼层 F ，满足 0 <= F <= N 任何从高于 F 的楼层落下的鸡蛋都会碎，从 F 楼层或比它低的楼层落下的鸡蛋都不会破。
# 
# 每次移动，你可以取一个鸡蛋（如果你有完整的鸡蛋）并把它从任一楼层 X 扔下（满足 1 <= X <= N）。
# 
# 你的目标是确切地知道 F 的值是多少。
# 
# 无论 F 的初始值如何，你确定 F 的值的最小移动次数是多少？
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：K = 1, N = 2
# 输出：2
# 解释：
# 鸡蛋从 1 楼掉落。如果它碎了，我们肯定知道 F = 0 。
# 否则，鸡蛋从 2 楼掉落。如果它碎了，我们肯定知道 F = 1 。
# 如果它没碎，那么我们肯定知道 F = 2 。
# 因此，在最坏的情况下我们需要移动 2 次以确定 F 是多少。
# 
# 
# 示例 2：
# 
# 输入：K = 2, N = 6
# 输出：3
# 
# 
# 示例 3：
# 
# 输入：K = 3, N = 14
# 输出：4
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= K <= 100
# 1 <= N <= 10000
# 
# 
#

# @lc code=start
class Solution:
    # 基于dpTable[k][m] = n:
    # 记作当前有K个鸡蛋，可以尝试扔m次，在最坏情况下可以测试一栋高为n的楼层
    # dp[k][m] = dp[k-1][m-1] + dp[k][m-1] + 1
    # dp[k-1][m-1]       蛋碎了，就是楼下的楼层数，因为鸡蛋个数 k 减一，同时扔鸡蛋次数 m 减一。
    # dp[k][m-1] + 1     蛋没碎，就是楼上的楼层数，因为鸡蛋个数 k 不变，扔鸡蛋次数 m 减一；+1当前楼层
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[0 for i in range(N+1)] for i in range(K+1)]
        m = 0
        while dp[K][m] < N:
            m += 1
            for k in range(1, K+1):
                dp[k][m] = dp[k-1][m-1] + dp[k][m-1] + 1
        # print(dp)
        return m
    
    #最简单解法，O(K*N^2)
    def superEggDrop2(self, K: int, N: int) -> int:
        cache = {}
        def dp(K, N):
            if K==1:return N
            if N==0:return 0
            if (K, N) in cache:
                return cache[(K, N)]
            re = float('inf')
            for i in range(1, N+1):
                re = min(
                        re, 
                        max(dp(K, N-i), dp(K-1, i-1)) + 1
                        )
            cache[(K, N)] = re
            return re
        return dp(K, N)



    # 优化，二分,O(K*NlogN)
    # https://leetcode-cn.com/problems/super-egg-drop/solution/ji-ben-dong-tai-gui-hua-jie-fa-by-labuladong/
    def superEggDrop3(self, K: int, N: int) -> int:
        cache = {}
        def dp(K, N):
            if K==1:return N
            if N==0:return 0
            if (K, N) in cache:
                return cache[(K, N)]
            res = float('inf')

            l, r = 1, N 
            while l <= r:
                mid = (l + r) // 2
                broken = dp(K-1, mid-1)
                not_broken = dp(K, N-mid)
                if broken > not_broken:             #碎了 > 没碎
                    r = mid - 1                     #往楼下找到刚好没碎的那一层
                    res = min(res, broken+1)
                else:
                    l = mid + 1                     #没碎，往上走
                    res = min(res, not_broken+1)
            cache[(K, N)] = res
            return res
        return dp(K, N)
        
# @lc code=end


K = 1
N = 2
K = 3
N = 14
o = Solution()
print(o.superEggDrop2(K,N))
print(o.superEggDrop3(K,N))
