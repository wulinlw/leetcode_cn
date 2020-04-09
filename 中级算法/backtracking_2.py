#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/49/backtracking/92/
# 生成括号
# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

# 例如，给出 n = 3，生成结果为：

# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]


# https://blog.csdn.net/weixin_41958153/article/details/80723622
# 思路：首先我们必须要明确的是，要生成的括号一定是先以左括号开头的，如果一开始不是左括号，生成的就不是我们想要的类型。
# 所以这道题我们为了遍历所有的加括号的情况，一定先生成左括号。
# 分析示例，假设我们有3个左括号，3个右括号。
# 比如说为了生成示例中的第一个，我们先添加尽可能多地添加左括号，然后在添加右括号。
# 第二个，我们在生成了2个左括号后，加一个右括号，再加左括号。
# 对比一下发现，与我们第一次连着添加三个左括号不同的是，第二次我们在添加了2个左括号后尝试着去添加右括号。
# 这就非常符合DFS的思想：先一条路一直从左走到黑（添加左括号），再回到上个路口的节点尝试右边的路（添加右括号），所以到目前思维就明确了。

# 这道题整体代码逻辑非常清晰，主函数+递归函数, DFS的left , right 分别表示左右括号的剩余数量，s表示目前制造的括号。
# 高含金量的逻辑出现在DFS函数中的else部分。首先我们都知道base条件是左括号和右括号的数量都为0时。
# 巧妙在于，我们的DFS一开始只会进入 if left > 0:里的函数，第一次函数递归完毕返回后，还是停留在left = 1 , s='(('的状况下，而且返回点在if left>0:下。
# 接着它会进入right>left里，进行一次递归后又会进入if left > 0：里的递归函数。
# 这就是DFS的魔力，它通过2个看起来平行的递归入口，通过代码顺序制造递归的先后，最终达到了深度优先搜索。


class Solution(object):
    # 如果左括号还有剩余，则可以放置左括号，如果右括号的剩余数大于左括号，则可以放置右括号。
    def generateParenthesis(self, n):
        def backtrack(l, r, tmp):
            if r>l:return 
            if l==0 and r==0:
                re.append(tmp)
                return
            if l>0: 
                backtrack(l-1, r, "("+tmp)
            if r>0:
                backtrack(l, r-1, ")"+tmp)    
        re = []
        backtrack(n, n, "")
        return re
        

digits = 3
s = Solution()
r = s.generateParenthesis(digits)
print(r)




