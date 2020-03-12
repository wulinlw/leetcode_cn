#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#
# https://leetcode-cn.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (56.43%)
# Likes:    403
# Dislikes: 0
# Total Accepted:    42.2K
# Total Submissions: 74.3K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
# 
# k 是一个正整数，它的值小于或等于链表的长度。
# 
# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
# 
# 
# 
# 示例：
# 
# 给你这个链表：1->2->3->4->5
# 
# 当 k = 2 时，应当返回: 2->1->4->3->5
# 
# 当 k = 3 时，应当返回: 3->2->1->4->5
# 
# 
# 
# 说明：
# 
# 
# 你的算法只能使用常数的额外空间。
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
# 
# 
#

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

    def reverseKGroup1(self, head: ListNode, k: int) -> ListNode:
        cur = head
        count = 0
        while cur and count!= k:
            cur = cur.next
            count += 1
        if count == k:
            cur = self.reverseKGroup(cur, k)
            while count:
                tmp = head.next
                head.next = cur
                cur = head
                head = tmp
                count -= 1
            head = cur   
        return head

    #普通翻转链表
    #链表头 a，翻转 a 到 b之间
    def reverse(self, a, b):
        pre = None
        cur = net = a
        while cur != b:     #到b结束，  普通翻转是到结尾None
            net = cur.next 
            cur.next = pre 
            pre = cur 
            cur = net
        return pre          #返回头
        
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:return None
        a = b = head
        for _ in range(k):                  #线走k个，然后翻转
            if not b:return head            #不足 k 个，不需要反转，base case
            b = b.next
        new = self.reverse(a, b)            #反转前 k 个元素
        a.next = self.reverseKGroup(b, k)   #a本来是头，翻转后变成第一段的尾，a.next 接上第二批要反转的
        return new






# @lc code=end

nums = [1,2,3,4,5]
o = Solution()
head = o.initlinklist(nums)
# o.printlinklist(head)

h = o.reverseKGroup(head, 2)
o.printlinklist(h)