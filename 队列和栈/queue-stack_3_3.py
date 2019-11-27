#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/learn/card/queue-stack/218/stack-last-in-first-out-data-structure/879/
# 每日温度
# 根据每日 气温 列表，请重新生成一个列表，对应位置的输入是你需要再等待多久温度才会升高超过该日的天数。如果之后都不会升高，请在该位置用 0 来代替。
# 例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。
# 提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。
 
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        '''
        * 根据题意，从最后一天推到第一天，这样会简单很多。因为最后一天显然不会再有升高的可能，结果直接为0。
        * 再看倒数第二天的温度，如果比倒数第一天低，那么答案显然为1，如果比倒数第一天高，又因为倒数第一天
        * 对应的结果为0，即表示之后不会再升高，所以倒数第二天的结果也应该为0。
        * 自此我们容易观察出规律，要求出第i天对应的结果，只需要知道第i+1天对应的结果就可以：
        * - 若T[i] < T[i+1]，那么res[i]=1；
        * - 若T[i] > T[i+1]
        *   - res[i+1]=0，那么res[i]=0;
        *   - res[i+1]!=0，那就比较T[i]和T[i+1+res[i+1]]（即将第i天的温度与比第i+1天大的那天的温度进行比较）
        '''
        # 维护递减栈，后入栈的元素总比栈顶元素小。
        # 比对当前元素与栈顶元素的大小
        # 若当前元素 < 栈顶元素：入栈
        # 若当前元素 > 栈顶元素：弹出栈顶元素，记录两者下标差值即为所求天数
        # 这里用栈记录的是 T 的下标。
        ans = [0] * len(T)
        stack = [] #温度栈，倒序遍历T，栈顶的是最小的温度
        for i in range(len(T) - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop() #前一天的温度比最近的高温还大，弹出栈顶，因为前面的温度只需要已当前温度对比
            if stack:
                ans[i] = stack[-1] - i #i是T数组的索引，stack[-1]是栈顶，就是离i最近的升温，stack[-1] - i就是下一个升温的距离
            stack.append(i)
        return ans


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
ss = Solution()
re = ss.dailyTemperatures(temperatures)
print(re)






