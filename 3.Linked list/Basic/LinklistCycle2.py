# Detect start node of cycle in linked list

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def linklistcycletwo(self, head):
        fast = head
        slow = head
        hascycle = False  # ✅ must initialize this

        # Step 1: Detect cycle
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                hascycle = True
                break

        if not hascycle:
            return None

        # Step 2: Find cycle length
        l = 0
        while slow.next != fast:
            slow = slow.next
            l += 1
        l += 1

        # Step 3: Move fast ahead by cycle length
        slow = head
        fast = head
        for i in range(l):
            fast = fast.next

        # Step 4: Move both at same speed
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow

# ----------------- Test Code -----------------

# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
#                               ^         |
#                               |_________|

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Create cycle: 5 -> 3
head.next.next.next.next.next = head.next.next  # Cycle starts at node with value 3

sol = Solution()
start_node = sol.linklistcycletwo(head)

if start_node:
    print("Cycle starts at node with value:", start_node.val)
else:
    print("No cycle detected.")
