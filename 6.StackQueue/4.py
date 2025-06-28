# Linklist implementation on Queue


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.length=0

    def push(self,x):
        newnode=Node(x)
        if self.front == None:
            self.front=newnode
            self.rear=newnode

        else:
            self.rear.next=newnode
            self.rear=newnode
        self.length+=1
        return x


    def pop(self):
        if self.front == None:
            print("empty dumbo")
            return -1
        
        else:
            x=self.front.data
            self.front=self.front.next
            self.length-=1
            return x
        

    def getfront(self):
        if self.front==None:
            return -1
        x=self.front.data
        return x
    
    def size(self):
        return self.length
        


q=Queue()

print(f"Element is pop {q.pop()}")
print(f"Element is pushed {q.push(1)}")
print(f"Element is pushed {q.push(2)}")
print(f"Element is pushed {q.push(3)}")
print(f"Element at top is {q.getfront()}")

print(f"Queue size is {q.size()} ")


print(f"Element is pop {q.pop()}")
print(f"Element at top is {q.getfront()}")
print(f"Element is pop {q.pop()}")
print(f"Element is pop {q.pop()}")

print(f"Element is pop {q.pop()}")
print(f"Element is pop {q.pop()}")

print(f"Queue size is {q.size()} ")