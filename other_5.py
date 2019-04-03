#!/usr/bin/python
#coding:utf-8


# 有效的括号
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

# 有效字符串需满足：

# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。

# 示例 1:

# 输入: "()"
# 输出: true
# 示例 2:

# 输入: "()[]{}"
# 输出: true
# 示例 3:

# 输入: "(]"
# 输出: false
# 示例 4:

# 输入: "([)]"
# 输出: false
# 示例 5:

# 输入: "{[]}"
# 输出: true



class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 左括号翻到栈中，
        # 右括号与栈顶对比一样则弹出，
        # 最后栈空了就是完全匹配
        a = {')':'(', ']':'[', '}':'{'}
        l = [None]
        for i in s:
            if i in a and a[i] == l[-1]:
                l.pop()
            else:
                l.append(i)
        return len(l)==1


n="{[]}"
s = Solution()
re = s.isValid(n)
print("deep:",re)