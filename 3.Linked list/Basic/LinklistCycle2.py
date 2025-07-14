# linklist cycle 2 


class Solution:

    def linklistcycletwo(self,head):
        
        fast=head
        slow=head

        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next

            if slow == fast:
                hascycle=True
                break
            

        if not hascycle:
            return None
