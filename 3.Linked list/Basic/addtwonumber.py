# Add two numbers represented as linked lists

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def addtwo(self, head1, head2):
        curr1 = head1
        curr2 = head2
        
        ans = Node(-1)
        c = 0
        curr3 = ans

        while curr1 != None or curr2 != None:
            total = c
            c = 0

            if curr1 != None:
                total += curr1.val
                curr1 = curr1.next
            if curr2 != None:
                total += curr2.val
                curr2 = curr2.next

            if total > 9:
                c = 1
                total -= 10

            newnode = Node(total)
            curr3.next = newnode
            curr3 = curr3.next

        if c > 0:
            newnode = Node(c)
            curr3.next = newnode

        return ans.next

# Helper to print linked list
def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Create first number: 342 (in reverse as 2 -> 4 -> 3)
head1 = Node(2)
head1.next = Node(4)
head1.next.next = Node(3)

# Create second number: 465 (in reverse as 5 -> 6 -> 4)
head2 = Node(5)
head2.next = Node(6)
head2.next.next = Node(4)

# Expected result: 807 → 7 -> 0 -> 8

sol = Solution()
result = sol.addtwo(head1, head2)

print("Sum List:")
print_list(result)
