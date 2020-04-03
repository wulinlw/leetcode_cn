#
# @lc app=leetcode.cn id=375 lang=python3
#
# [375] 猜数字大小 II
#
# https://leetcode-cn.com/problems/guess-number-higher-or-lower-ii/description/
#
# algorithms
# Medium (37.10%)
# Likes:    95
# Dislikes: 0
# Total Accepted:    4.6K
# Total Submissions: 12.3K
# Testcase Example:  '1'
#
# 我们正在玩一个猜数游戏，游戏规则如下：
# 
# 我从 1 到 n 之间选择一个数字，你来猜我选了哪个数字。
# 
# 每次你猜错了，我都会告诉你，我选的数字比你的大了或者小了。
# 
# 然而，当你猜了数字 x 并且猜错了的时候，你需要支付金额为 x 的现金。直到你猜到我选的数字，你才算赢得了这个游戏。
# 
# 示例:
# 
# n = 10, 我选择了8.
# 
# 第一轮: 你猜我选择的数字是5，我会告诉你，我的数字更大一些，然后你需要支付5块。
# 第二轮: 你猜是7，我告诉你，我的数字更大一些，你支付7块。
# 第三轮: 你猜是9，我告诉你，我的数字更小一些，你支付9块。
# 
# 游戏结束。8 就是我选的数字。
# 
# 你最终要支付 5 + 7 + 9 = 21 块钱。
# 
# 
# 给定 n ≥ 1，计算你至少需要拥有多少现金才能确保你能赢得这个游戏。
# 
#
# import functools
# @lc code=start
class Solution:
    # https://leetcode-cn.com/problems/guess-number-higher-or-lower-ii/solution/chao-jian-ji-python-fen-zhi-by-amir-6/
    # 分治法，自顶向下
    # 当区间长度为 1 时（l == r），费用是 0。
    # 当区间长度为 2 时（r - l == 1），费用是 l（较小的那个数）。
    # 当区间长度为 3 时（r - l == 2），费用是 l + 1（中间那个数）。
    # 区间长度更长，我们就直接分成两个区间做，取两个区间里最大的一个就成了。
    def getMoneyAmount2(self, n: int) -> int:
        import functools
        @functools.lru_cache(None)
        def dp(l, r):
            if l==r:return 0
            if r-1==1:return 1
            if r-l==2:return l+1
            ans = sum(range(r))
            for x in range(l+r>>1, r):                                  #按x分为2边，取大的（至少需要这么多） ，结果+x
                ans = min(max(dp(l, x-1), dp(x+1, r)) + x, ans)         #然后取min
            return ans 
        return dp(1,n)

    # 自底向上
    # dp[i][j]表示从[i,j]中猜出正确数字所需要的最少花费金额.(dp[i][j] = 0)
    # 假设在范围[i,j]中选择x, 则选择x的最少花费金额为: max(dp[i][x-1], dp[x+1][j]) + x
    # 用max的原因是我们要计算最坏反馈情况下的最少花费金额(选了x之后, 正确数字落在花费更高的那侧) 
    # 初始化为(n+2)*(n+2)数组的原因: 处理边界情况更加容易, 例如对于求解dp[1][n]时x如果等于1, 需要考虑dp[0][1](0不可能出现, dp[0][n]为0)
    # 而当x等于n时, 需要考虑dp[n+1][n+1](n+1也不可能出现, dp[n+1][n+1]为0)
    # 如何写出相应的代码更新dp矩阵, 递推式dp[i][j] = max(max(dp[i][x-1], dp[x+1][j]) + x), x~[i:j], 可以画出矩阵图协助理解, 可以发现
    # dp[i][x-1]始终在dp[i][j]的左部, dp[x+1][j]始终在dp[i][j]的下部, 所以更新dp矩阵时i的次序应当遵循bottom到top的规则, j则相反, 由于
    # i肯定小于等于j, 所以我们只需要遍历更新矩阵的一半即可(下半矩阵)
    def getMoneyAmount(self, n: int) -> int: 
        dp = [[0 for i in range(n+2)] for _ in range(n+2)]
        for i in range(n, 0, -1):                                               #从下到上
            for j in range(i, n+1):                                             #从左到右
                # print(i,j)
                if i==j:continue                                                #对角线都是0，dp[1][1],1到1无法分割
                dp[i][j] = float('inf')                                         #后面要取最小值，这里先放一个最大的数
                # print('i','j','x','l','d')
                for x in range(i, j+1):
                    # print(i,j,x,dp[i][x-1], dp[x+1][j])
                    dp[i][j] = min(dp[i][j], max(dp[i][x-1], dp[x+1][j]) + x)
        # for i in dp:
        #     print(i)
        return dp[1][n]


    # def getMoneyAmount3(self, n: int) -> int: 
    #     dp = [[0] * n for _ in range(n+1)]
    #     for i in reversed(range(n)):
    #         for j in range(i+1, n):
    #             dp[i][j] = min(k+1 + max(dp[i][k-1], dp[k+1][j]) \
    #                             for k in range(i, j+1))
    #             #这个min是在for出所有结果后，选择出最小的一个
    #     return dp[0][n-1]


    # def getMoneyAmount4(self, n: int) -> int:
    #     if n==0:return 0
    #     # dp = [[float('inf') for i in range(n+1)] for i in range(n+1)]
    #     dp = [[99 for i in range(n+1)] for i in range(n+1)]
    #     # print(dp)
    #     for i in range(n+1):
    #         dp[i][i] = 0
    #     for j in range(2, n+1):
    #         for i in range(j-1, 0, -1):
    #             for x in range(i+1, j):
    #                 dp[i][j] = min(x + max(dp[i][x-1], dp[x+1][j]), dp[i][j])#max(左 下)
    #             dp[i][j] = min(dp[i][j], i+dp[i+1][j])
    #             dp[i][j] = min(dp[i][j], j+dp[i][j-1])
    #     for i in dp:
    #         print(i)
    #     return dp[1][n]


    

# @lc code=end

n = 5
pick = 6
o = Solution()
print(o.getMoneyAmount(n))