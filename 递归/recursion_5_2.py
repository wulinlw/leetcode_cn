#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/orignial/card/recursion-i/260/conclusion/1231/
# 第K个语法符号
# 在第一行我们写上一个 0。接下来的每一行，将前一行中的0替换为01，1替换为10。
# 给定行数 N 和序数 K，返回第 N 行中第 K个字符。（K从1开始）

# 例子:
# 输入: N = 1, K = 1
# 输出: 0

# 输入: N = 2, K = 1
# 输出: 0

# 输入: N = 2, K = 2
# 输出: 1

# 输入: N = 4, K = 5
# 输出: 1

# 解释:
# 第一行: 0
# 第二行: 01
# 第三行: 0110
# 第四行: 01101001
# 注意：
# N 的范围 [1, 30].
# K 的范围 [1, 2^(N-1)].
class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        # 第 K 个数字是上一行第 (K+1) / 2 个数字生成的。如果上一行的数字为 0，被生成的数字为 1 - (K%2)，如果上一行的数字为 1，被生成的数字为 K%2
        # 链接：https://leetcode-cn.com/problems/k-th-symbol-in-grammar/solution/di-kge-yu-fa-fu-hao-by-leetcode/
        if N == 1: return 0
        return (1 - K%2) ^ self.kthGrammar(N-1, (K+1)/2)

    def kthGrammar2(self, N, K):
        lastrow = '0'
        while len(lastrow) < N:
            lastrow = "".join('01' if x == '0' else '10'
                              for x in lastrow)
        # print(lastrow[K-1])
        return int(lastrow[K-1])








N = 4
K = 5
S = Solution()
deep = S.kthGrammar(N,K)
print("deep:",deep)
deep = S.kthGrammar2(N,K)
print("deep:",deep)