# 面试题01.01.判定字符是否唯一
# 
# https://leetcode-cn.com/problems/is-unique-lcci/
# 
# 实现一个算法，确定一个字符串 s 的所有字符是否全都不同。
# 示例 1：
# 
# 输入: s = leetcode
# 输出: false 
# 
# 
# 示例 2：
# 
# 输入: s = abc
# 输出: true
# 
# 
# 限制：
# 
# 	0 
# 	如果你不使用额外的数据结构，会很加分。
# 
#     
# 
# Easy 72.3%
# Testcase Example: "leetcode"
# 
# 提示:
# 试试散列表
# 位向量有用吗？
# 你能用O(NlogN)的时间复杂度解决它吗？这样的解法会是什么样呢？
# 
# 

class Solution:
    def isUnique(self, astr: str) -> bool:
        map = {}
        for i in range(len(astr)):
            if astr[i] in map:
                return False
            map[astr[i]] = 1
        return True

astr = "leetcode"
o = Solution()
print(o.isUnique(astr))