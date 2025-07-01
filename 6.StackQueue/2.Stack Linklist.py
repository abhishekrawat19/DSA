# LINKLIST IMPLEMENTATION IN STACK


class Node:
    def __init__(self,data):
        self.next=None
        self.data=data


class Stack:
    def __init__(self):
        self.top=None

    def push(self,x):
        if self.top == None:
            self.top=Node(x)
            return x
        else:
            newnode=Node(x)
            newnode.next=self.top
            self.top=newnode
            return x


    def pop(self):
        data=self.top.data
        self.top=self.top.next
        return data
    
    def top_most(self):
        if self.top==None:
            return "Its empty"
        data=self.top.data
        return data



stack=Stack()
print(f"Element is pushed {stack.push(3)}")
print(f"Top most element in stack is {stack.top_most()}")
print(f"Element is pushed {stack.push(2)}")
print(f"Top most element in stack is {stack.top_most()}")
print(f"Element is pushed {stack.push(1)}")


print("pop")
print(stack.pop())
print(f"Top most element in stack is {stack.top_most()}")
print("pop")
print(stack.pop())
print(f"Top most element in stack is {stack.top_most()}")
print("pop")
print(stack.pop())
print(f"Top most element in stack is {stack.top_most()}")


