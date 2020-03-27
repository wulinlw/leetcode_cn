#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#
# https://leetcode-cn.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (65.00%)
# Likes:    438
# Dislikes: 0
# Total Accepted:    36K
# Total Submissions: 55.2K
# Testcase Example:  '3'
#
# 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
# 
# 示例:
# 
# 输入: 3
# 输出: 5
# 解释:
# 给定 n = 3, 一共有 5 种不同结构的二叉搜索树:
# 
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
# 
#

# @lc code=start
class Solution:
    # 动态规划O(N^2)
    # 假设n个节点存在二叉排序树的个数是G(n)，令f(i)为以i为根的二叉搜索树的个数，则
    # G(n) = f(1) + f(2) + f(3) + f(4) + ... + f(n)G(n)=f(1)+f(2)+f(3)+f(4)+...+f(n)
    # 当i为根节点时，其左子树节点个数为i-1个，右子树节点为n-i，则
    # f(i) = G(i-1)*G(n-i)f(i)=G(i−1)∗G(n−i)
    # 综合两个公式可以得到 卡特兰数 公式
    # G(n) = G(0)*G(n-1) + G(1)*(n-2)+...+ G(n-1)*G(0)
    # https://leetcode-cn.com/problems/unique-binary-search-trees/solution/bu-tong-de-er-cha-sou-suo-shu-by-leetcode/
    def numTrees2(self, n: int) -> int:
        G = [0]*(n+1)
        G[0], G[1] = 1, 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1] * G[i-j]
        return G[n]

    #卡特兰数 公式O(n)
    def numTrees(self, n):
        C = 1
        for i in range(0, n):
            C = C * 2*(2*i+1)/(i+2)
        return int(C)


# @lc code=end


n = 3
o = Solution()
print(o.numTrees(n))