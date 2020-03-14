#
# @lc app=leetcode.cn id=725 lang=python3
#
# [725] 分隔链表
#
# https://leetcode-cn.com/problems/split-linked-list-in-parts/description/
#
# algorithms
# Medium (53.18%)
# Likes:    46
# Dislikes: 0
# Total Accepted:    6.6K
# Total Submissions: 12.4K
# Testcase Example:  '[1,2,3,4]\n5'
#
# 给定一个头结点为 root 的链表, 编写一个函数以将链表分隔为 k 个连续的部分。
# 
# 每部分的长度应该尽可能的相等: 任意两部分的长度差距不能超过 1，也就是说可能有些部分为 null。
# 
# 这k个部分应该按照在链表中出现的顺序进行输出，并且排在前面的部分的长度应该大于或等于后面的长度。
# 
# 返回一个符合上述规则的链表的列表。
# 
# 举例： 1->2->3->4, k = 5 // 5 结果 [ [1], [2], [3], [4], null ]
# 
# 示例 1：
# 
# 
# 输入: 
# root = [1, 2, 3], k = 5
# 输出: [[1],[2],[3],[],[]]
# 解释:
# 输入输出各部分都应该是链表，而不是数组。
# 例如, 输入的结点 root 的 val= 1, root.next.val = 2, \root.next.next.val = 3, 且
# root.next.next.next = null。
# 第一个输出 output[0] 是 output[0].val = 1, output[0].next = null。
# 最后一个元素 output[4] 为 null, 它代表了最后一个部分为空链表。
# 
# 
# 示例 2：
# 
# 
# 输入: 
# root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
# 输出: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
# 解释:
# 输入被分成了几个连续的部分，并且每部分的长度相差不超过1.前面部分的长度大于等于后面部分的长度。
# 
# 
# 
# 
# 提示:
# 
# 
# root 的长度范围： [0, 1000].
# 输入的每个节点的大小范围：[0, 999].
# k 的取值范围： [1, 50].
# 
# 
# 
# 
#
from typing import List
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def initlinklist(self, nums):
        head = ListNode(nums[0])
        re = head
        for i in nums[1:]:
            re.next = ListNode(i)
            re = re.next
        return head
    
    def printlinklist(self, head):
        re = []
        while head:
            re.append(head.val)
            head = head.next
        print(re)

    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        cur = root
        N = 0
        while cur:
            N += 1
            cur = cur.next
        width, remainder = divmod(N, k) #多少段， 剩余的

        # 知道有多少段，以及剩余的
        # 那切分的时候，每一段里加一个剩余的，直到分完
        # 这样前n段中，每段都多一个
        ans = []
        cur = root
        for _ in range(k):
            head = cur                  #记录头部
            remainder_surplus = 1 if remainder>0 else 0
            step = width + remainder_surplus -1
            for _ in range(step):
                if cur:                 #每一步都要判断，以免不够长度报错
                    cur = cur.next
            if cur:
                # cur.next, cur = None, cur.next
                tmp =  cur.next
                cur.next= None
                cur = tmp
            ans.append(head)
            remainder -= 1
        return ans

# @lc code=end

# nums = [1,2,3]
# k = 5
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3
o = Solution()
head = o.initlinklist(nums)
# o.printlinklist(head1)

h = o.splitListToParts(head, k)
print(h)
# o.printlinklist(h)
for i in h:
    o.printlinklist(i)
