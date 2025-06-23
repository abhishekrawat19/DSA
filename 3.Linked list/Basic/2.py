class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class Linklist:
    def __init__(self):
        self.head=None

    def traverse(self):
        curr=self.head
        while curr!=None:
            print(curr.data)
            curr=curr.next

    def delete_at_first(self):
        self.head=self.head.next

    def delete_at_end(self):
        curr=self.head

        while curr.next.next!=None:
            curr=curr.next
        curr.next=None

    def delete_at_kth(self,pos):
        curr=self.head
        for i in range(pos-1):
            curr=curr.next
        curr.next=curr.next.next
        


ll=Linklist()
ll.head=Node(30)
ll.head.next=Node(40)
ll.head.next.next=Node(50)
ll.head.next.next.next=Node(60)
ll.traverse()
# print()
# ll.delete_at_first()
# ll.traverse()
print()
ll.delete_at_end()
ll.traverse()
print()
ll.delete_at_kth(2)
ll.traverse()