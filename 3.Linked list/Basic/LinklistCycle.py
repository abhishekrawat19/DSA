# Detect if linked list contains a cycle

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def cycle(self, head):
        fast = head
        slow = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

# ---------- Test Case 1: With Cycle ----------

# Create nodes: 1 -> 2 -> 3 -> 4 -> 5
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)

# Create cycle: 5 -> 3
head1.next.next.next.next.next = head1.next.next  # Node with value 3

sol = Solution()
print("Cycle exists (Test 1)?", sol.cycle(head1))  # Output: True

# ---------- Test Case 2: Without Cycle ----------

head2 = ListNode(10)
head2.next = ListNode(20)
head2.next.next = ListNode(30)

print("Cycle exists (Test 2)?", sol.cycle(head2))  # Output: False
