# Reverse a singly linked list

# Node class to create linked list nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def reverse(self, head):
        curr = head      # Pointer to current node
        prev = None      # Will become the new head at the end
        nxt = None       # To store next node temporarily

        while curr != None:
            nxt = curr.next        # Store next node
            curr.next = prev       # Reverse the link
            prev = curr            # Move prev to current
            curr = nxt             # Move to next node (stored earlier)

        # At the end, prev will be the new head
        # head is prev
        return prev

# Create linked list manually: 1 -> 2 -> 3 -> 4 -> 5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Reverse the list
sol = Solution()
reversed_head = sol.reverse(head)

# Print reversed list
curr = reversed_head
while curr:
    print(curr.data, end=" -> ")
    curr = curr.next
print("None")
