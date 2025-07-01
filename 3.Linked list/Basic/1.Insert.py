# Linklist


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linklist:
    def __init__(self):
        self.head=None

    def insert_at_begin(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def insert_at_end(self,data):
        curr=self.head
        newnode=Node(data)
        while curr.next!=None:
            curr=curr.next
        curr.next=newnode
        
    def insert_at_middle(self,pos,data):
        curr=self.head
        newnode=Node(data)
        for i in range(pos-1):
            curr=curr.next
        newnode.next=curr.next
        curr.next=newnode

        

    def traverse(self):
        curr=self.head
        while curr!=None:
            print(curr.data)
            curr=curr.next



ll=Linklist()
ll.insert_at_begin(10)
ll.traverse()
print()
ll.insert_at_begin(40)
ll.traverse()
print()
ll.insert_at_end(20)
ll.traverse()
print()
ll.insert_at_middle(2,2)
ll.traverse()