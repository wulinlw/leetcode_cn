#
# @lc app=leetcode.cn id=1111 lang=python3
#
# [1111] 有效括号的嵌套深度
#
# https://leetcode-cn.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/description/
#
# algorithms
# Medium (66.71%)
# Likes:    46
# Dislikes: 0
# Total Accepted:    4.6K
# Total Submissions: 6.2K
# Testcase Example:  '"(()())"'
#
# 有效括号字符串 仅由 "(" 和 ")" 构成，并符合下述几个条件之一：
# 
# 
# 空字符串
# 连接，可以记作 AB（A 与 B 连接），其中 A 和 B 都是有效括号字符串
# 嵌套，可以记作 (A)，其中 A 是有效括号字符串
# 
# 
# 类似地，我们可以定义任意有效括号字符串 s 的 嵌套深度 depth(S)：
# 
# 
# s 为空时，depth("") = 0
# s 为 A 与 B 连接时，depth(A + B) = max(depth(A), depth(B))，其中 A 和 B 都是有效括号字符串
# s 为嵌套情况，depth("(" + A + ")") = 1 + depth(A)，其中 A 是有效括号字符串
# 
# 
# 例如：""，"()()"，和 "()(()())" 都是有效括号字符串，嵌套深度分别为 0，1，2，而 ")(" 和 "(()"
# 都不是有效括号字符串。
# 
# 
# 
# 给你一个有效括号字符串 seq，将其分成两个不相交的子序列 A 和 B，且 A 和 B 满足有效括号字符串的定义（注意：A.length +
# B.length = seq.length）。
# 
# 现在，你需要从中选出 任意 一组有效括号字符串 A 和 B，使 max(depth(A), depth(B)) 的可能取值最小。
# 
# 返回长度为 seq.length 答案数组 answer ，选择 A 还是 B 的编码规则是：如果 seq[i] 是 A 的一部分，那么
# answer[i] = 0。否则，answer[i] = 1。即便有多个满足要求的答案存在，你也只需返回 一个。
# 
# 
# 
# 示例 1：
# 
# 输入：seq = "(()())"
# 输出：[0,1,1,1,1,0]
# 
# 
# 示例 2：
# 
# 输入：seq = "()(())()"
# 输出：[0,0,0,1,1,0,1,1]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= text.size <= 10000
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    # 一句话概括就是，
    # 给你一个合法的括号序列，你需要将其拆分成两个合法的子序列（不连续），使得两个子序列的括号嵌套深度较大者尽量的小。
    
    # 解法就是把"("平均分到A，B 2个子序列中
    # 维护一个栈 s，从左至右遍历括号字符串中的每一个字符：
    # 如果当前字符是 (，就把 ( 压入栈中，此时这个 ( 的嵌套深度为栈的高度；
    # 如果当前字符是 )，此时这个 ) 的嵌套深度为栈的高度，随后再从栈中弹出一个 (。
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        re = []
        for i in range(len(seq)):                  #i既是栈高度，
            if seq[i] == '(':
                re.append(i % 2)                   
            else:
                re.append((i-1) % 2)               #碰到")"时，从栈中弹出一个“(”
            # 上面的代码也可以简写成
            # ans.append((i & 1) ^ (ch == '('))
        return re




# @lc code=end

seq = "(()())"
# [0,1,1,1,1,0]

# seq = "()(())()"
# [0,0,0,1,1,0,1,1]
o = Solution()
print(o.maxDepthAfterSplit(seq))