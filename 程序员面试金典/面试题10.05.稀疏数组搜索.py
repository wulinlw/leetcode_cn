# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题10.05.稀疏数组搜索
# 
# https://leetcode-cn.com/problems/sparse-array-search-lcci/
# 
# 稀疏数组搜索。有个排好序的字符串数组，其中散布着一些空字符串，编写一种方法，找出给定字符串的位置。
# 示例1:
# 
#  输入: words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ta"
#  输出：-1
#  说明: 不存在返回-1。
# 
# 
# 示例2:
# 
#  输入：words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ball"
#  输出：4
# 
# 
# 提示:
# 
# 
# 	words的长度在[1, 1000000]之间
# 
# 
# 
# Easy 59.4%
# Testcase Example: ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
# "ta"
# 
# 提示:
# 尝试修改二分查找来处理这个问题。
# 
# 
from typing import List
class Solution:
    def findString(self, words: List[str], s: str) -> int:
        l,r = 0,len(words)-1
        while l<=r:
            mid = (l+r)>>1
            midTmp = mid
            while words[mid] == '' and mid<r:
                mid += 1
            if words[mid] == '':
                r = midTmp - 1
                continue
            if words[mid] == s:
                return mid
            elif s < words[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return -1



words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""]
s = "ta"
o = Solution()
print(o.findString(words, s))