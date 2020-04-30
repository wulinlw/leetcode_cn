# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题16.18.模式匹配
# 
# https://leetcode-cn.com/problems/pattern-matching-lcci/
# 
# 你有两个字符串，即pattern和value。 pattern字符串由字母"a"和"b"组成，用于描述字符串中的模式。例如，字符串"catcatgocatgo"匹配模式"aabab"（其中"cat"是"a"，"go"是"b"），该字符串也匹配像"a"、"ab"和"b"这样的模式。但需注意"a"和"b"不能同时表示相同的字符串。编写一个方法判断value字符串是否匹配pattern字符串。
# 示例 1：
# 输入： pattern = "abba", value = "dogcatcatdog"
# 输出： true
# 
# 示例 2：
# 输入： pattern = "abba", value = "dogcatcatfish"
# 输出： false
# 
# 示例 3：
# 输入： pattern = "aaaa", value = "dogcatcatdog"
# 输出： false
# 
# 示例 4：
# 输入： pattern = "abba", value = "dogdogdogdog"
# 输出： true
# 解释： "a"="dogdog",b=""，反之也符合规则
# 
# 提示：
# 
# 0 
# 0 
# 你可以假设pattern只包含字母"a"和"b"，value仅包含小写字母。
# 
# 
# 
# Medium 23.9%
# Testcase Example: "abba"
# "dogcatcatdog"
# 
# 提示:
# 从蛮力解法开始。你能试一下a和b的所有可能性吗?
# 观察其中一个子字符串，a或b都可以，必须从字符串的开头开始。这减少了可能性的种类。
# 不要忘记处理pattern中的第一个字符是b的可能性。
# 谨慎地选择分析时间复杂度的方式。如果遍历O(n2)个子字符串，每个子字符串都进行O(n)次的字符串比较，那么总体运行时间为O(n3)。
# 假设你确定了一个模式中“a”部分的值。b有多少种可能性?
# 由于a的值决定b的值（反之亦然），并且a或b必须出现于值的起始处，所以你应该只有O(n)种可能来分解模式串。
# 你应该能够有一个O(n2)的算法。
# 
# 
import collections
class Solution:
    # 简单说就是统计a和b的数量，比如统计到3个a和2个b。
    # 然后就是解方程：3 * str_a.length() + 2 * str_b.length() = value.length()
    # 其中：str_a是指代表a的字符串，str_b是指代表b的字符串，value是指patternMatching(String pattern, String value)方法的第2个参数。
    # 至于怎么解呢？穷举就完事了。
    # 需要注意的是，str_a或str_b可以为空字符串""，同时题目要求：str_a不能与str_b相同。
    def patternMatching(self, pattern: str, value: str) -> bool:
        dic = collections.Counter(pattern)
        n_a = dic.get('a',0)
        n_b = dic.get('b',0)
        if n_a == 0 and n_b==0:
            return not value 
        if n_a == 0:
            return (len(value)%n_b==0) and n_b*value[:len(value)//n_b] == value
        if n_b == 0:
            return (len(value)%n_a==0) and n_a*value[:len(value)//n_a] == value

        candidate = []
        m = len(value)//n_a
        for i in range(0, m+1):
            if (len(value)-i*n_a)%n_b == 0:
                candidate.append([i, (len(value)-i*n_a)//n_b])
        
        for i,j in candidate:
            if self.check(pattern, value, i, j):
                return True
        return False

    def check(self, pattern, value, i, j):
        set1 = set()
        set2 = set()
        for c in pattern:
            if c == 'a':
                if set1 and value[:i] not in set1:
                    return False
                set1.add(value[:i])
                value = value[i:]
            elif c == 'b':
                if set2 and value[:j] not in set2:
                    return False
                set2.add(value[:j])
                value = value[j:]
        if set1 == set2:        ## a,b对应模式相同返回False
            return False
        return True



pattern = "abba"
value = "dogcatcatdog"
o = Solution()
print(o.patternMatching(pattern, value))
