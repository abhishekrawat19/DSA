class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next

# Manually create linked list: 4 -> 5 -> 1 -> 9
head = ListNode(4)
head.next = ListNode(5)
head.next.next = ListNode(1)
head.next.next.next = ListNode(9)

# Delete node with value 5
node_to_delete = head.next  # Node with value 5

sol = Solution()
sol.deleteNode(node_to_delete)

# Print updated linked list: should be 4 -> 1 -> 9
curr = head
while curr:
    print(curr.val, end=" -> ")
    curr = curr.next
print("None")
