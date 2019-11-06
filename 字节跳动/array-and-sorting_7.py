#!/usr/bin/python
#coding:utf-8
import math

# https://leetcode-cn.com/explore/interview/card/bytedance/243/array-and-sorting/1021/
# 第k个排列
# 给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

# 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 给定 n 和 k，返回第 k 个排列。

# 说明：
# 给定 n 的范围是 [1, 9]。
# 给定 k 的范围是[1,  n!]。
# 示例 1:

# 输入: n = 3, k = 3
# 输出: "213"
# 示例 2:

# 输入: n = 4, k = 9
# 输出: "2314"

# https://cloud.tencent.com/developer/article/1407034
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        curr = []
        self.result = ''
        for i in range(1, n+1):
            curr.append(i) 
        self.getPermutationHelper(n, k, curr)
        return self.result

    def getPermutationHelper(self, index, rest, curr):
        # print index, rest, '结果str：', curr
        if index == 0:
            return 
        for i in range(index-1, -1, -1):
            temp = math.factorial(index-1)
            # print temp, i, rest - (temp * i + 1)
            if rest - (temp * i + 1) >= 0:
                self.result += str(curr[i])
                curr.pop(i)
                # print(curr)
                self.getPermutationHelper(index-1, rest - (temp * i), curr)
                break
    
    # https://cloud.tencent.com/developer/article/1335755
    # n 个数字有 n！种全排列，每种数字开头的全排列有 (n - 1)!种。 
    # 所以用 k / (n - 1)! 就可以得到第 k 个全排列是以第几个数字开头的。 
    # 用 k % (n - 1)! 就可以得到第 k 个全排列是某个数字开头的全排列中的第几个。
    def getPermutation2(self, n, k):
        res = ''
        k -= 1
        fac = 1
        for i in range(1, n): fac *= i
        num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in reversed(range(n)):
            curr = num[k/fac]
            res += str(curr)
            num.remove(curr)
            if i !=0:
                k %= fac
                fac /= i
        return res


n = 3
k = 3
s = Solution()
n = s.getPermutation(n, k)
print(n)

