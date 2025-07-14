# intersection of two linklist


# Intersection of two linked lists

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def getintersection(self,head1,head2):
        p1=head1
        p2=head2
        count=0
        while True:
            p1=p1.next
            p2=p2.next


            
            if p1==p2:
                return p1
            
            if p1==None:
                if count>2:
                    return 0
                p1=head2
            if p2==None:
                p2=head1

            


            

# Helper to print list from a node
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Create intersecting lists:
# List A: 1 -> 2 \
#                  -> 8 -> 9
# List B:     3  /

# Shared part
intersect = ListNode(8)
intersect.next = ListNode(9)

# First list
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = intersect

# Second list
head2 = ListNode(3)
head2.next = intersect

# Run test
sol = Solution()
node = sol.getintersection(head1, head2)

# Print result
if node:
    print("Intersection at node with value:", node.val)
else:
    print("No intersection.")
