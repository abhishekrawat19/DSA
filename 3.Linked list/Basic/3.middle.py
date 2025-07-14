class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head):
        curr = head
        l = 0
        while curr:
            curr = curr.next
            l += 1
        curr = head
        for i in range(l // 2):
            curr = curr.next
        return curr

# Manually create linked list like TreeNode style
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Test
sol = Solution()
mid = sol.middleNode(head)
print(mid.val)
