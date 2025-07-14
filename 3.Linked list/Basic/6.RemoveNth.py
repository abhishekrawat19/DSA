# Remove nth node from the end of linked list

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def removenode(self, head, n):
        curr = head
        l = 0

        while curr != None:
            curr = curr.next
            l += 1

        curr = head
        if n == l:
            return head.next

        for i in range(l - n - 1):
            curr = curr.next

        curr.next = curr.next.next
        return head

    def pointer(self, head, n):
        p1 = head
        p2 = head

        for i in range(n):
            p2 = p2.next

        if p2 == None:
            return head.next

        while p2.next != None:
            p1 = p1.next
            p2 = p2.next

        p1.next = p1.next.next
        return head

# Manually create linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

sol = Solution()

# Remove 2nd node from end using removenode()
head = sol.removenode(head, 2)

# Print final linked list
curr = head
while curr:
    print(curr.val, end=" -> ")
    curr = curr.next
print("None")
