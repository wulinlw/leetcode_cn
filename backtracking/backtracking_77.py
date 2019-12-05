#!/usr/bin/python
#coding:utf-8

# 77. 组合
# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

# 示例:
# 输入: n = 4, k = 2
# 输出:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/combinations
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        output = []
        def backtrack(first = 1, curr = []):
            if len(curr) == k:  
                output.append(curr[:])
                return 
            for i in range(first, n + 1):
                curr.append(i)
                backtrack(i + 1, curr)
                curr.pop()
        
        backtrack()
        return output

    def combine2(self, n, k):
        out = []
        def backtrack(i, k, tmp):
            if k==0:
                out.append(tmp)
                return 
            for j in range(i, n+1):
                backtrack(j+1, k-1, tmp+[j])
        backtrack(1,k,[])
        return out



n=4
k=2
obj = Solution()
r = obj.combine(n,k)
print('return', r)
r = obj.combine2(n,k)
print('return', r)