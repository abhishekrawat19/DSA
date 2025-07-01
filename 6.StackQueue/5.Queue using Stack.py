# Queue make in implementation Stack making it two stack


class Stack:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]

    def push(self,x):
        while len(self.stack1)>0:
            self.stack2.append(self.stack1.pop())

        self.stack1.append(x)

        while len(self.stack2)>0:
            self.stack1.append(self.stack2.pop())        

    def pop(self):
        x=self.stack1[-1]
        self.stack1.pop()
        return x
        
    def peek(self):
        x=self.stack1[-1]
        return x
        


q=Stack()
q.push(2)
print(f"Pop element is {q.pop()}")
q.push(3)
print(f"Pop element is {q.pop()}")
q.push(1)
print(f"Pop element is {q.pop()}")