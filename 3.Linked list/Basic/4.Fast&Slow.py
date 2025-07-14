class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middlenode(self, head):
        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        return slow

# Manually create linked list like TreeNode style
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Use your function
sol = Solution()
mid = sol.middlenode(head)

# Print from middle node to end
while mid:
    print(mid.val, end=" -> ")
    mid = mid.next
print("None")
