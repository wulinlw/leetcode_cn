# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题08.14.布尔运算
# 
# https://leetcode-cn.com/problems/boolean-evaluation-lcci/
# 
# 给定一个布尔表达式和一个期望的布尔结果 result，布尔表达式由 0 (false)、1 (true)、&amp; (AND)、 | (OR) 和 ^ (XOR) 符号组成。实现一个函数，算出有几种可使该表达式得出 result 值的括号方法。
# 示例 1:
# 
# 输入: s = "1^0|0|1", result = 0
# 
# 输出: 2
# 解释:&nbsp;两种可能的括号方法是
# 1^(0|(0|1))
# 1^((0|0)|1)
# 
# 
# 示例 2:
# 
# 输入: s = "0&amp;0&amp;0&amp;1^1|0", result = 1
# 
# 输出: 10
# 
# 提示：
# 
# 
# 	运算符的数量不超过 19 个
# 
# 
# 
# Medium 46.1%
# Testcase Example: "1"
# 0
# 
# 提示:
# 我们能试试所有的可能性吗？这看起来像什么？
# 我们可以把每种可能性都看作是每个可以放置括号的地方。这意味着围绕每个操作符，使表达式在运算符上被分割。基线条件是什么？
# 基本情况是我们有一个值，1或0。
# 如果你的代码看起来很长，有很多的if（基于每个可能的操作符、“目标”布尔结果和左/右侧），考虑不同部分之间的关系。尽量简化代码。它不需要大量复杂的if语句。例如，考虑OR与AND的表达式。两者可能都需要知道计算结果为true的数量。看看你可以重用哪些代码。
# 着眼于你的递归上。有重复调用吗？可以将结果存起来吗？
# 
# 

class Solution:
    # https://leetcode-cn.com/problems/boolean-evaluation-lcci/solution/python3-ji-yi-hua-sou-suo-by-yesohh-2/
    def countEval(self, s: str, result: int) -> int:
        """
        {
            符号: {
                需要计算出的结果: {
                    [(左子式需要计算的结果，右子式需要计算的结果)]
                }
            }
            
        }
        """
        self.ops = {
            '&': {
                True: [(True, True)],
                False: [(True, False), (False, True), (False, False)]
            },
            '|': {
                True: [(True, False), (False, True), (True, True)],
                False: [(False, False)]
            },
            '^': {
                True: [(True, False), (False, True)],
                False: [(True, True), (False, False)]
            }
        }
        return self.dfs(s, result, {})
        
    def dfs(self, expression, result, memo):
        # 查询备忘录，有结果则直接返回
        if (expression, result) in memo:
            return memo[(expression, result)]
        
        # 边界情况
        if len(expression) == 1:
            val = int(expression)
            return int(bool(val) == result)
        
        # 递归计算左右子式的结果
        total = 0
        for i in range(len(expression)):
            if expression[i] in self.ops:
                for lr, rr in self.ops[expression[i]][result]:
                    total += self.dfs(expression[:i], lr, memo)*self.dfs(expression[i+1:], rr, memo)
        memo[(expression, result)] = total
        return total

s = "1^0|0|1"
result = 0
o = Solution()
print(o.countEval(s, result))