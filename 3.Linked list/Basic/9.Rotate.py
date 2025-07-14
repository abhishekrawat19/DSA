# Rotate a linked list

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def rotate(sself, head, k):
        last = head
        l = 0

        # Find last node and length
        while last.next != None:
            last = last.next
            l += 1

        l += 1
        k = k % l

        if k == 0:
            return head

        curr = head

        # Move to the (l - k - 1)th node
        for i in range(l - k - 1):
            curr = curr.next

        last.next = head         # Connect end to head
        head = curr.next         # New head after rotation
        curr.next = None         # Break the list

        return head

# Helper to create and print linked list

def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Create list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Rotate by k = 2
sol = Solution()
head = sol.rotate(head, 2)

# Print result
print_list(head)
