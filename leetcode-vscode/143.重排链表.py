#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#
# https://leetcode-cn.com/problems/reorder-list/description/
#
# algorithms
# Medium (54.65%)
# Likes:    171
# Dislikes: 0
# Total Accepted:    18.3K
# Total Submissions: 33.3K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
# 
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
# 
# 示例 1:
# 
# 给定链表 1->2->3->4, 重新排列为 1->4->2->3.
# 
# 示例 2:
# 
# 给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
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
        
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next: return head
        fast = slow = head
        #找到中点
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        # 将后半条链转置
        new_chain_head = slow.next
        slow.next = None
        pre = None
        cur = new_chain_head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
            # pre 指向转置后的链表头
        # self.printlinklist(head)
        # self.printlinklist(pre)

        # 构建新链
        cur = head
        insert_cur = pre
        while insert_cur:
            tmp = insert_cur.next           #后段的next放到变量里
            insert_cur.next = cur.next      #后段第一个->前段第二个
            cur.next = insert_cur           #前段第一个->后段第一个
                                            #下面更新cur和insert_cur
            cur = insert_cur.next           #就是cur.next.next
            insert_cur = tmp
        return head
        # 构建过程
        # cur       1 2 3
        # inser_cur 5 4

        # 想要写成 1 5 2 3，就是要把 5 插到 2 3 前，
        # 1、要把 5 放到 1 后面，不能把他后面的 4 跟过去，所以打断insert_cur，并且在最后一行重置一下，并与下次循环
        # 2、cur的 2 3 放到 5 后面
        # 3、连接 1 和 5，这时候 cur 是 1 5 2 3 
        # 4、拼接完第一个后，需要移动cur到 2



# @lc code=end

nums = [1,2,3,4,5]
o = Solution()
head = o.initlinklist(nums)
# o.printlinklist(head)

h = o.reorderList(head)
o.printlinklist(h)