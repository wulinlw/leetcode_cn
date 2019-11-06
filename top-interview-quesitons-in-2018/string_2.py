#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/featured/card/top-interview-quesitons-in-2018/275/string/1137/
# 分割回文串
# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
# 返回 s 所有可能的分割方案。

# 示例:
# 输入: "aab"
# 输出:
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s: 
            return []

        res = [[]]
        for i, x in enumerate(s):
            tmp = []
            for r in res:
                tmp.append(r+[x])
                if len(r) >= 1 and r[-1] == x: 
                    tmp.append(r[:-1]+[r[-1]+x])
                    
                if len(r) >= 2 and r[-2] == x: 
                    tmp.append(r[:-2]+[r[-2]+r[-1]+x])
                    
            res = tmp
        return res

    def _partition(self, s, index, t, result):
        if index == len(s):
            result.append(t.copy())
            return 

        for i in range(index+1, len(s)+1):
            if s[index:i] == s[index:i][::-1]:
                t.append(s[index:i])
                self._partition(s, i, t, result)
                t.pop()  # 注意这里要弹出t的第一个值
        
    def partition_2(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = list()
        if not s:
            return result
        
        self._partition(s, 0, list(), result)
        return result


string = "aab"
s = Solution()
res = s.partition(string)
print(res)
















