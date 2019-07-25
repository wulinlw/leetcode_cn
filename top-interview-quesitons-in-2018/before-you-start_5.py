#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/featured/card/top-interview-quesitons-in-2018/261/before-you-start/1110/
# 鸡蛋掉落
# 你将获得 K 个鸡蛋，并可以使用一栋从 1 到 N  共有 N 层楼的建筑。
# 每个蛋的功能都是一样的，如果一个蛋碎了，你就不能再把它掉下去。
# 你知道存在楼层 F ，满足 0 <= F <= N 任何从高于 F 的楼层落下的鸡蛋都会碎，从 F 楼层或比它低的楼层落下的鸡蛋都不会破。
# 每次移动，你可以取一个鸡蛋（如果你有完整的鸡蛋）并把它从任一楼层 X 扔下（满足 1 <= X <= N）。
# 你的目标是确切地知道 F 的值是多少。
# 无论 F 的初始值如何，你确定 F 的值的最小移动次数是多少？

# 示例 1：
# 输入：K = 1, N = 2
# 输出：2
# 解释：
# 鸡蛋从 1 楼掉落。如果它碎了，我们肯定知道 F = 0 。
# 否则，鸡蛋从 2 楼掉落。如果它碎了，我们肯定知道 F = 1 。
# 如果它没碎，那么我们肯定知道 F = 2 。
# 因此，在最坏的情况下我们需要移动 2 次以确定 F 是多少。
# 示例 2：

# 输入：K = 2, N = 6
# 输出：3
# 示例 3：

# 输入：K = 3, N = 14
# 输出：4
 
# 提示：
# 1 <= K <= 100
# 1 <= N <= 10000


# https://www.cnblogs.com/yunlambert/p/10028865.html
# https://blog.csdn.net/qq_35170267/article/details/84330662
# 首先找出状态转移方程，令二维数组dp[K][Step], K表示鸡蛋个数，Step表示第几次摔落。dp[i][j] 表示i个鸡蛋经过j次摔落最多可以确定多少层楼。显然j <= N。
# 求d[i][j]
# 当第j次摔落鸡蛋不破，我们可以继续往上确定dp[i][j - 1]层
# 当第j次摔落鸡蛋不破，我们最多只能确定dp[i - 1][j - 1]层
# 状态方程 d[i][j] = dp[i - 1][j - 1] + ( dp[i][j - 1] + 1 ) 最后的1表示本层
class Solution(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        dp = [[0 for _ in range(N + 1)] for _ in range(K + 1)]
        print dp
        for i in range(1, K + 1):#k个鸡蛋
            for step in range(1, N + 1):#n层楼
                dp[i][step] = dp[i - 1][step - 1] + dp[i][step - 1] + 1#当前情况=丢下去碎了，消耗一步能确定的层数+丢下去没碎，消耗一步能确定的层数+当前这一层
                print dp
                if dp[K][step] >= N:
                    return step
        return 0

    def superEggDrop2(self, K, N):
        dp = [0] * (K + 1)
        m = 0
        while dp[K] < N:
            m += 1
            for k in range(K, 0, -1):
                print(m, k)
                dp[k] = dp[k - 1] + dp[k] + 1
        return m



K = 2
N = 6
s = Solution()
res = s.superEggDrop2(K, N)
print(res)







