#!/usr/bin/python
#coding:utf-8

# 942. 增减字符串匹配
# 给定只含 "I"（增大）或 "D"（减小）的字符串 S ，令 N = S.length。
# 返回 [0, 1, ..., N] 的任意排列 A 使得对于所有 i = 0, ..., N-1，都有：
# 如果 S[i] == "I"，那么 A[i] < A[i+1]
# 如果 S[i] == "D"，那么 A[i] > A[i+1]

# 示例 1：
# 输出："IDID"
# 输出：[0,4,1,3,2]

# 示例 2：
# 输出："III"
# 输出：[0,1,2,3]

# 示例 3：
# 输出："DDI"
# 输出：[3,2,0,1]

# 提示：
# 1 <= S.length <= 1000
# S 只包含字符 "I" 或 "D"。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/di-string-match
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution(object):
    def diStringMatch(self, s):
        """
        :type S: str
        :rtype: List[int]
        """
        n = len(s)
        if n==0: return[]
        re = []
        l = 0
        r = n
        for i in range(len(s)):
            if s[i] == "I":
                re.append(l)
                l+=1
            else:
                re.append(r)
                r-=1
        last = l if s[i] == "I" else r
        re.append(last)
        return re
    

    #玩耍的hhhh
    def blackMagic(self, s):
        import random,time
        start = time.time()
        def check(arr):
            if len(arr) != len(set(arr)):
                return False
            for i in range(len(s)):
                if s[i] == "I" :
                    if arr[i] > arr[i+1]:
                        return False
                else:
                    if arr[i] < arr[i+1]:
                        return False
            return True
        
        n = len(s)
        while True:
            re = []
            for i in range(n+1):
                re.append(i)
            random.shuffle(re)
            if check(re):
                useTime = time.time() - start
                print("Time used:%.2f"%useTime)
                return re

s = "IDID"
s = "III"
s = "DDI"
s = "IDIDIDIDIIDIDIIDIDID"
obj = Solution()
n = obj.diStringMatch(s)
print('return', n) 
# n = obj.blackMagic(s)
# print('return', n) 