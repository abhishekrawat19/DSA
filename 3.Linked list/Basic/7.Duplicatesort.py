# Remove duplicate elements from sorted linked list

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def duplicatesorted(self, head):
        curr = head
        if head is None or head.next is None:
            return head

        while curr != None and curr.next != None:
            # duplicate value found 
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head  # ✅ return the updated list

# Manually create a sorted linked list: 1 -> 1 -> 2 -> 3 -> 3
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)

# Remove duplicates
sol = Solution()
new_head = sol.duplicatesorted(head)

# Print updated list
curr = new_head
while curr:
    print(curr.val, end=" -> ")
    curr = curr.next
print("None")
